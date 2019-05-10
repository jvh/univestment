from zoopla import Zoopla, exceptions as ZooplaExceptions

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
        except ZooplaExceptions.RequestFormatException:
            raise ZooplaExceptions.RequestFormatException("Invalid parameters for property listing request. See"
                                                          "Zoopla API docs for valid parameters.")
        except ZooplaExceptions.ResponseFormatException:
            raise ZooplaExceptions.ResponseFormatException("Property listing request returned unexpected parameters."
                                                           "This may be due to changes in the Zoopla API.")
        except ZooplaExceptions.ZooplaAPIException as e:
            raise ZooplaExceptions.ZooplaAPIException(str(e))


if __name__ == "__main__":
    zi = ZooplaIngest()
