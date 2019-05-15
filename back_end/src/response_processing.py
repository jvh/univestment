import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR
from back_end.src.database import database_functions as db_func
from datetime import datetime


def generate_admission_prediction():
    """
    forcast next year's admission statistics for universities
    """
    query = "SELECT * FROM admissions_data"
    result = db_func.query_database(query)
    admission_data = pd.DataFrame(result)
    admission_data.rename(columns={0: "year", 1: "university", 2:"admissions",3:"id"}, inplace=True)
    admission_data = admission_data.sort_values(by=["university","year"], ascending=True)
    admission_data = admission_data.groupby("university")
    admission_data = [admission_data.get_group(x) for x in admission_data.groups]

    for uni in admission_data:
        uni_name = list(uni["university"])[0]
        uni = uni.drop(columns=["university", "id"])
        uni.set_index(uni.year, inplace=True)

        historic_points = generate_admission_year_points()
        historic_admissions = fill_none_admissions(uni["admissions"].tolist())

        historic_data = (historic_points, historic_admissions)

        try:
            # Generate autoregressive model
            model = AR(uni["admissions"])
            model_fit = model.fit()

            # predict next 2 years
            prediction_points = generate_admission_year_points(future=True)
            predicted_admissions = model_fit.predict(len(uni["year"]), len(uni["year"])+1).to_list()
            predicted_data = (prediction_points, predicted_admissions)
            insert_predicted_admission(uni_name, historic_data, predicted_data)
        except ValueError as e:
            print(e)


def generate_prediction(data):
    """
    Create and train a autoregressive model and predict property prices for the next 24 months

    :param data:
    :return: list(int) of points, list(int) of prices
    """
    pricing_data = pd.DataFrame(data)
    pricing_data = pricing_data.drop(columns=[0, 3, 4, 5, 6, 7])
    pricing_data.rename(columns={1: "price", 2: "date"}, inplace=True)
    pricing_data.date = pd.to_datetime(pricing_data.date, infer_datetime_format=True)

    # Remove outliers (more than 3 s.d. from mean)
    pricing_data = pricing_data[np.abs(pricing_data.price - pricing_data.price.mean())
                                <= (3 * pricing_data.price.std())]
    pricing_data.set_index(pricing_data.date, inplace=True)
    pricing_data = pricing_data.groupby(pd.Grouper(freq='M')).mean().dropna()

    # Generate autoregressive model
    model = AR(pricing_data["price"])
    model_fit = model.fit()

    # predict next 24 months
    predictions = model_fit.predict(len(pricing_data["price"]), len(pricing_data["price"]) + 23)

    start_date = pricing_data.index.to_series().tolist()[0]

    historic_points = pricing_data.index.to_series().apply(lambda x: pd.datetime.strftime(x, '%m:%Y'))\
        .tolist()
    historic_points = generate_date_points(historic_points)
    predicted_points = [i+len(historic_points)+1 for i in range(24)]

    historic_prices = pricing_data["price"].tolist()
    predicted_prices = predictions.tolist()

    historic_data = (historic_points, historic_prices)
    predicted_data = (predicted_points, predicted_prices)

    return start_date, historic_data, predicted_data


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
    db_func.insert_to_db(query, params)


def insert_predicted_admission(university, historic, predictions):
    historic_data = str(historic[0]) + ":" + str(historic[1])
    if predictions:
        predictions_data = str(predictions[0]) + ":" + str(predictions[1])
    else:
        predictions_data = None
    params = (university, historic_data, predictions_data)
    query = "INSERT INTO predicted_admissions_table VALUES (%s, %s, %s)"
    db_func.insert_to_db(query, params)


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


def generate_admission_year_points(future=False):
    if future:
        start_year = datetime.now().year
        target_year = start_year + 2
        points = [year for year in range(start_year, target_year)]
    else:
        start_year = 2006
        current_year = datetime.now().year
        points = [year for year in range(start_year, current_year)]
    return points


def fill_none_admissions(admissions):
    number_of_admissions = len(admissions)
    current_year = datetime.now().year
    missing_data = [0 for _ in range(2006, current_year-number_of_admissions)]
    full_data = missing_data + admissions
    return full_data
