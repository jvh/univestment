import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE


class DatabaseHandler:
    def __init__(self):
        self.create_tables()

    def create_pricing_table(self):
        """
        Schema for the house pricing data

        :return: string representing table field commands
        """
        house_price_data = \
            'CREATE TABLE IF NOT EXISTS house_price_data (' \
            '   id INTEGER PRIMARY KEY,' \
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
        yield house_price_data

    def create_admissions_table(self):
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
        yield admissions_data

    def create_uni_addresses_table(self):
        """
        Schema for the university address data

        :return: string representing table field commands
        """
        uni_addresses_data = \
            'CREATE TABLE IF NOT EXISTS uni_addresses_table (' \
            '   id INTEGER PRIMARY KEY,' \
            '   establishment_name TEXT NOT NULL,' \
            '   street TEXT,' \
            '   Town TEXT,' \
            '   postcode TEXT NOT NULL' \
            ');'
        yield uni_addresses_data

    def create_tables(self):
        """
        Create tables for all data sets if they do not already exist
        """
        try:
            connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                          password=POSTGRES_PASSWORD,
                                          database=POSTGRES_DATABASE)

            cursor = connection.cursor()

            for table_command in self.create_pricing_table():
                cursor.execute(table_command)
            for table_command in self.create_admissions_table():
                cursor.execute(table_command)
            for table_command in self.create_uni_addresses_table():
                cursor.execute(table_command)

            connection.commit()
            connection.close()
            cursor.close()
        except (Exception, psycopg2.Error) as error :
            print ("Error connecting to postgres: ", error)


if __name__ == "__main__":
    db = DatabaseHandler()
