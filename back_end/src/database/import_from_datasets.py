"""
Imports data from pandas dataframes into our database
"""
import pandas as pd
from uuid import uuid4


def fill_admissions_data(engine, import_files):
    """
    Store admissions data in admissions_data table

    :param engine: database engine object
    :param import_files: ImportFiles object
    """
    data = import_files.admissions_data
    data.columns = map(str.lower, data.columns)
    data['id'] = [uuid4() for _ in range(len(data.index))]
    data.to_sql('admissions_data', engine, if_exists="fail", index=False)


def fill_uni_addresses(engine, import_files):
    """
    Store university address data in uni_addresses_data table

    :param engine: database engine object
    :param import_files: ImportFiles object
    """
    from back_end.src.api_usage import geo_locations

    data = import_files.uni_addresses
    data.columns = map(str.lower, data.columns)
    longitude = []
    latitude = []
    data = data[pd.notnull(data['postcode'])]
    for row in data['postcode']:
        long_, lat = geo_locations.get_coords_from_postcode(row)
        longitude.append(long_)
        latitude.append(lat)
    data['longitude'] = longitude
    data['latitude'] = latitude

    data.to_sql('uni_addresses_data', engine, if_exists="replace", index=False)


def fill_house_data(engine, import_files):
    """
    Store university house price data in house_price_data table

    :param engine: database engine object
    :param import_files: ImportFiles object
    """
    print("Importing house price data... Go get a coffee or something")
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
        chunked_data['postcode'] = chunked_data['postcode'].apply(lambda x: x.replace(" ", ""))
        chunked_data['id'] = [uuid4() for _ in range(len(chunked_data.index))]

        chunked_data.to_sql('house_price_data', engine, if_exists="fail", index=False)

        print("chunk interval done: {}".format(count))
        count = count + 1
    print("Finished importing house price data. Yay")
