import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, POSTGRES_PORT, \
    DEVELOPMENT
from back_end.src.import_files import ImportFiles
from sqlalchemy import create_engine, Column

from uuid import uuid4

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
            '   id uuid DEFAULT uuid_generate_v4 (),' \
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
            '   price_paid_transaction_type TEXT,' \
            '   PRIMARY KEY (id)' \
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
            '   id UUID DEFAULT uuid_generate_v4 (),' \
            '   year INTEGER NOT NULL,' \
            '   university TEXT NOT NULL,' \
            '   admissions INTEGER NOT NULL,' \
            '   PRIMARY KEY (id)' \
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
            '   id UUID PRIMARY KEY,' \
            '   establishmentname TEXT NOT NULL,' \
            '   street TEXT,' \
            '   town TEXT,' \
            '   postcode TEXT NOT NULL' \
            ');'
        return uni_addresses_data

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
            if DEVELOPMENT:
                connection = psycopg2.connect(user=POSTGRES_SUPER,
                                              password='password',
                                              dbname=POSTGRES_DATABASE)
            else:
                connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                              password=POSTGRES_PASSWORD,
                                              dbname=POSTGRES_DATABASE)


            cursor = connection.cursor()

            # Downloading extensions
            cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

            # Creating tables
            for table_command in DatabaseHandler.create_tables():
                cursor.execute(table_command)

            #

            connection.commit()
            connection.close()
            cursor.close()
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)

    @staticmethod
    def fill_uni_addresses():
        engine = create_engine('postgresql://{}:{}@127.0.0.1:{}/{}'.format(POSTGRES_USERNAME, POSTGRES_PASSWORD,
                                                                           POSTGRES_PORT, POSTGRES_DATABASE))
        import_files = ImportFiles()
        data = import_files.uni_addresses
        data.columns = map(str.lower, data.columns)
        # data['id'] = uuid4()
        data['id'] = [uuid4() for _ in range(len(data.index))]
        with pd.option_context('display.max_rows', None, 'display.max_columns',
                               None):  # more options can be specified also
            print(data)
        data.to_sql('uni_addresses_data', engine, if_exists="append", index=False)


if __name__ == "__main__":
    db = DatabaseHandler()
    db.fill_uni_addresses()
