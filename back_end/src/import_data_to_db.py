import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_IP, POSTGRES_PORT
from sqlalchemy import create_engine
from back_end.src.import_files import ImportFiles
import pandas as pd

class DatabaseHandler:

    def __init__(self):
        self.database_commands()

    @staticmethod
    def create_pricing_table():
        """
        Schema for the house pricing data

        :return: string representing table field commands
        """
        house_price_data = \
            'CREATE TABLE IF NOT EXISTS house_price_data (' \
            '   index INTEGER PRIMARY KEY,' \
            '   level_0 TEXT,' \
            '   level_1 TEXT,' \
            '   price FLOAT NOT NULL,' \
            '   date_of_transfer DATE,' \
            '   postcode TEXT NOT NULL,' \
            '   property_type TEXT,' \
            '   is_newly_built BOOL,' \
            '   duration TEXT,' \
            '   primary_addressable_object_name TEXT,' \
            '   secondary_addressable_object_name TEXT,' \
            '   street TEXT,' \
            '   locality TEXT,' \
            '   town_city TEXT,' \
            '   district TEXT,' \
            '   county TEXT,' \
            '   price_paid_transaction_type TEXT' \
            ');'
        return house_price_data

    @staticmethod
    def create_admissions_table():
        """
        Schema for the university admissions data

        :return: string representing table field commands
        """
        admissions_data = \
            'CREATE TABLE IF NOT EXISTS admissions_data (' \
            '   id INTEGER PRIMARY KEY,' \
            '   year INTEGER NOT NULL,' \
            '   university TEXT NOT NULL,' \
            '   admissions INTEGER NOT NULL' \
            ');'
        return admissions_data

    @staticmethod
    def create_uni_addresses_table():
        """
        Schema for the university address data

        :return: string representing table field commands
        """
        uni_addresses_data = \
            'CREATE TABLE IF NOT EXISTS uni_addresses_data (' \
            '   index INTEGER PRIMARY KEY,' \
            '   establishmentname TEXT,' \
            '   street TEXT,' \
            '   town TEXT,' \
            '   postcode TEXT' \
            ');'
        return uni_addresses_data
#'   id uuid DEFAULT uuid_generate_v4 (),' \
    @staticmethod
    def create_tables():
        yield DatabaseHandler.create_pricing_table()
        yield DatabaseHandler.create_admissions_table()
        yield DatabaseHandler.create_uni_addresses_table()

    @staticmethod
    def database_commands():
        """
        Create tables for all data sets if they do not already exist
        """
        try:
            connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                          password=POSTGRES_PASSWORD,
                                          database=POSTGRES_DATABASE)

            cursor = connection.cursor()

            #cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-oosp"')

            for table_command in DatabaseHandler.create_tables():
                cursor.execute(table_command)

            connection.commit()
            connection.close()
            cursor.close()
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)

    @staticmethod
    def fill_uni_addresses():
        engine = create_engine('postgresql://{}:{}@127.0.0.1:{}/{}'.format(POSTGRES_USERNAME, POSTGRES_PASSWORD
                                                                            , POSTGRES_PORT, POSTGRES_DATABASE))
        importf = ImportFiles()
        data = importf.uni_addresses
        data.to_sql('uni_addresses_data', engine, if_exists="replace", index=True)

    @staticmethod
    def fill_property_data():
        engine = create_engine('postgresql://{}:{}@127.0.0.1:{}/{}'.format(POSTGRES_USERNAME, POSTGRES_PASSWORD
                                                                           , POSTGRES_PORT, POSTGRES_DATABASE))
        importf = ImportFiles()
        skiprows = 0
        while True:
            data = importf.read_property_data(skiprows)
            skiprows = skiprows + 500
            for chunk in data:
                record = pd.DataFrame(chunk)
                record.to_sql('house_price_data', engine, if_exists="append", index=True)
            if data.shape(0) < 500:
                break


if __name__ == "__main__":
    db = DatabaseHandler()
    db.fill_uni_addresses()
    db.fill_property_data()
