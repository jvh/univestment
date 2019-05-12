from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
from back_end.src.adzuna_ingest import Adzuna, AdzunaAPIException, \
    AdzunaAuthorisationException, AdzunaRequestFormatException
from back_end.src.database.import_data_to_db import DatabaseHandler
from back_end.src import DEVELOPMENT
from back_end.src import vision
from uuid import uuid4
import psycopg2.extras as psql_extras

adzuna = Adzuna()
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


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

@app.route('/search')
def query_property_listing():
    """
    Query the Adzuna API for property listings using the received parameters

    :return: Property listing
    """
    params = request.args.to_dict()

    try:
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
                r['hd_img'] = large

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

