"""
Creates tables for the database
"""


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


def create_prediction_table():
    """
    Schema for predictions_data (out codes only)

    :return: string representing table field commands
    """
    predictions_data = \
        'CREATE TABLE IF NOT EXISTS predictions_data (' \
        '   outcode TEXT PRIMARY KEY, ' \
        '   start_date DATE NOT NULL,' \
        '   historical_data TEXT NOT NULL,' \
        '   prediction_data TEXT NOT NULL' \
        ');'
    return predictions_data


def create_property_table():
    """
    Schema for seen_adverts

    :return: string representing table field commands
    """
    seen_adverts = \
        'CREATE TABLE IF NOT EXISTS seen_adverts (' \
        '   id INTEGER PRIMARY KEY, ' \
        '   beds INTEGER,' \
        '   description TEXT,' \
        '   image_url TEXT,' \
        '   is_furnished BOOLEAN,' \
        '   latitude FLOAT,' \
        '   longitude FLOAT,' \
        '   postcode TEXT,' \
        '   property_type TEXT,' \
        '   redirect_url TEXT,' \
        '   sale_price FLOAT,' \
        '   title TEXT,' \
        '   university TEXT,' \
        '   date_of_insertion DATE NOT NULL DEFAULT NOW(),' \
        '   has_large_img BOOLEAN NOT NULL' \
        ');'
    return seen_adverts


def create_seen_queries():
    """
    Schema for seen_queries

    :return: string representing table field commands
    """
    seen_queries = \
        'CREATE TABLE IF NOT EXISTS seen_queries (' \
        '   id UUID PRIMARY KEY, ' \
        '   query TEXT NOT NULL,' \
        '   properties TEXT,' \
        '   date_of_insertion DATE NOT NULL DEFAULT NOW()' \
        ');'
    return seen_queries


def create_admissions_table():
    """
    Schema for the university admissions data

    :return: string representing table field commands
    """

    admissions_data = \
        'CREATE TABLE IF NOT EXISTS admissions_data (' \
        '   year INTEGER NOT NULL,' \
        '   university TEXT PRIMARY KEY,' \
        '   admissions INTEGER NOT NULL' \
        ');'
    return admissions_data


def create_uni_addresses_table():
    """
    Schema for the university address data

    :return: string representing table field commands
    """
    uni_addresses_data = \
        'CREATE TABLE IF NOT EXISTS uni_addresses_data (' \
        '   establishmentname TEXT PRIMARY KEY,' \
        '   street TEXT,' \
        '   town TEXT,' \
        '   postcode TEXT NOT NULL,' \
        '   longitude FLOAT NOT NULL,' \
        '   latitude FLOAT NOT NULL' \
        ');'
    return uni_addresses_data


def create_img_thumbnail():
    """
    Schema for img_thumbnail_to_lrg

    :return: string representing table field commands
    """
    img_thumbnail_to_lrg = \
        'CREATE TABLE IF NOT EXISTS img_thumbnail_to_lrg (' \
        '   id UUID PRIMARY KEY,' \
        '   thumbnail_url TEXT NOT NULL,' \
        '   lrg_url TEXT' \
        ');'
    return img_thumbnail_to_lrg


def create_predicted_admissions_table():
    predicted_admissions_data = \
        'CREATE TABLE IF NOT EXISTS predicted_admissions_table (' \
        '   university TEXT PRIMARY KEY,' \
        '   historic_admissions TEXT NOT NULL,' \
        '   predicted_admissions TEXT NOT NULL' \
        ');'
    return predicted_admissions_data


def create_distance_from_uni_table():
    """
    Schema for distance_from_uni_data

    :return: string representing table field commands
    """
    distance_from_uni_data = \
        'CREATE TABLE IF NOT EXISTS distance_from_uni (' \
        '   university_name TEXT PRIMARY KEY,' \
        '   distance_from INTEGER,' \
        '   property_id_list TEXT' \
        ');'
    return distance_from_uni_data


def create_tables():
    """
    return SQL statements for creating tables

    :return String
    """
    yield create_pricing_table()
    yield create_admissions_table()
    yield create_uni_addresses_table()
    yield create_img_thumbnail()
    yield create_prediction_table()
    yield create_predicted_admissions_table()
    yield create_property_table()
    yield create_seen_queries()
    yield create_distance_from_uni_table()
