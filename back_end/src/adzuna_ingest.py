import requests
from back_end.src import ADZUNAAPIID, ADZUNAAPIKEY


class AdzunaAPIException(Exception):
    def __str__(self):
        return "Adzuna server error"


class AdzunaAuthorisationException(Exception):
    def __str__(self):
        return "Adzuna Authorisation failed: {}"


class AdzunaRequestFormatException(Exception):
    def __str__(self):
        return "Invalid parameters for Adzuna property request"


class Adzuna:
    API_URL = 'http://api.adzuna.com/v1/api/property/gb/search/'

    def __init__(self):
        pass

    def get_property_listing(self, current_page, params=None):
        """
        Query the Adzuna API for property listings

        :param params: dict of query parameters
        :return: dict of returned results
        """
        if not params:
            params = {}

        params.update({"app_id": ADZUNAAPIID})
        params.update({"app_key": ADZUNAAPIKEY})
        params.update({"category": "for-sale"})
        base_url = self.API_URL + str(current_page)
        response = requests.get(base_url, params=params)

        if response.ok:
            results = response.json()
            return results
        elif response.status_code == 400:
            raise AdzunaRequestFormatException
        elif response.status_code == 410:
            raise AdzunaAuthorisationException
        elif response.status_code in [404, 500]:
            raise AdzunaAPIException


# if __name__ == "__main__":
#     ad = Adzuna()
#     result = ad.api_call(params={"location0": "UK",
#                         "location1": "South East England"})
#     a = result.get("results")
#     b =
#     print(result.get("results"))
#     print(result)
