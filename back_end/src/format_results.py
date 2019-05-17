"""
Formats results into a usable states
"""
import uuid
from copy import deepcopy
from psycopg2 import extras as psql_extras

from back_end.src.api_usage import google_vision
from back_end.src import app
from back_end.src.database import database_functions as db_func
from back_end.src.predictions import property_price_predictions_helper as ppd_helper
from back_end.src.database import generic_db_functions as general_db_fun
from back_end.src import average_rent
from back_end.src import mortgage_payment


def large_images_only(results):
    """
    Gets those properties with large images only (not only thumbnails)
    """
    new_results = []

    for i in range(len(results)):
        r = results[i]
        r_data = r['data']
        if 'image_url' not in r_data:
            continue

        img = r_data['image_url']
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
            r_data['image_url'] = large
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
    sale_price = None
    postcode = None

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
    if 'sale_price' in p:
        sale_price = p['sale_price']
    if 'postcode' in p:
        postcode = p['postcode']
    params = (p['id'], number_beds, p['description'], img_url, p['is_furnished'], p['latitude'], p['longitude'],
              postcode, p_type, p['redirect_url'], sale_price, p['title'], uni, lrg)
    return params


def hash_params(params):
    """
    Converts parameters into a unique hash

    :param params: parameters to generate the hash for
    :return: hash to use as query ID
    """
    # Converting the parameters to a hash (that is deterministic)
    string_to_hash = []
    for p in sorted(params):
        string_to_hash.append(p + '&' + params[p])
    string_to_hash = ';'.join(string_to_hash)
    query_id = uuid.uuid3(uuid.NAMESPACE_DNS, string_to_hash)
    query_id = psql_extras.UUID_adapter(query_id)
    return query_id


def build_property_dict_universities(university):
    """
    Builds the universities section of property_dict containing data regarding properties which encompass the
    universities

    :param university: The university you would like to gather data for
    :return: The data regarding that university
    """
    data = dict()
    admissions = db_func.query_predicted_admissions(university)

    # Getting logo if exists and putting into correct format
    logo = db_func.query_uni_logos(university)
    if logo:
        [logo] = logo
        logo = logo[0]
    else:
        logo = None

    data['name'] = university
    data['logo'] = logo
    data['admissions'] = admissions

    return data


