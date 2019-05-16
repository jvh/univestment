from back_end.src.api_usage.adzuna_ingest import Adzuna
from back_end.src.database import database_functions as db_func
from back_end.src import format_results


def calculate_average_rent(postcode):
    """
    calculate the average rent for the outcode the postcode belongs to

    :param postcode: postcode of the property
    """
    adzuna = Adzuna()
    distance = "0.1"
    max_beds = 5

    params = dict()
    params["where"] = postcode[:-3]
    params["category"] = "to-rent"

    rental_values = dict()

    hash_params = dict()
    hash_params["where"] = params["where"]
    hash_params["category"] = params["category"]
    
    for beds in range(2, max_beds):
        params["distance"] = distance
        params["beds"] = beds
        hash_params["distance"] = params["distance"]

        query_id = format_results.hash_params(hash_params)
        results = db_func.query_already_processed(query_id)

        if not results:
            results = adzuna.get_property_listing(params)

        large_images = format_results.large_images_only(results)

        total_rent = 0
        count = 0
        for r in results:
            if "price_per_month" in r:
                total_rent += r["price_per_month"]
                count += 1
            elif "sale_price" in r:
                total_rent += r["sale_price"]
                count += 1

        average_rent = total_rent/count
        rental_values[str(beds)] = average_rent

        for r in results:
            if "price_per_month" in r:
                r["sale_price"] = r.pop("price_per_month")
            else:
                r["sale_price"] = 0

        db_func.populate_seen_tables(results, large_images, query_id, params)

    return rental_values


if __name__ == "__main__":
    a = calculate_average_rent("SO140AU")
    print(a)
