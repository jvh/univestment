from back_end.src.api_usage.adzuna_ingest import Adzuna
from back_end.src.database import generic_db_functions as general_db_func

def get_ads_near_uni(university):
    query = "SELECT postcode FROM uni_addresses_data WHERE establishmentname = '{}';".format(university)
    uni_postcode = general_db_func.query_database(query)[0]
    adzuna = Adzuna()

    if uni_postcode:
        search_params = dict()
        search_params['where'] = uni_postcode
        max_distance = 4

        for distance in range(1, max_distance):
            search_params['distance'] = distance
            results = adzuna.get_property_listing(search_params, results_per_page=10)

            ids = [r["id"] for r in results]

            params = (university, distance, str(ids))
            query = "INSERT INTO distance_from_uni VALUES (%s, %s, %s)"
            general_db_func.insert_to_db(query, params)

