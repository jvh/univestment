from zoopla import Zoopla, exceptions as zoopla_exceptions

from back_end.src import constants


class ZooplaIngest:

    def __init__(self):
        self.zoopla = Zoopla(api_key=constants.ZOOPLAAPIKEY)

    def get_property_listing(self, params):
        """
        Query zoopla for property listings which match a
        set of parameters

        :param params: dict(parameter:value)
        :return: dict(parameter:value)
        """
        try:
            listings = self.zoopla.property_listings(params)
            return listings
        except zoopla_exceptions.RequestFormatException:
            raise zoopla_exceptions.RequestFormatException("Invalid parameters for property listing request. See"
                                                          "Zoopla API docs for valid parameters.")
        except zoopla_exceptions.ResponseFormatException:
            raise zoopla_exceptions.ResponseFormatException("Property listing request returned unexpected parameters."
                                                           "This may be due to changes in the Zoopla API.")
        except zoopla_exceptions.ZooplaAPIException as e:
            raise zoopla_exceptions.ZooplaAPIException(str(e))


# if __name__ == "__main__":
#     zi = ZooplaIngest()
#     result = zi.get_property_listing({
#         'maximum_beds': 2,
#         'page_size': 100,
#         'listing_status': 'sale',
#         'area': 'Blackley, Greater Manchester'
#     })
#     print(result)