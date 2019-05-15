"""
Specialised interaction with the database (serving specific purposes)
"""
import back_end.src.property_price_predictions_helper
from back_end.src.database import generic_db_functions as general_db_func
from back_end.src import property_price_predictions as ppp
from back_end.src import format_results
from back_end.src import property_price_predictions_helper as ppp_helper


def query_by_postcode(postcode):
    """
    Query database for properties by postcode

    :param postcode: String - a postcode
    :return:
    """
    query = "SELECT * FROM house_price_data WHERE postcode = '{}' ORDER BY date_of_transfer;".format(postcode)
    results = general_db_func.query_database(query)
    return results


def query_for_price_data(outcode):
    """
    Query database for predicted admissions by university

    :param outcode: String - an outcode
    :return: query result
    """
    query = "SELECT historical_data, prediction_data FROM predictions_data WHERE outcode = '{}';".format(outcode)
    results = general_db_func.query_database(query)
    return results


def query_admission(university):
    """
    Query database for admissions by university

    :param university: String - name of university
    :return: query result
    """
    query = "SELECT * FROM admissions_data WHERE university = '{}'".format(university)
    results = general_db_func.query_database(query)
    return results


def query_predicted_admission_data(university):
    """
    Query database for predicted admissions by university

    :param university: String - name of university
    :return: query result
    """
    query = "SELECT historic_admissions, predicted_admissions FROM predicted_admissions_table WHERE " \
            "university = '{}'".format(university)
    results = general_db_func.query_database(query)

    return results


def query_by_outcode(outcodes):
    """
    Query database for properties by outcode and insert market value predictions into database

    :param outcodes: A list of outcodes
    """
    for outcode in outcodes:
        query = "SELECT outcode FROM predictions_data WHERE outcode = '{}'".format(outcode)
        result = general_db_func.query_database(query)

        if not result:
            query_results_area = general_db_func.query_database("SELECT * FROM house_price_data "
                                                                "WHERE substr(postcode,1,{}) = '{}' "
                                                                "ORDER BY date_of_transfer;"
                                                                .format(len(outcode), outcode))

            # returned_house_prices_area = returned_house_prices_area + query_results_area
            if query_results_area:
                start_date, historic_data, predicted_data = ppp.generate_prediction(query_results_area)
                back_end.src.property_price_predictions_helper.insert_predictions(outcode, start_date, historic_data,
                                                                                  predicted_data)


def query_already_processed(query_id):
    """
    If a query has already been processed, get its results

    :param query_id: ID of the query
    :return: If it has been processed, return list of results
    """
    query = "SELECT properties FROM seen_queries WHERE id={}".format(query_id)
    if_processed = general_db_func.query_database(query)

    # If the query has been processed beforehand
    if if_processed:
        [[unpacked]] = list(if_processed)
        # Get IDs of those advertisements part of this query
        results = unpacked.split(' ')

        results_from_db_lrg = []
        for r in results:
            query = "SELECT * FROM seen_adverts WHERE id={}".format(r)
            [db_res] = general_db_func.query_database(query)

            record = dict()
            record['has_large_img'] = db_res[14]
            # Don't include
            if not record['has_large_img']:
                continue
            record['id'] = db_res[0]
            record['beds'] = db_res[1]
            record['description'] = db_res[2]
            record['image_url'] = db_res[3]
            record['is_furnished'] = db_res[4]
            record['latitude'] = db_res[5]
            record['longitude'] = db_res[6]
            record['postcode'] = db_res[7]
            record['property_type'] = db_res[8]
            record['redirect_url'] = db_res[9]
            record['sale_price'] = db_res[10]
            record['title'] = db_res[11]
            record['university'] = db_res[12]
            record['date_of_insertion'] = db_res[13]

            results_from_db_lrg.append(record)

        return results_from_db_lrg


def populate_seen_tables(results, large_images, query_id, params):
    """
    When a new query is ran, populate the seen tables (seen_queries and seen_adverts) with their corresponding data.

    :param results: The resulting advertisements given by a query
    :param large_images: The list of results which have large images
    :param query_id: The UUID of the query
    :param params: Params given by the user for the query
    """
    # The list of property IDs in the results (of the advertisements)
    property_id_list = []

    # Adding advertisements to seen_adverts table
    for r in results:
        property_id_list.append(r['id'])
        args = (r['id'],)

        # Identify if the property advertisement has already been seen by the table
        seen_property_listing = "SELECT id FROM seen_adverts WHERE id=%s;"
        seen_before = general_db_func.query_database(seen_property_listing, args)

        # If it has been seen, update date
        if seen_before:
            search_property_query = "UPDATE seen_adverts SET date_of_insertion=DEFAULT WHERE id=%s;"
            general_db_func.insert_to_db(search_property_query, args)
        else:
            # Add it to the table
            add_property_query = "INSERT INTO seen_adverts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                 "%s, %s, %s, DEFAULT, %s);"
            args = format_results.get_property_args(r, large_images)
            general_db_func.insert_to_db(add_property_query, args)

    # Add it to the table seen_queries
    add_query = "INSERT INTO seen_queries VALUES (%s, %s, %s, DEFAULT);"
    args = (query_id, str(params), ' '.join(str(e) for e in property_id_list))
    general_db_func.insert_to_db(add_query, args)


def query_predicted_admissions(university):
    """
    query predicted_admissions_table for one university's
    prediction data

    :param university: String - name of university
    :return: dict
    """
    result = query_predicted_admission_data(university)
    if result:
        historic_data, predicted_data = ppp_helper.parse_prediction_data_from_db(result)
        return_data = {"historic": {"x": historic_data[0], "y": historic_data[1]},
                       "predicted": {"x": predicted_data[0], "y": predicted_data[1]}}
        return return_data
    else:
        return None
