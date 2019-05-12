from back_end.src.import_data_to_db import DatabaseHandler


class AdzunaResponseProcessor:

    def __init__(self):
        self.db = DatabaseHandler

    def query_by_postcode(self, response_data):
        returned_house_prices = []
        for response in response_data:
            postcode = response.get("postcode")
            if postcode is not None:
                query_results = self.db.query_database("SELECT * FROM house_price_data WHERE "
                                                       "postcode = '{}'".format(postcode))
                returned_house_prices = returned_house_prices + query_results
