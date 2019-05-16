"""
Formats results into a usable states
"""
import uuid
from copy import deepcopy
from psycopg2 import extras as psql_extras

from back_end.src.api_usage import google_vision
from back_end.src import app
from back_end.src.database import database_functions as db_func
from back_end.src import property_price_predictions_helper as ppd_helper
from back_end.src.database import generic_db_functions as general_db_fun


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
        result = general_db_fun.query_database(query)

        if result:
            large = result[0][-1]
        # Doesn't exist in the DB, place in there
        else:
            large = google_vision.get_large_from_thumbnail(img)
            gen_id = uuid.uuid4()
            gen_id = psql_extras.UUID_adapter(gen_id)
            params = (gen_id, img, large)
            query = "INSERT INTO img_thumbnail_to_lrg VALUES (%s, %s, %s);"
            general_db_fun.insert_to_db(query, params)
        if large:
            r['image_url'] = large
            new_results.append(r)

    return new_results


def hashed_params(params):
    """
    Hashes parameters into a deterministic UUID3 format

    :param params: The parameters
    :return: The UUID3 representation of those params
    """
    string_to_hash = []
    for p in sorted(params):
        string_to_hash.append(p + '&' + str(params[p]))
    string_to_hash = ';'.join(string_to_hash)
    query_id = uuid.uuid3(uuid.NAMESPACE_DNS, string_to_hash)
    query_id = psql_extras.UUID_adapter(query_id)

    return query_id


def format_params(params):
    """
    Formats a set of given parameters for use by adzuna

    :param params: The params requiring formatting
    :return: Params which are now able to be used to adzuna
    """
    for p in deepcopy(params):
        if p not in app.valid_adzuna_params:
            del params[p]
    return params


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
    img_url = None
    number_beds = None
    if 'university' in p:
        uni = p['university']
    if p in large_images:
        lrg = True
    if 'property_type' in p:
        p_type = p['property_type']
    if 'image_url' in p:
        img_url = p['image_url']
    if 'beds' in p:
        number_beds = p['beds']
    params = (p['id'], number_beds, p['description'], img_url, p['is_furnished'], p['latitude'], p['longitude'],
              p['postcode'], p_type, p['redirect_url'], p['sale_price'], p['title'], uni, lrg)
    return params


def build_property_dict(results):
    """
    Build the structure of the return json file

    :param results: list(properties) - list of property data
    :return: dict of data to return
    """
    # historic_prices, predicted_prices = ppd_helper.get_existing_outcode_processing(results)
    # estimates = {}
    formatted_json = {}

    # Unique set of universities connected to all houses in property_results
    universities = set()
    # Set of outcodes encompassing the property listings
    outcodes = set()

    # Stores the property results
    property_results = []
    # Contains information on the admissions data from each uni
    university_admissions_data = []
    # Outcode information
    outcode_price_data = []
    outcode_price_data_dict = dict()

    # Gathering outcodes
    for r in results:
        # Getting outcode of each property
        postcode = r['postcode']
        outcode = postcode[:len(postcode) - 3]
        r['outcode'] = outcode
        outcodes.add(outcode)

        # Getting all of the universities
        uni = r['university']
        universities.add(uni)

    # University admissions data
    for u in universities:
        admissions = db_func.query_predicted_admissions(u)
        university_admissions_data.append(admissions)

    # Outcode price point predictions data
    for o in outcodes:
        db_func.insert_price_data_if_not_exist(o)
        ppd_outcode = db_func.get_property_price_data_for_outcode(o)
        outcode_price_data.append(ppd_outcode)
        outcode_price_data_dict[o] = ppd_outcode

    # Individual listing data
    for r in results:
        p_data = dict()
        postcode = r['postcode']
        outcode = r['outcode']
        p_data['data'] = r

        # Getting outcode price data and finding an estimate of the predicted price (obtaining market_value)
        investment_dict = dict()
        outcode_pd = outcode_price_data_dict[outcode]
        # Getting the latest historic data and earliest predicted for prediction of market return
        latest_historic_price = float(outcode_pd['historic']['y'][-1])
        predicted_first = float(outcode_pd['predicted']['y'][0])
        estimated_return = ppd_helper.get_current_estimate(latest_historic_price, predicted_first)
        investment_dict['market_value'] = estimated_return
        p_data['investment'] = investment_dict

        # Properties existing within that postcode
        p_data["postcode"] = db_func.query_by_postcode(postcode)

        property_results.append(p_data)

    formatted_json['properties'] = property_results
    formatted_json["universities"] = university_admissions_data
    formatted_json["outcodes"] = outcode_price_data

    return formatted_json
