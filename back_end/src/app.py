"""
Endpoints for our Flask API
"""
from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
from back_end.src.api_usage import adzuna_ingest
import uuid
import psycopg2.extras as psql_extras

from back_end.src.database import database_functions as db_func
from back_end.src import DEVELOPMENT
from back_end.src.api_usage import geo_locations
from back_end.src import format_results
from back_end.src import property_price_predictions_helper as ppp_helper
from back_end.src import seach_helper
from back_end.src import uni_nearby_ads

adzuna = adzuna_ingest.Adzuna()
app = Flask(__name__)
CORS(app)

# Valid parameters for adzuna
valid_adzuna_params = {'country', 'app_id', 'app_key', 'page', 'results_per_page', 'what', 'what_and', 'what_phrase',
                       'what_or', 'what_exclude', 'title_only', 'location0', 'location1', 'location2', 'location3',
                       'location4', 'location5	', 'location6', 'location7', 'where', 'distance', 'max_days_old',
                       'category', 'sort_direction', 'sort_by', 'beds', 'is_furnished', 'price_min', 'price_max',
                       'price_include_unknown', 'property_type'}


@app.route('/')
def hello_world():
    """
    First hello world thing
    """
    return 'Hello, World!'


@app.route('/testad')
def test_admission():
    """
    An endpoint for returning historic and predicted admissions for a given university

    :return: University admissions data
    """
    params = request.args.to_dict()
    university = params["university"]
    result = db_func.query_predicted_admission_data(university)
    historic_data, predicted_data = ppp_helper.parse_prediction_data_from_db(result)
    return_data = {"historic": {"x": historic_data[0], "y": historic_data[1]},
                   "predicted": {"x": predicted_data[0], "y": predicted_data[1]}}
    return jsonify(return_data)


@app.route('/coords')
def coordinates_endpoint():
    """
    Given a postcode, return coordinates

    :return: Coordinates (jsonified)
    """
    params = request.args.to_dict()
    postcode = params['where']
    coords = geo_locations.get_coords_from_postcode(postcode)
    return jsonify(coords)


@app.route('/test_data', methods=['GET', 'POST'])
@crossdomain(origin='*')
def test_data():
    """
    Jsonified test data
    """
    if request.method == 'POST':
        return 'ok'
    elif request.method == 'GET':
        return jsonify({'result': {'data': [1, 2, 3, 4, 5, 9, 10, 7, 8]}})


@app.route('/search')
def query_property_listing():
    """
    Query the Adzuna API for property listings using the received parameters

    :return: Property listing
    """
    params = request.args.to_dict()
    # The params collected exclusively for preprocessing
    preprocessing_params = {}
    if 'where' in params:
        preprocessing_params['where'] = params['where']
    if 'distance' in params:
        preprocessing_params['distance'] = params['distance']
    if 'km_away_from_uni' in params:
        preprocessing_params['km_away_from_uni'] = params['km_away_from_uni']
    if 'radius_from' in params:
        preprocessing_params['radius_from'] = params['radius_from']

    # Converting the parameters to a hash (that is deterministic)
    string_to_hash = []
    for p in sorted(preprocessing_params):
        string_to_hash.append(p + '&' + preprocessing_params[p])
    string_to_hash = ';'.join(string_to_hash)
    query_id = uuid.uuid3(uuid.NAMESPACE_DNS, string_to_hash)
    query_id = psql_extras.UUID_adapter(query_id)

    # If query has already been processed, get results
    already_processed = db_func.query_already_processed(query_id)

    if 'testing' in params:
        print("Testing has been enabled.")

    if already_processed and 'testing' not in params:
        print("Query already processed... Getting results")
        # The final results after processing
        final_result = already_processed
    else:
        print("This query has not been seen before.")
        # Query has not been processed before and therefore must be processed as new
        try:
            # If we are testing, we only want the distance and where in order to generate results
            if 'testing' in params and params['testing'] == 'uni_nearby_ads':
                test_params = dict()
                test_params['where'] = params['where']
                test_params['distance'] = params['distance']
                results = adzuna.get_property_listing(test_params, results_per_page=10)
                uni_nearby_ads.get_ads_near_uni("University of Southampton", results, params['distance'])
            else:
                results = seach_helper.get_properties_near_unis(params)

            if not results:
                return jsonify({"error": "No results returned"})
            else:
                if 'testing' not in params:
                    print("Getting large images...")
                    # Obtain all of those results which have large images available
                    large_images = format_results.large_images_only(results)

                    print("Populating seen_queries and seen_adverts tables...")
                    # Populates seen_queries and seen_adverts tables with results of query
                    db_func.populate_seen_tables(results, large_images, query_id, preprocessing_params)
                else:
                    large_images = results

                # The final results after processing
                final_result = large_images

        except adzuna_ingest.AdzunaAuthorisationException:
            return jsonify({"error": 410})
        except adzuna_ingest.AdzunaRequestFormatException:
            return jsonify({"error": 400})
        except adzuna_ingest.AdzunaAPIException:
            return jsonify({"error": 500})

    # formatted_results = format_results(final_result, params)

    if 'testing' in params and params['testing'] == 'uni_nearby_ads':
        return jsonify(final_result)

    # print("Building the machine learning model for outcodes...")
    # Builds the results with other metadata into a format to be consumed by frontend
    property_dict = format_results.build_property_dict(final_result)
    print("Finished.")
    return jsonify(property_dict)


if __name__ == '__main__':
    if DEVELOPMENT:
        app.run(host='0.0.0.0', port=5005, debug=True)
    else:
        app.run(debug=False)
