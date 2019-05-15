from back_end.src.database.generic_db_functions import query_database, insert_to_db


def get_ads_near_uni(university, results, distance):
    query = "SELECT postcode FROM uni_addresses_data WHERE establishmentname = '{}';".format(university)
    uni_postcode = query_database(query)[0]

    if uni_postcode:
        distance = distance

        params = dict()
        params["where"] = uni_postcode
        params["distance"] = distance
        params["testing"] = "uni_nearby_ads"

        ids = [r["id"] for r in results]

        params = (university, distance, str(ids))
        query = "INSERT INTO distance_from_uni VALUES (%s, %s, %s)"
        insert_to_db(query, params)
