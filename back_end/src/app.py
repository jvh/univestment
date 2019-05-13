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
import time


adzuna = Adzuna()
app = Flask(__name__)
CORS(app)
db = DatabaseHandler()
arp = AdzunaResponseProcessor()

# Valid parameters for adzuna
valid_adzuna_params = {'country', 'app_id', 'app_key', 'page', 'results_per_page', 'what', 'what_and', 'what_phrase',
                'what_or', 'what_exclude', 'title_only', 'location0', 'location1', 'location2', 'location3',
                'location4', 'location5	', 'location6', 'location7', 'where', ' distance', 'max_days_old',
                'category', 'sort_direction', 'sort_by', 'beds', 'is_furnished', 'price_min', 'price_max',
                'price_include_unknown', 'property_type'}


@app.route('/')
def hello_world():
    return 'Hello, World!'


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
    if request.method == 'POST':
        return 'ok'
    elif request.method == 'GET':
        return jsonify({'result': {'data': [1, 2, 3, 4, 5, 9, 10, 7, 8]}})


def large_images_only(results):
    """
    Gets those properties with large images only (not only thumbnails)
    """
    new_results = []

    for i in range(len(results)):
        r = results[i]
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
            new_results.append(r)

    return new_results


def format_params(params):
    """
    Formats a set of given parameters for use by adzuna

    :param params: The params requiring formatting
    :return: Params which are now able to be used to adzuna
    """
    for p in deepcopy(params):
        if p not in valid_adzuna_params:
            del params[p]
    return params


@app.route('/search')
def query_property_listing():
    """
    Query the Adzuna API for property listings using the received parameters

    :return: Property listing
    """
    params = request.args.to_dict()
    results = []
    final_response = []
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

            if not nearby_unis:
                return jsonify({"error": "No universities within area specified."})

            # The set of properties surrounding those universities
            properties = []

            # Searching for houses from each university
            for uni in nearby_unis:
                post = uni[3]
                uni_params = deepcopy(params)
                uni_params['where'] = post
                uni_params['distance'] = params['km_away_from_uni']

                # Formatting parameters for use by adzuna
                uni_params = format_params(uni_params)
                property_listing = adzuna.get_property_listing(uni_params)
                results = property_listing.get("results")

                for r in results:
                    # Assigning that property to a particular university
                    r['university'] = uni[0]
                    if r not in properties:
                        properties.append(r)

        else:
            params = format_params(params)
            property_listing = adzuna.get_property_listing(params)
            results = property_listing.get("results")
            print()

        if not results:
            return jsonify({"error": "No results returned"})
        else:
            results = large_images_only(results)
            property_dict = build_property_dict(results)
            final_response = property_dict

            for r in results:
                img = r['image_url']
                query = "SELECT * FROM img_thumbnail_to_lrg WHERE thumbnail_url='{}';".format(img)
                result = DatabaseHandler.query_database(query)

                if result:
                    large = result[0][-1]
                # Doesn't exist in the DB, place in there
                else:
                    #large = vision.get_large_from_thumbnail(img)
                    gen_id = uuid4()
                    gen_id = psql_extras.UUID_adapter(gen_id)
                    params = (gen_id, img, large)
                    query = "INSERT INTO img_thumbnail_to_lrg VALUES (%s, %s, %s);"
                    DatabaseHandler.insert_to_db(query, params)

                if large:
                    r['image_url'] = large

        return jsonify(final_response)
    except AdzunaAuthorisationException:
        return jsonify({"error": 410})
    except AdzunaRequestFormatException:
        return jsonify({"error": 400})
    except AdzunaAPIException:
        return jsonify({"error": 500})


def build_property_dict(results):
    historic_prices, predicted_prices = get_existing_outcode_processing(results)
    estimates = {}
    final_list = []
    for property in results:
        if "postcode" not in property:
            continue

        outcode = property["postcode"][:len(property["postcode"]) - 3]

        current_estimate = get_current_estimate(historic_prices[outcode][1][-1], predicted_prices[outcode][1][0])
        estimates[outcode] = current_estimate

        property_dict = {"property": {"adzuna": property}}

        # placeholder
        property_dict["property"]["investment"] = {"market_value": current_estimate}

        property_dict["historic_data"] = {"outcode": {"historic": {"x": historic_prices[outcode][0],
                                                                   "y": historic_prices[outcode][1]}}}
        property_dict["historic_data"]["outcode"]["predicted"] = {"x": predicted_prices[outcode][0],
                                                                  "y": predicted_prices[outcode][1]}

        property_dict["postcode"] = {"property": list(arp.query_by_postcode(property.get("postcode")))}
        final_list.append(property_dict)
    return final_list


def get_current_estimate(historic_month, predicted_month):
    """
    estimate the current value of a property

    :param historic_month: predicted value from previous month
    :param predicted_month: predicted value for next month
    :return: estimated value
    """
    today = int(time.strftime("%d"))
    delta = (predicted_month - historic_month)/30
    estimate = historic_month + (today * delta)
    return estimate


def get_existing_outcode_processing(results):
    """
    Given an outcode, determine if the outcode has already undergone preprocessing. If it has, return the result from
    the database
    """
    outcodes = set()
    for x in results:
        postcode = x.get("postcode")
        if postcode:
            outcode = postcode[0:len(postcode)-3]
            outcodes.add(outcode)

    arp.query_by_outcode(outcodes)
    historic_prices = {}
    predicted_prices = {}
    for outcode in outcodes:
        query_results = arp.query_for_price_data(outcode)

        historic_data = query_results[0][0].split(":")
        historic_months = historic_data[0]
        historic_averages = historic_data[1]

        historic_months = historic_months[1:len(historic_months)-1].split(",")
        historic_averages = historic_averages[1:len(historic_averages)-1].split(",")

        historic_months = list(map(lambda x: int(x), historic_months))
        historic_averages = list(map(lambda x: float(x), historic_averages))

        predicted_data = query_results[0][1].split(":")
        predicted_months = predicted_data[0]
        predicted_averages = predicted_data[1]

        predicted_months = predicted_months[1:len(predicted_months) - 1].split(",")
        predicted_averages = predicted_averages[1:len(predicted_averages) - 1].split(",")

        predicted_months = list(map(lambda x: int(x), predicted_months))
        predicted_averages = list(map(lambda x: float(x), predicted_averages))

        historic_prices[outcode] = (historic_months, historic_averages)
        predicted_prices[outcode] = (predicted_months, predicted_averages)
    return historic_prices, predicted_prices


if __name__ == '__main__':
    if DEVELOPMENT:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(debug=False)

