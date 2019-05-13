from back_end.src.database.import_files import ImportFiles
from sqlalchemy import create_engine
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, POSTGRES_PORT, \
    DEVELOPMENT, POSTGRES_SUPER_PASSWORD, POSTGRES_IP
import psycopg2
from back_end.src.database.import_data_to_db import DatabaseHandler


def database_commands(load_data=False):
    """
    Create tables for all data sets if they do not already exist
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
        for table_command in DatabaseHandler.create_tables():
            cursor.execute(table_command)

        connection.commit()

        # If you need to load the data into the database
        if load_data:
            # Populate databases if not already populated
            import_files = ImportFiles()
            DatabaseHandler.fill_uni_addresses(engine, import_files)
            DatabaseHandler.fill_admissions_data(engine, import_files)
            DatabaseHandler.fill_house_data(engine, import_files)

        connection.commit()
        connection.close()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to postgres: ", error)


if __name__ == "__main__":
    database_commands()
