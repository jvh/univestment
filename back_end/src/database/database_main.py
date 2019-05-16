"""
Connects to postgres, creating and populating tables where applicable
"""
from sqlalchemy import create_engine

from back_end.src.database.csv_to_dataframe import ImportFiles
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, POSTGRES_PORT, \
    DEVELOPMENT, POSTGRES_SUPER_PASSWORD, POSTGRES_IP
import psycopg2
from back_end.src.database import import_from_datasets as ifd
from back_end.src.preprocess_data import preprocess_admission_predictions as pap
from back_end.src.database import create_tables as ct


def database_commands(load_data=False, manual_import=False):
    """
    Create tables for all data sets if they do not already exist

    :param load_data: True if data should be loaded automatically from CSV
    :param manual_import: True if data should be loaded manually from CSV
    """
    try:
        if DEVELOPMENT:
            connection = psycopg2.connect(user=POSTGRES_SUPER,
                                          password=POSTGRES_SUPER_PASSWORD,
                                          dbname=POSTGRES_DATABASE)
        else:
            connection = psycopg2.connect(user=POSTGRES_SUPER,
                                          password=POSTGRES_SUPER_PASSWORD,
                                          dbname=POSTGRES_DATABASE)
            # connection = psycopg2.connect(user=POSTGRES_USERNAME,
            #                               password=POSTGRES_PASSWORD,
            #                               dbname=POSTGRES_DATABASE)

        cursor = connection.cursor()

        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(POSTGRES_USERNAME, POSTGRES_PASSWORD,
                                                                    POSTGRES_IP, POSTGRES_PORT,
                                                                    POSTGRES_DATABASE))

        # Creating tables
        for table_command in ct.create_tables():
            cursor.execute(table_command)

        connection.commit()

        # Manually populate table from CSV
        if manual_import:
            import_files = ImportFiles()
            data = import_files.read_file(absolute_path='insert_abs_path')


        # If you need to load the data into the database
        if load_data:
            # Populate databases if not already populated
            import_files = ImportFiles()
            ifd.fill_uni_addresses(engine, import_files)
            ifd.fill_admissions_data(engine, import_files)
            ifd.fill_house_data(engine, import_files)
            pap.generate_admission_prediction()

        connection.commit()
        connection.close()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to postgres: ", error)


if __name__ == "__main__":
    database_commands()
