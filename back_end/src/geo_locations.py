from geopy import geocoders
from geopy.geocoders import Nominatim
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="http://univestment.co.uk/")


def get_coords_from_postcode(postcode):
    """
    Given a postcode, return the longitude and latitude

    :param postcode: The postcode (in the UK)
    :return: The (longitude, latitude)
    """
    postcode = postcode
    location = geolocator.geocode("{}, UK".format(postcode))

    return location.longitude, location.latitude


if __name__ == '__main__':
    print(get_coords_from_postcode('SE10 0EW'))
