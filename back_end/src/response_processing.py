import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR
from back_end.src.database.import_data_to_db import DatabaseHandler


class AdzunaResponseProcessor:

    def __init__(self):
        self.db = DatabaseHandler

    def query_by_postcode(self, response_data):
        """
        Query database for postcodes

        :param response_data:
        :return:
        """
        returned_house_prices_street = []
        returned_house_prices_area = []
        for response in response_data:
            postcode = response.get("postcode")
            if postcode is not None:
                query_results_street = self.db.query_database("SELECT * FROM house_price_data WHERE "
                                                       "postcode = '{}' ORDER BY date_of_transfer;".format(postcode))
                query_results_area = self.db.query_database("SELECT * FROM house_price_data WHERE substr(postcode,1,{}) "
                                                            "= '{}' ORDER BY date_of_transfer;".format(len(postcode)-3, postcode[0:len(postcode)-3]))
                returned_house_prices_street = returned_house_prices_street + query_results_street
                returned_house_prices_area = returned_house_prices_area + query_results_area

                points, price = self.generate_prediction(returned_house_prices_area)
                return points, price, returned_house_prices_street

    def generate_prediction(self, data):
        pricing_data = pd.DataFrame(data)
        pricing_data = pricing_data.drop(columns=[0, 3, 4, 5, 6, 7])
        pricing_data.rename(columns={1: "price", 2: "date"}, inplace=True)
        pricing_data.date = pd.to_datetime(pricing_data.date, infer_datetime_format=True)

        #Remove outliers (more than 3 s.d. from mean)
        pricing_data = pricing_data[np.abs(pricing_data.price - pricing_data.price.mean()) <= (3 * pricing_data.price.std())]
        pricing_data.set_index(pricing_data.date, inplace=True)
        pricing_data = pricing_data.groupby(pd.Grouper(freq='M')).mean().dropna()

        #Generate autoregressive model
        model = AR(pricing_data["price"])
        model_fit = model.fit()

        #predict next 24 months
        predictions = model_fit.predict(len(pricing_data["price"]), len(pricing_data["price"]) + 23)

        points = pricing_data.index.to_series().apply(lambda x: pricing_data.datetime.strftime(x, '%m')).tolist()
        time_points = self.generate_date_points(points)
        time_points += [i+len(time_points)+1 for i in range(24)]
        final_prices = pricing_data["prices"] + predictions.tolist()
        return time_points, final_prices

    @staticmethod
    def generate_date_points(dates):
        points = []
        counter = 1
        last_month = 0
        for date in dates:
            if date == 12:
                last_month = 0
                points.append(counter)
                counter += 1
            elif date != last_month + 1:
                last_month += 1
            else:
                points.append(counter)
                counter += 1

        return points