def build_property_dict(results):
    """
    Build the structure of the return json file

    :param results: list(properties) - list of property data
    :return: dict of data to return
    """
    # The returned JSON file formatted for the web
    formatted_json = {}

    # Unique set of universities connected to all houses in property_results
    universities = set()
    # Set of outcodes encompassing the property listings
    outcodes = set()
    # The average rent for a given outcode (by number of bed) {outcode: {number_beds: rent}}
    outcode_rent = dict()

    # Stores the property results
    property_results = []
    # Contains information on the admissions data from each uni
    university_admissions_data = []
    # Outcode information
    outcode_price_data = []
    outcode_price_data_dict = dict()

    # Stores properties by uni
    property_by_university = dict()

    # Results which contain all necessary args
    legal_results = list()

    # Gathering outcodes
    for r in results:
        # Postcode in our case is compulsory
        if 'postcode' not in r:
            continue
        # Getting outcode of each property
        postcode = r['postcode']
        outcode = postcode[:len(postcode) - 3]
        r['outcode'] = outcode
        outcodes.add(outcode)

        # Getting all of the universities
        uni = r['university']
        universities.add(uni)
        legal_results.append(r)

    results = legal_results

    # University admissions data
    for u in universities:
        data = build_property_dict_universities(u)
        university_admissions_data.append(data)

    # Outcode price point predictions data
    for o in outcodes:
        db_func.insert_price_data_if_not_exist(o)
        ppd_outcode = db_func.get_property_price_data_for_outcode(o)
        outcode_price_data_dict[o] = ppd_outcode

        # Getting the average rent prices for current property listing in the outcode, divided by number of beds
        average_total_rent_by_bed = average_rent.calculate_average_total_rent_by_bed(o)
        outcode_price_data_dict[o]["average_total_rent_by_bed"] = average_total_rent_by_bed
        outcode_rent[o] = average_total_rent_by_bed

        outcode_price_data.append(ppd_outcode)

    # Populating property_by_university with the universities
    for u in universities:
        property_by_university[u] = list()

    # Individual listing data
    for r in results:
        p_data = dict()
        postcode = r['postcode']
        outcode = r['outcode']
        beds = r['beds']
        sale_price = r['sale_price']
        p_data['data'] = r
        p_uni = r['university']

        # Cannot deal with instances where there are >6 beds
        if not beds or beds > 6:
            continue

        # Getting the rent(s) for the outcode. Getting the average rent for the number of beds in this property.
        outcode_rent_data = outcode_rent[outcode]
        average_rent_for_beds = outcode_rent_data[beds]

        # In the case no properties in that postcode with x amount of beds exist
        if average_rent_for_beds == 0:
            # Setting the starting point to look for beds
            if beds == 1:
                start_beds = 2
            else:
                start_beds = beds + 1

            # Looking for properties with different beds in the same outcode for an approximation of average price
            for key in range(start_beds, 7):
                if outcode_rent_data[key] != 0:
                    average_rent_for_beds = outcode_rent_data[key] * beds/key
                    break

            if beds > 1:
                # If we still don't have average_rent, go to one below as last resort
                average_rent_for_beds = outcode_rent_data[beds-1] * beds/(beds-1)

        # Calculate mortgage payments
        mortgage_return = mortgage_payment.calculate_mortgage_return(sale_price, average_rent_for_beds)

        # Getting outcode price data and finding an estimate of the predicted price (obtaining market_value)
        investment_dict = dict()
        outcode_pd = outcode_price_data_dict[outcode]
        # Getting the latest historic data and earliest predicted for prediction of market return
        latest_historic_price = float(outcode_pd['historic']['y'][-1])
        predicted_first = float(outcode_pd['predicted']['y'][0])
        estimated_return = ppd_helper.get_current_estimate(latest_historic_price, predicted_first)
        investment_dict['market_value'] = estimated_return
        # Add mortgage repayment to return json
        mortgage_return['potential_rent_profit'] = mortgage_return["rent"] - mortgage_return["mortgage_payment"]
        investment_dict["mortgage_return"] = mortgage_return
        p_data['investment'] = investment_dict

        # Properties existing within that postcode
        p_data["postcode"] = db_func.query_by_postcode(postcode)
        property_by_university[p_uni].append(p_data)
        # property_results.append(p_data)

    property_results = get_best_properties_per_uni(property_by_university)
    formatted_json['properties'] = property_results
    formatted_json["universities"] = university_admissions_data
    formatted_json["outcodes"] = outcode_price_data

    return formatted_json


def get_best_properties_per_uni(property_by_uni, number_properties=50):
    """
    Returns the best number_properties for that university.

    :param property_by_uni: Each university's properties
    :param number_properties: The number of properties returned
    :return: The best properties for that university
    """
    print("Getting best properties...")

    # number_properties * number of unis returned
    number_properties = number_properties * len(property_by_uni)
    best_properties = list()
    for uni in property_by_uni:
        uni_properties = property_by_uni[uni]
        # Getting the best potential_rent_profit ordered
        uni_properties.sort(key=lambda k: (k['investment']['mortgage_return']['potential_rent_profit']), reverse=True)
        # Only those with a profit
        uni_properties = [x for x in uni_properties if x['investment']['mortgage_return']['potential_rent_profit'] > 0]

        best_properties.extend(uni_properties)

    # Getting top number_properties results
    best_properties = best_properties[:number_properties]

    print("Getting large images...")

    # Getting large images
    large_images = large_images_only(best_properties)
    # Getting the best overall properties
    large_images.sort(key=lambda k: (k['investment']['mortgage_return']['potential_rent_profit']), reverse=True)

    return large_images
