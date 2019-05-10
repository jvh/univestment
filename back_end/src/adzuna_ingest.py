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
    API_URL = 'http://api.adzuna.com/v1/api/property/gb/search/1'

    def __init__(self):
        pass

    def get_property_listing(self, params=None):
        if not params:
            params = {}

        params.update({"app_id": ADZUNAAPIID})
        params.update({"app_key": ADZUNAAPIKEY})
        params.update({"category": "for-sale"})
        response = requests.get(self.API_URL, params=params)

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
