from back_end.src.api_usage.adzuna_ingest import Adzuna
from back_end.src.database import database_functions as db_func
from back_end.src import format_results


def get_rental_properties(postcode):
    """
    Get rental properties from database or Adzuna

    :param postcode: postcode to search in
    """
    adzuna = Adzuna()
    distance = "0.1"

    # Search parameters
    params = dict()
    params["where"] = postcode[:-3]
    params["category"] = "to-rent"
    params["distance"] = distance

    # Rarameters for calculating hash
    hash_params = dict()
    hash_params["where"] = params["where"]
    hash_params["category"] = params["category"]
    hash_params["distance"] = params["distance"]

    print("Attempting to get queries for rental properties from database")
    query_id = format_results.hash_params(hash_params)
    results = db_func.query_already_processed(query_id)

    if not results:
        print("Unseen query. Querying Adzuna for rental properties")
        results = adzuna.get_property_listing(params, 50)

    # Replace price_per_month with sale_price for compatibility with table schema
    for r in results:
        if "price_per_month" in r:
            r["sale_price"] = r.pop("price_per_month")

    large_images = format_results.large_images_only(results)

    # Add results to database if new
    db_func.populate_seen_tables(results, large_images, query_id, params)

    return results


def calculate_average_rent_by_bed(postcode):
    """
    Calculate average rent price for properties within outcode of property

    :param postcode: postcode to search in
    :return: dict of average rent price by beds
    """
    max_beds = 7

    # Keep track of a running total for rent prices by bed
    total_rents = {bed: 0 for bed in range(1, max_beds)}
    # Keep track of the number of properties by bed
    counts = {bed: 0 for bed in range(1, max_beds)}

    # Get rental property listings
    results = get_rental_properties(postcode)

    # Get running total and counts over results
    for r in results:
        if "beds" in r and r["beds"]:
            beds = r["beds"]
            if "price_per_month" in r:
                total_rents[int(beds)] += r["price_per_month"]
                counts[beds] += 1
            elif "sale_price" in r and r["sale_price"]:
                total_rents[int(beds)] += r["sale_price"]
                counts[beds] += 1

    # Calculate average rents by bed
    for key in total_rents.keys():
        if counts[key] != 0:
            total_rents[key] /= counts[key]
    average_rents = total_rents

    return average_rents


if __name__ == "__main__":
    a = calculate_average_rent_by_bed("DA51ER")
    print(a)
