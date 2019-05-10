import psycopg2
from back_end.src import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_IP, POSTGRES_PORT, POSTGRES_DATABASE

def create_tables():
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

try:
    connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                  password=POSTGRES_PASSWORD,
                                  host=POSTGRES_IP,
                                  port=POSTGRES_PORT,
                                  database=POSTGRES_DATABASE)
    cursor = connection.cursor()

    for table_command in create_tables():
        cursor.execute(table_command)

except (Exception, psycopg2.Error) as error :
    print ("Error connecting to postgres: ", error)

