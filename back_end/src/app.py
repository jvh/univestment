from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
from back_end.src.adzuna_ingest import Adzuna, AdzunaAPIException, \
    AdzunaAuthorisationException, AdzunaRequestFormatException
from back_end.src.database.import_data_to_db import DatabaseHandler
from back_end.src.response_processing import AdzunaResponseProcessor

from back_end.src import DEVELOPMENT
from back_end.src import vision
from uuid import uuid4
import psycopg2.extras as psql_extras
from back_end.src import geo_locations
from copy import deepcopy

adzuna = Adzuna()
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/coords')
def coordinates_endpoint():
    params = request.args.to_dict()
    postcode = params['where']
    coords = geo_locations.get_coords_from_postcode(postcode)
    return jsonify(coords)


@app.route('/test_data', methods=['GET', 'POST'])
@crossdomain(origin='*')
def test_data():
    if request.method == 'POST':
        return 'ok'
    elif request.method == 'GET':
        return jsonify({'result': {'data': [1, 2, 3, 4, 5, 9, 10, 7, 8]}})


# @app.route('/trend_data')
# def trend_data():
#     """
#     Obtain the data for a set of movies and identify trends using time series analysis
#
#     :return: The original data along with predicted data related to movie trends
#     """
#     print(data.trends())
#
#     return 'test'

db = DatabaseHandler()
arp = AdzunaResponseProcessor()

@app.route('/search')
def query_property_listing():
    """
    Query the Adzuna API for property listings using the received parameters

    :return: Property listing
    """
    params = request.args.to_dict()

    try:
        # If the user has selected they're searching for student rental opportunities
        if "search_student_lets" in params and params["search_student_lets"] == 'true':
            if "where" not in params:
                raise Exception("Please enter a postcode.")
            elif "radius_from" not in params:
                raise Exception("Please enter a radius away from the location you have specified in which to search "
                                "against.")
            elif "km_away_from_uni" not in params:
                raise Exception("Please enter the distance from any given university (in km) that you would like to "
                                "search houses for.")

            nearby_unis = geo_locations.get_universities_near_location(params['where'], params['radius_from'])

            # Searching for houses from each university
            for uni in nearby_unis:
                post = uni[3]
                uni_params = deepcopy(params)
                uni_params['where'] = post
                uni_params['distance'] = params['km_away_from_uni']

                
                print(uni_params)
                pass

            return jsonify(params)
        else:
            property_listing = adzuna.get_property_listing(params)
            results = property_listing.get("results")

            for r in results:
                img = r['image_url']
                query = "SELECT * FROM img_thumbnail_to_lrg WHERE thumbnail_url='{}';".format(img)
                result = DatabaseHandler.query_database(query)

                if result:
                    large = result[0][-1]
                # Doesn't exist in the DB, place in there
                else:
                    large = vision.get_large_from_thumbnail(img)
                    gen_id = uuid4()
                    gen_id = psql_extras.UUID_adapter(gen_id)
                    params = (gen_id, img, large)
                    query = "INSERT INTO img_thumbnail_to_lrg VALUES (%s, %s, %s);"
                    DatabaseHandler.insert_to_db(query, params)

                if large:
                    r['image_url'] = large

        return jsonify(results)
    except AdzunaAuthorisationException:
        return jsonify({"error": 410})
    except AdzunaRequestFormatException:
        return jsonify({"error": 400})
    except AdzunaAPIException:
        return jsonify({"error": 500})


if __name__ == '__main__':
    if DEVELOPMENT:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=5000, debug=False)

