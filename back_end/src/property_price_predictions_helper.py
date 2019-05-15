"""
Helper functions used for predicting market value
"""
import time

from back_end.src.database import database_functions as db_func
from back_end.src.database import generic_db_functions as general_db_func


def get_current_estimate(historic_month, predicted_month):
    """
    estimate the current value of a property

    :param historic_month: predicted value from previous month
    :param predicted_month: predicted value for next month
    :return: estimated value
    """
    today = int(time.strftime("%d"))
    delta = (predicted_month - historic_month)/30
    estimate = historic_month + (today * delta)
    return estimate


def get_existing_outcode_processing(results):
    """
    Given an outcode, determine if the outcode has already undergone preprocessing. If it has, return the result from
    the database
    """
    outcodes = set()

    for x in results:
        postcode = x.get("postcode")
        if postcode:
            outcode = postcode[0:len(postcode)-3]
            outcodes.add(outcode)

    db_func.query_by_outcode(outcodes)
    historic_prices = {}
    predicted_prices = {}

    for outcode in outcodes:
        query_results = db_func.query_for_price_data(outcode)

        historic_data, predicted_data = parse_prediction_data_from_db(query_results)

        historic_prices[outcode] = (historic_data[0], historic_data[1])
        predicted_prices[outcode] = (predicted_data[0], predicted_data[1])
    return historic_prices, predicted_prices


def parse_prediction_data_from_db(query_results):
    """
    parse prediction data from query to lists

    :param query_results: list(tuple) - results of query
    :return: Historic data, predicted data
    """
    historic_data = query_results[0][0].split(":")
    historic_months = historic_data[0]
    historic_averages = historic_data[1]

    historic_months = historic_months[1:len(historic_months) - 1].split(",")
    historic_averages = historic_averages[1:len(historic_averages) - 1].split(",")

    historic_months = list(map(lambda x: int(x), historic_months))
    historic_averages = list(map(lambda x: float(x), historic_averages))

    predicted_data = query_results[0][1]

    if predicted_data:
        predicted_data = predicted_data.split(":")
        predicted_months = predicted_data[0]
        predicted_averages = predicted_data[1]

        predicted_months = predicted_months[1:len(predicted_months) - 1].split(",")
        predicted_averages = predicted_averages[1:len(predicted_averages) - 1].split(",")

        predicted_months = list(map(lambda x: int(x), predicted_months))
        predicted_averages = list(map(lambda x: float(x), predicted_averages))
    else:
        predicted_months = []
        predicted_averages = []

    historic_data = (historic_months, historic_averages)
    predicted_data = (predicted_months, predicted_averages)

    return historic_data, predicted_data


def insert_predictions(outcode, start_date, historic, predictions):
    """
    insert record for predicted price of properties in an outcode

    :param outcode: String - an outocode
    :param start_date: String - Month Year
    :param historic: tuple(list(String),list(String)) - historic data
    :param predictions: tuple(list(String),list(String)) - prediction data
    """
    historic_data = str(historic[0]) + ":" + str(historic[1])
    predictions_data = str(predictions[0]) + ":" + str(predictions[1])
    params = (outcode, start_date, historic_data, predictions_data)
    query = "INSERT INTO predictions_data VALUES (%s, %s, %s, %s)"
    general_db_func.insert_to_db(query, params)
