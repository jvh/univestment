import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE, POSTGRES_SUPER, POSTGRES_PORT, \
    DEVELOPMENT, POSTGRES_SUPER_PASSWORD, POSTGRES_IP
from back_end.src.import_files import ImportFiles
from sqlalchemy import create_engine

from uuid import uuid4


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
            '   id UUID PRIMARY KEY,' \
            '   price FLOAT NOT NULL,' \
            '   date_of_transfer DATE,' \
            '   postcode TEXT NOT NULL,' \
            '   property_type TEXT,' \
            '   is_newly_built BOOL,' \
            '   duration TEXT,' \
            '   primary_addressable_object_name TEXT,' \
            '   secondary_addressable_object_name TEXT,' \
            '   street TEXT,' \
            '   town_city TEXT,' \
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

            connection.commit()
            connection.close()
            cursor.close()
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)

    @staticmethod
    def fill_admissions_data(engine, import_files):
        data = import_files.admissions_data
        data.columns = map(str.lower, data.columns)
        data['id'] = [uuid4() for _ in range(len(data.index))]

        ImportFiles.print_dataframe(data)

        data.to_sql('admissions_data', engine, if_exists="replace", index=False)

    @staticmethod
    def fill_uni_addresses(engine, import_files):
        data = import_files.uni_addresses
        data.columns = map(str.lower, data.columns)
        data['id'] = [uuid4() for _ in range(len(data.index))]
        data.to_sql('uni_addresses_data', engine, if_exists="replace", index=False)


if __name__ == "__main__":
    db = DatabaseHandler()
