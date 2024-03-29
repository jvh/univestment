"""
Endpoints for our Flask API
"""
from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
import datetime

from back_end.src.api_usage import adzuna_ingest
from back_end.src.database import database_functions as db_func
from back_end.src import DEVELOPMENT
from back_end.src.api_usage import geo_locations
from back_end.src import format_results
from back_end.src.predictions import property_price_predictions_helper as ppp_helper
from back_end.src import seach_helper

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
    print('\nCurrent time: {}'.format(datetime.datetime.now()))
    # The arguments passed into /search endpoint (in the format /search?arg1=arg1_val&arg2=arg2_val&...)
    params = request.args.to_dict()

    # Simplified parameters of input parameters to better describe parameters input
    simplified_params = dict()
    simplified_params['where'] = params['where']
    simplified_params['km_away_from_uni'] = params['km_away_from_uni']
    simplified_params['radius_from'] = params['radius_from']
    simplified_query_id = format_results.hash_params(simplified_params)

    # If the query has already been seen before, set results
    already_processed = db_func.query_already_processed(simplified_query_id)
    if already_processed:
        print('This particular query, {}, has already been processed. Getting results...'.format(simplified_params))
        results = already_processed
    else:
        if 'testing' in params:
            print("Testing has been enabled.")

        try:
            if 'testing' in params:
                results = seach_helper.get_properties_near_unis(params, 10)
            else:
                results = seach_helper.get_properties_near_unis(params)

            if not results:
                return jsonify({"error": "No results returned"})

        except adzuna_ingest.AdzunaAuthorisationException:
            return jsonify({"error": 410})
        except adzuna_ingest.AdzunaRequestFormatException:
            return jsonify({"error": 400})
        except adzuna_ingest.AdzunaAPIException:
            return jsonify({"error": 500})

    # Builds the results with other metadata into a format to be consumed by frontend
    property_dict, property_results = format_results.build_property_dict(results)

    # for r in property_results:
    #     print(r)

    if not already_processed:
        print("Populating seen tables for this particular query: {}".format(simplified_params))
        db_func.populate_seen_tables([x['data'] for x in property_results], [], simplified_query_id, simplified_params)

    print("Finished.")
    return jsonify(property_dict)


if __name__ == '__main__':
    if DEVELOPMENT:
        app.run(host='0.0.0.0', port=5005, debug=True)
    else:
        app.run(debug=False)
