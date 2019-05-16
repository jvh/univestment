"""
This covers the admission predictions
"""
from datetime import datetime
from statsmodels.tsa.ar_model import AR
import pandas as pd

from back_end.src.database import generic_db_functions as general_db_func


def generate_admission_year_points(future=False):
    """
    Generates the x axis (the years)

    :param future: True when you want to generate years for future dates (predicted)
    :return: list of years spanned by the data
    """
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


def generate_admission_prediction():
    """
    forcast next year's admission statistics for universities
    """
    query = "SELECT * FROM admissions_data"
    result = general_db_func.query_database(query)
    admission_data = pd.DataFrame(result)
    admission_data.rename(columns={0: "year", 1: "university", 2: "admissions"}, inplace=True)
    admission_data = admission_data.sort_values(by=["university", "year"], ascending=True)
    admission_data = admission_data.groupby("university")
    admission_data = [admission_data.get_group(x) for x in admission_data.groups]

    for uni in admission_data:
        uni_name = list(uni["university"])[0]
        uni = uni.drop(columns=["university"])
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


def insert_predicted_admission(university, historic, predictions):
    """
    Insert historic and predicted admission data into database

    :param university: name of university
    :param historic: historic admission data
    :param predictions: predicted admission data
    """
    historic_data = str(historic[0]) + ":" + str(historic[1])
    if predictions:
        predictions_data = str(predictions[0]) + ":" + str(predictions[1])
    else:
        predictions_data = None
    params = (university, historic_data, predictions_data)
    query = "INSERT INTO predicted_admissions_table VALUES (%s, %s, %s)"
    general_db_func.insert_to_db(query, params)
