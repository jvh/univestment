"""
Provides basic functionality for interaction with the database
"""
import psycopg2

from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, DEVELOPMENT, \
    POSTGRES_SUPER_PASSWORD


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
