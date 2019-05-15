"""
Helper functions for the /search endpoint
"""
from copy import deepcopy
from flask import jsonify

from back_end.src.api_usage import geo_locations
from back_end.src.app import adzuna
from back_end.src.database import database_functions as db_func
from back_end.src import format_results


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

        data = db_func.query_predicted_admissions(uni[0])

        # Formatting parameters for use by adzuna
        uni_params = format_results.format_params(uni_params)
        results = adzuna.get_property_listing(uni_params)

        for r in results:
            # Assigning that property to a particular university
            r['university'] = uni[0]
            if data:
                r["admissions"] = data
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
    property_listing = adzuna.get_property_listing(params)

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
