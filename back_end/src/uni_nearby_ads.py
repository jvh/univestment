from back_end.src.database.generic_db_functions import query_database, insert_to_db
import requests


def get_ads_near_uni(university):
    url = "http://localhost:5005/search"

    query = "SELECT postcode FROM uni_addresses_data WHERE establishmentname = '{}';".format(university)
    uni_postcode = query_database(query)[0]

    if uni_postcode:
        distance = 2

        params = dict()
        params["where"] = uni_postcode
        params["distance"] = distance
        params["testing"] = "uni_nearby_ads"

        response = requests.get(url, params=params)
        if response:
            ids = []
            for r in response:
                ids.append(r[id])

            params = (response[university, distance, ids])
            query = "INSERT INTO distance_from_uni_data VALUES (%s, %s, %s)"
            insert_to_db(query, params)


if __name__ == "__main__":
    get_ads_near_uni("University of Southampton")