"""
Requesting information from Adzuna API
"""
import requests
import math

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

    def __init__(self):
        self.API_URL = 'http://api.adzuna.com/v1/api/property/gb/search/'

    @staticmethod
    def get_properties_per_page(params, url):
        """
        Gets the properties existing from the given url
        :param params: The parameters passed
        :param url: The url request
        :return: The properties from that url request
        """
        response = requests.get(url, params=params)
        if response.ok:
            results = response.json()
            return results
        elif response.status_code == 400:
            raise AdzunaRequestFormatException
        elif response.status_code == 410:
            raise AdzunaAuthorisationException
        elif response.status_code in [404, 500]:
            raise AdzunaAPIException

    def get_property_listing(self, params, results_per_page=50):
        """
        Query the Adzuna API for property listings

        :param params: dict of query parameters
        :param results_per_page: A query result is divided into 'pages' by Adzuna. The maximum number of results per
                                 page is 50. This specifies the number of results returned per page.
        :return: dict of returned results
        """
        # Defining necessary parameters
        if not params:
            params = {}
        params.update({"app_id": ADZUNAAPIID})
        params.update({"app_key": ADZUNAAPIKEY})
        params.update({"category": "for-sale"})
        params.update({'results_per_page': results_per_page})

        results = []

        url = self.API_URL + str(1)
        r = self.get_properties_per_page(params, url)
        for result in r['results']:
            results.append(result)

        # Getting the total count in order to determine the number of pages necessary
        count = int(r['count'])

        # Only reason to set results < 50 would be testing, so we only need the first page
        if results_per_page < 50:
            return results

        number_pages = math.ceil(count / results_per_page)

        # Collecting all those properties delivered by Adzuna (across all pages)
        # for i in range(2, 5):
        #     page_number = i
        #     url = self.API_URL + str(page_number)
        #
        #     # Getting the response from this single place
        #     r = self.get_properties_per_page(params, url)
        #     for result in r['results']:
        #         results.append(result)

        return results
