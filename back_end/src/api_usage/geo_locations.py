"""
Uses geopy for geographical information
"""
from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import certifi
import ssl
from back_end.src.database import generic_db_functions as general_db_func

ctx = ssl.create_default_context(cafile=certifi.where())
geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="http://univestment.co.uk/")


def get_coords_from_postcode(postcode):
    """
    Given a postcode, return the longitude and latitude

    :param postcode: The postcode (in the UK)
    :return: The (longitude, latitude)
    """
    # Insert space if one doesn't exist
    if postcode[-4] != ' ':
        postcode = list(postcode)
        postcode.insert(-3, ' ')
        postcode = ''.join(postcode)
    location = geolocator.geocode("{}, UK".format(postcode))

    return location.longitude, location.latitude


def get_universities_near_location(location, distance):
    """
    Returns a list of all the universities which are situated within a specific distance

    :param location: The origin of which we are searching (postcode)
    :param distance: The distance in which we are searching in km
    :return: A list of universities
    """
    long, lat = get_coords_from_postcode(location)
    origin = (long, lat)
    unis = general_db_func.query_database("SELECT * FROM uni_addresses_data")

    nearby_unis = []

    for uni in unis:
        uni_lat = uni[-2]
        uni_long = uni[-1]
        uni_loc = (uni_lat, uni_long)
        km_away = geodesic(origin, uni_loc).kilometers
        if km_away < float(distance):
            nearby_unis.append(uni)

    return nearby_unis
