"""
Helper functions for the /search endpoint
"""
from copy import deepcopy
from flask import jsonify

from back_end.src.api_usage import geo_locations
from back_end.src import app
from back_end.src import format_results
from back_end.src.database import database_functions as db_func


def get_properties_near_unis(params, results_per_page=50):
    """
    Returns all those properties within the vicinity of a university

    :param params: The parameters passed
    :param results_per_page: A query result is divided into 'pages' by Adzuna. The maximum number of results per
                            page is 50. This specifies the number of results returned per page
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

    print("Getting universities within a radius of {} to {}...".format(params['radius_from'], params['where']))
    nearby_unis = geo_locations.get_universities_near_location(params['where'], params['radius_from'])
    print('These are the universities nearby: {}'.format(", ".join([x[0] for x in nearby_unis])))

    if not nearby_unis:
        return jsonify({"error": "No universities within area specified."})

    # The set of properties surrounding those universities
    properties = []

    # Searching for houses from each university
    for uni in nearby_unis:
        name = uni[0]
        post = uni[3]
        uni_params = deepcopy(params)
        uni_params['where'] = post
        uni_params['distance'] = params['km_away_from_uni']

        # Formatting parameters for use by adzuna
        uni_params = format_results.format_params(uni_params)
        results = app.adzuna.get_property_listing(uni_params, results_per_page=results_per_page)

        # Ensuring that listings unseen and queries unseen are populated into the table. If they are, they should be
        # taken out for immediate access
        query_id = format_results.hashed_params(uni_params)

        # Checking if query has already been processed
        already_processed = db_func.query_already_processed(query_id)
        if already_processed:
            print("Query already processed for {} with a radius of {}km. Getting results..."
                  .format(name, uni_params['distance']))
            results = already_processed
        else:
            # Query has never been processed, process it
            print("This query has not been seen before. Processing results for {} with a radius of {}..."
                  .format(name, uni_params['distance']))
            large_images = format_results.large_images_only(results)
            db_func.populate_seen_tables(results, large_images, query_id, params)

        for r in results:
            # Assigning that property to a particular university
            r['university'] = uni[0]

            if r not in properties:
                properties.append(r)

    return properties


def get_all_listings(params):
    """
    Currently, Adzuna only allows for up to 50 results per 'page'. The issue is that the results can be far, far more
    than only 50 properties. This leads to an issue whereby properties are lost and unaccounted for when searching.

    This method rectifies this issue by looping through these pages and obtaining all results (not just a subset)

    :return:
    """
    property_listing = app.adzuna.get_property_listing(params)

    return property_listing


# def format_results(results, params):
#     """
#     Formats results such that we only return ones which are appropriate
#     """
#     beds = None
#     min_price = None
#     max_price = None
#     if 'beds' in params:
#         beds = params['beds']
#     if 'price_min' in params:
#         min_price = params['price_min']
#     if 'price_max' in params:
#         max_price = params['price_max']
#
#     new_results = []
#     # for r in results:
#     #     if beds and
#
#     return results
