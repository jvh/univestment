import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, POSTGRES_PORT, \
    DEVELOPMENT, POSTGRES_SUPER_PASSWORD, POSTGRES_IP
from back_end.src.import_files import ImportFiles
from sqlalchemy import create_engine
import pandas as pd

from uuid import uuid4


class DatabaseHandler:

    def __init__(self, load_data=False):
        if load_data:
            self.database_commands()

    @staticmethod
    def create_pricing_table():
        """
        Schema for the house pricing data

        :return: string representing table field commands
        """
        house_price_data = \
            'CREATE TABLE IF NOT EXISTS house_price_data (' \
            '   id UUID PRIMARY KEY,' \
            '   price INTEGER NOT NULL,' \
            '   date_of_transfer DATE,' \
            '   postcode TEXT NOT NULL,' \
            '   property_type TEXT,' \
            '   street TEXT,' \
            '   town_city TEXT,' \
            '   county TEXT' \
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
            '   id UUID PRIMARY KEY,' \
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
            '   id UUID PRIMARY KEY,' \
            '   establishmentname TEXT NOT NULL,' \
            '   street TEXT,' \
            '   town TEXT,' \
            '   postcode TEXT NOT NULL' \
            ');'
        return uni_addresses_data

    @staticmethod
    def create_tables():
        """
        return SQL statements for creating tables

        :return String
        """
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
                                              password=POSTGRES_SUPER_PASSWORD,
                                              dbname=POSTGRES_DATABASE)
            else:
                connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                              password=POSTGRES_PASSWORD,
                                              dbname=POSTGRES_DATABASE)

            cursor = connection.cursor()

            # Creating tables
            for table_command in DatabaseHandler.create_tables():
                cursor.execute(table_command)

            engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(POSTGRES_USERNAME, POSTGRES_PASSWORD,
                                                                        POSTGRES_IP, POSTGRES_PORT,
                                                                        POSTGRES_DATABASE))

            connection.commit()

            # Populate databases if not already populated
            import_files = ImportFiles()
            DatabaseHandler.fill_uni_addresses(engine, import_files)
            DatabaseHandler.fill_admissions_data(engine, import_files)
            DatabaseHandler.fill_house_data(engine, import_files)

            connection.commit()
            connection.close()
            cursor.close()
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)

    @staticmethod
    def query_database(query):
        """
        Query the housing database and return all results

        :param query: String representing query
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

            cursor.execute(query)

            result = cursor.fetchall()

            connection.close()
            cursor.close()
            return result
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)

    def postcode_query(self):
        pass

    @staticmethod
    def fill_admissions_data(engine, import_files):
        """
        Store admissions data in admissions_data table

        :param engine: database engine object
        :param import_files: ImportFiles object
        """
        data = import_files.admissions_data
        data.columns = map(str.lower, data.columns)
        data['id'] = [uuid4() for _ in range(len(data.index))]
        data.to_sql('admissions_data', engine, if_exists="replace", index=False)

    @staticmethod
    def fill_uni_addresses(engine, import_files):
        """
        Store university address data in uni_addresses_data table

        :param engine: database engine object
        :param import_files: ImportFiles object
        """
        data = import_files.uni_addresses
        data.columns = map(str.lower, data.columns)
        data['id'] = [uuid4() for _ in range(len(data.index))]
        data.to_sql('uni_addresses_data', engine, if_exists="replace", index=False)

    @staticmethod
    def fill_house_data(engine, import_files):
        """
        Store university house price data in house_price_data table

        :param engine: database engine object
        :param import_files: ImportFiles object
        """
        print("importing house price data. Go get a coffee or something")
        count = 1
        data = import_files.read_property_data()

        for chunk in data:
            chunked_data = pd.DataFrame(chunk)
            chunked_data = chunked_data.drop(columns=["iden", "record status", "locality", "district",
                                                      "is_newly_built", "duration",
                                                      "primary_addressable_object_name",
                                                      "secondary_addressable_object_name",
                                                      "price_paid_transaction_type", "record status"])
            chunked_data = chunked_data[pd.notnull(chunked_data['postcode'])]
            chunked_data['postcode'] = chunked_data['postcode'].apply(lambda x: x.replace(" ",""))
            chunked_data['id'] = [uuid4() for _ in range(len(chunked_data.index))]

            chunked_data.to_sql('house_price_data', engine, if_exists="append", index=False)

            print("chunk interval done: {}".format(count))
            count = count + 1
        print("finished importing house price data. yay")


if __name__ == "__main__":
    db = DatabaseHandler(load_data=True)
