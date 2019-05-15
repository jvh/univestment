from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
from back_end.src.adzuna_ingest import Adzuna, AdzunaAPIException, \
    AdzunaAuthorisationException, AdzunaRequestFormatException
from back_end.src.database.import_data_to_db import DatabaseHandler
from back_end.src.response_processing import AdzunaResponseProcessor

from back_end.src import DEVELOPMENT
from back_end.src import vision
import uuid
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
                'location4', 'location5	', 'location6', 'location7', 'where', 'distance', 'max_days_old',
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
        if 'image_url' not in r:
            continue

        img = r['image_url']
        query = "SELECT * FROM img_thumbnail_to_lrg WHERE thumbnail_url='{}';".format(img)
        result = DatabaseHandler.query_database(query)

        if result:
            large = result[0][-1]
        # Doesn't exist in the DB, place in there
        else:
            large = vision.get_large_from_thumbnail(img)
            gen_id = uuid.uuid4()
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


def query_already_processed(query_id):
    """
    If a query has already been processed, get its results

    :param query_id: ID of the query
    :return: If it has been processed, return list of results
    """
    query = "SELECT properties FROM seen_queries WHERE id={}".format(query_id)
    if_processed = DatabaseHandler.query_database(query)

    # If the query has been processed beforehand
    if if_processed:
        [[unpacked]] = list(if_processed)
        # Get IDs of those advertisements part of this query
        results = unpacked.split(' ')

        results_from_db_lrg = []
        for r in results:
            query = "SELECT * FROM seen_adverts WHERE id={}".format(r)
            [db_res] = DatabaseHandler.query_database(query)

            record = dict()
            record['has_large_img'] = db_res[14]
            # Don't include
            if not record['has_large_img']:
                continue
            record['id'] = db_res[0]
            record['beds'] = db_res[1]
            record['description'] = db_res[2]
            record['image_url'] = db_res[3]
            record['is_furnished'] = db_res[4]
            record['latitude'] = db_res[5]
            record['longitude'] = db_res[6]
            record['postcode'] = db_res[7]
            record['property_type'] = db_res[8]
            record['redirect_url'] = db_res[9]
            record['sale_price'] = db_res[10]
            record['title'] = db_res[11]
            record['university'] = db_res[12]
            record['date_of_insertion'] = db_res[13]

            results_from_db_lrg.append(record)

        return results_from_db_lrg


def get_properties_near_unis(params):
    """
    Returns all those properties within the vicinity of a university

    :param params: The parameters passed
    :return: The list of properties near the universities
    """
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
        results = adzuna.get_property_listing(uni_params)

        for r in results:
            # Assigning that property to a particular university
            r['university'] = uni[0]
            if r not in properties:
                properties.append(r)

    return properties


def get_property_args(p, large_images):
    """
    For a given advertisement, get the property parameters for table insertion
    :param p: The property
    :param large_images: The large image results
    :return: The parameters for insertion into table
    """
    uni = None
    lrg = False
    p_type = 'N/A'
    if 'university' in p:
        uni = p['university']
    if p in large_images:
        lrg = True
    if 'property_type' in p:
        p_type = p['property_type']
    params = (p['id'], p['beds'], p['description'], p['image_url'], p['is_furnished'], p['latitude'], p['longitude'],
              p['postcode'], p_type, p['redirect_url'], p['sale_price'], p['title'], uni, lrg)
    return params


def populate_seen_tables(results, large_images, query_id, params):
    """
    When a new query is ran, populate the seen tables (seen_queries and seen_adverts) with their corresponding data.

    :param results: The resulting advertisements given by a query
    :param large_images: The list of results which have large images
    :param query_id: The UUID of the query
    :param params: Params given by the user for the query
    """
    # The list of property IDs in the results (of the advertisements)
    property_id_list = []

    # Adding advertisements to seen_adverts table
    for r in results:
        property_id_list.append(r['id'])
        args = (r['id'],)

        # Identify if the property advertisement has already been seen by the table
        seen_property_listing = "SELECT id FROM seen_adverts WHERE id=%s;"
        seen_before = DatabaseHandler.query_database(seen_property_listing, args)

        # If it has been seen, update date
        if seen_before:
            search_property_query = "UPDATE seen_adverts SET date_of_insertion=DEFAULT WHERE id=%s;"
            DatabaseHandler.insert_to_db(search_property_query, args)
        else:
            # Add it to the table
            add_property_query = "INSERT INTO seen_adverts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                 "%s, %s, %s, DEFAULT, %s);"
            args = get_property_args(r, large_images)
            DatabaseHandler.insert_to_db(add_property_query, args)

    # Add it to the table seen_queries
    add_query = "INSERT INTO seen_queries VALUES (%s, %s, %s, DEFAULT);"
    args = (query_id, str(params), ' '.join(str(e) for e in property_id_list))
    DatabaseHandler.insert_to_db(add_query, args)


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


def get_all_listings(params):
    """
    Currently, Adzuna only allows for up to 50 results per 'page'. The issue is that the results can be far, far more
    than only 50 properties. This leads to an issue whereby properties are lost and unaccounted for when searching.

    This method rectifies this issue by looping through these pages and obtaining all results (not just a subset)

    :return:
    """
    property_listing = adzuna.get_property_listing(params)

    return property_listing


def format_results(results, params):
    """
    Formats results such that we only return ones which are appropriate
    """
    beds = None
    min_price = None
    max_price = None
    if 'beds' in params:
        beds = params['beds']
    if 'price_min' in params:
        min_price = params['price_min']
    if 'price_max' in params:
        max_price = params['price_max']

    new_results = []
    # for r in results:
    #     if beds and

    return results


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
    already_processed = query_already_processed(query_id)

    if already_processed:
        print("Query already processed... Getting results")
        # The final results after processing
        final_result = already_processed
    else:
        print("This query has not been seen before.")
        # Query has not been processed before and therefore must be processed as new
        try:
            results = get_properties_near_unis(params)

            if not results:
                return jsonify({"error": "No results returned"})
            else:
                print("Getting large images...")
                # Obtain all of those results which have large images available
                large_images = large_images_only(results)

                print("Populating seen_queries and seen_adverts tables...")
                # Populates seen_queries and seen_adverts tables with results of query
                populate_seen_tables(results, large_images, query_id, preprocessing_params)

                # The final results after processing
                final_result = large_images

        except AdzunaAuthorisationException:
            return jsonify({"error": 410})
        except AdzunaRequestFormatException:
            return jsonify({"error": 400})
        except AdzunaAPIException:
            return jsonify({"error": 500})

    formatted_results = format_results(final_result, params)

    print("Building the machine learning model for outcodes...")
    # Builds the results with other metadata into a format to be consumed by frontend
    property_dict = build_property_dict(formatted_results)
    print("Finished.")
    return jsonify(property_dict)


if __name__ == '__main__':
    if DEVELOPMENT:
        app.run(host='0.0.0.0', port=5005, debug=True)
    else:
        app.run(debug=False)

