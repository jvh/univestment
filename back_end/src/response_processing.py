import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR
from back_end.src.database.import_data_to_db import DatabaseHandler


class AdzunaResponseProcessor:

    def __init__(self):
        self.db = DatabaseHandler

    def query_by_postcode(self, postcode):
        """
        Query database for properties by postcode

        :param response_data: response object containing parameters
        :return:
        """
        query = "SELECT * FROM house_price_data WHERE postcode = '{}' ORDER BY date_of_transfer;".format(postcode)
        results = DatabaseHandler.query_database(query)
        return results

    def query_for_price_data(self, outcode):
        #print(outcode)
        query = "SELECT historical_data, prediction_data FROM predictions_data WHERE outcode = '{}';".format(outcode)
        results = DatabaseHandler.query_database(query)
        #print(results)
        return results

    def query_by_outcode(self, outcodes):
        """
        Query database for properties by outcode

        :param response_data: response object containing parameters
        :return:
        """
        #returned_house_prices_street = []
        #returned_house_prices_area = []
        for outcode in outcodes:
            query = "SELECT outcode FROM predictions_data WHERE outcode = '{}'".format(outcode)
            result = DatabaseHandler.query_database(query)

            if not result:
                query_results_area = self.db.query_database("SELECT * FROM house_price_data WHERE substr(postcode,1,{})"
                                                            " = '{}' ORDER BY date_of_transfer;"
                                                            .format(len(outcode), outcode))

                # returned_house_prices_area = returned_house_prices_area + query_results_area
                if query_results_area:
                    start_date, historic_data, predicted_data = self.generate_prediction(query_results_area)
                    #print("{} {} {}".format(start_date, historic_data, predicted_data))
                    #print("inserting: {} {} {} {}".format(outcode, start_date, historic_data, predicted_data))
                    self.insert_predictions(outcode, start_date, historic_data, predicted_data)
                    #return points, price, query_results_area

    def generate_prediction(self, data):
        """
        Create and train a autoregressive model and predict property prices for the next 24 months

        :param data:
        :return: list(int) of points, list(int) of prices
        """
        pricing_data = pd.DataFrame(data)
        pricing_data = pricing_data.drop(columns=[0, 3, 4, 5, 6, 7])
        pricing_data.rename(columns={1: "price", 2: "date"}, inplace=True)
        pricing_data.date = pd.to_datetime(pricing_data.date, infer_datetime_format=True)

        #Remove outliers (more than 3 s.d. from mean)
        pricing_data = pricing_data[np.abs(pricing_data.price - pricing_data.price.mean())
                                    <= (3 * pricing_data.price.std())]
        pricing_data.set_index(pricing_data.date, inplace=True)
        pricing_data = pricing_data.groupby(pd.Grouper(freq='M')).mean().dropna()

        #Generate autoregressive model
        model = AR(pricing_data["price"])
        model_fit = model.fit()

        #predict next 24 months
        predictions = model_fit.predict(len(pricing_data["price"]), len(pricing_data["price"]) + 23)

        start_date = pricing_data.index.to_series().tolist()[0]
        #print('-----------------------')
        #print(pricing_data.index)

        historic_points = pricing_data.index.to_series().apply(lambda x: pd.datetime.strftime(x, '%m:%Y'))\
            .tolist()
        historic_points = self.generate_date_points(historic_points)
        predicted_points = [i+len(historic_points)+1 for i in range(24)]

        historic_prices = pricing_data["price"].tolist()
        predicted_prices = predictions.tolist()

        historic_data = (historic_points, historic_prices)
        predicted_data = (predicted_points, predicted_prices)

        return start_date, historic_data, predicted_data

    @staticmethod
    def insert_predictions(outcode, start_date, historic, predictions):
        historic_data = str(historic[0]) + ":" + str(historic[1])
        predictions_data = str(predictions[0]) + ":" + str(predictions[1])
        params = (outcode, start_date, historic_data, predictions_data)
        #print(params[2])
        query = "INSERT INTO predictions_data VALUES (%s, %s, %s, %s)"
        DatabaseHandler.insert_to_db(query, params)

    @staticmethod
    def generate_date_points(dates):
        """
        generate date points for timeseries

        :param dates: list(String)
        :return: list(int)
        """
        current_year = int(dates[0].split(":")[1])
        year_modifier = 0
        points = []

        for date in dates:
            year = int(date.split(":")[1])
            if year > current_year:
                year_modifier += 12 * (year-current_year)
                current_year = year
            current_point = int(date.split(":")[0])
            points.append(current_point+year_modifier)
        return points
