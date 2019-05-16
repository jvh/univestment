from back_end.src.api_usage.adzuna_ingest import Adzuna
from back_end.src.database import database_functions as db_func


def calculate_average_rent(postcode):
    """
    calculate the average rent for the outcode the postcode belongs to

    :param postcode: postcode of the property
    """
    adzuna = Adzuna()
    params = dict()
    params["where"] = postcode[:-3]
    params["distance"] = 0.1
    max_beds = 5
    rental_values = dict()

    for beds in range(2, max_beds):
        params["beds"] = beds
        results = adzuna.get_property_listing(params, ad_type="to-rent")
        db_func.populate_seen_tables(results, large_images, query_id, preprocessing_params)

        total_rent = 0
        count = 0

        for r in results:
            if "price_per_month" in r:
                total_rent += r["price_per_month"]
                count += 1
        average_rent = total_rent/count
        rental_values[str(beds)] = average_rent
    return rental_values


if __name__ == "__main__":
    a = calculate_average_rent("SO140AU")
    print(a)