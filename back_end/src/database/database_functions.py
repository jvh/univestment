"""
Provides basic functionality for interaction with the database
"""

import psycopg2

from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, DEVELOPMENT, \
    POSTGRES_SUPER_PASSWORD
from back_end.src import property_price_predictions as ppp


def insert_to_db(query, params=""):
    """
    Insert into a database

    :param query: String representing query
    :param params: Any additional parameters which are passed (in tuple format)
    """
    try:
        if DEVELOPMENT:
            connection = psycopg2.connect(user=POSTGRES_SUPER,
                                          password=POSTGRES_SUPER_PASSWORD,
                                          dbname=POSTGRES_DATABASE)
        else:
            connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                          password=POSTGRES_PASSWORD,
                                          dbname=POSTGRES_DATABASE)

        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to postgres: ", error)


def query_database(query, params=""):
    """
    Query the housing database and return all results

    :param query: String representing query
    :param params: Any additional parameters which are passed (in tuple format)
    :return: list(Tuple) of returned results
    """
    try:
        if DEVELOPMENT:
            connection = psycopg2.connect(user=POSTGRES_SUPER,
                                          password=POSTGRES_SUPER_PASSWORD,
                                          dbname=POSTGRES_DATABASE)
        else:
            connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                          password=POSTGRES_PASSWORD,
                                          dbname=POSTGRES_DATABASE)

        cursor = connection.cursor()

        if not params:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        result = cursor.fetchall()
        connection.close()
        cursor.close()
        return result
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to postgres: ", error)


def query_by_postcode(postcode):
    """
    Query database for properties by postcode

    :param postcode: String - a postcode
    :return:
    """
    query = "SELECT * FROM house_price_data WHERE postcode = '{}' ORDER BY date_of_transfer;".format(postcode)
    results = query_database(query)
    return results


def query_for_price_data(outcode):
    """
    Query database for predicted admissions by university

    :param outcode: String - an outcode
    :return: query result
    """
    query = "SELECT historical_data, prediction_data FROM predictions_data WHERE outcode = '{}';".format(outcode)
    results = query_database(query)
    return results


def query_admission(university):
    """
    Query database for admissions by university

    :param university: String - name of university
    :return: query result
    """
    query = "SELECT * FROM admissions_data WHERE university = '{}'".format(university)
    results = query_database(query)
    return results


def query_predicted_admission_data(university):
    """
    Query database for predicted admissions by university

    :param university: String - name of university
    :return: query result
    """
    query = "SELECT historic_admissions, predicted_admissions FROM predicted_admissions_table WHERE " \
            "university = '{}'".format(university)
    results = query_database(query)

    return results


def query_by_outcode(outcodes):
    """
    Query database for properties by outcode and insert market value predictions into database

    :param outcodes: A list of outcodes
    """
    for outcode in outcodes:
        query = "SELECT outcode FROM predictions_data WHERE outcode = '{}'".format(outcode)
        result = query_database(query)

        if not result:
            query_results_area = query_database("SELECT * FROM house_price_data WHERE substr(postcode,1,{})"
                                                        " = '{}' ORDER BY date_of_transfer;"
                                                        .format(len(outcode), outcode))

            # returned_house_prices_area = returned_house_prices_area + query_results_area
            if query_results_area:
                start_date, historic_data, predicted_data = ppp.generate_prediction(query_results_area)
                ppp.insert_predictions(outcode, start_date, historic_data, predicted_data)
