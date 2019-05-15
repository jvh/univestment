"""
ML model to predict future housing market value
"""
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR


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
