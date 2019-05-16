from back_end.src.database import database_functions as db_func
from back_end.src import format_results
from back_end.src import app


def get_rental_properties(outcode):
    """
    Get rental properties from database or Adzuna

    :param outcode: Outcode to search in
    """
    adzuna = app.adzuna
    distance = "0.5"

    # Search parameters
    params = dict()
    params["where"] = outcode
    params["category"] = "to-rent"
    params["distance"] = distance
    params["results_per_page"] = 50

    # Parameters for calculating hash
    hash_params = dict()
    hash_params["where"] = params["where"]
    hash_params["category"] = params["category"]
    hash_params["distance"] = params["distance"]

    query_id = format_results.hash_params(hash_params)
    print("Attempting to get queries for rental properties from database")
    results = db_func.query_already_processed(query_id, outcode_rentals=True)

    if not results:
        print("Unseen query. Querying Adzuna for rental properties")
        results = adzuna.get_property_listing(params, category="to-rent")

        # Replace price_per_month with sale_price for compatibility with table schema
        for r in results:
            if "price_per_month" in r:
                r["sale_price"] = r.pop("price_per_month")

        # Add results to database if new
        print("adding rental results to database")
        db_func.populate_seen_tables(results, [], query_id, hash_params)

    return results


def calculate_average_total_rent_by_bed(outcode):
    """
    Calculate average total rent price for properties within outcode of property

    :param outcode: Outcode to search in
    :return: dict of average rent price by beds
    """
    print("\nBeginning calculation of average rent prices by bed for outcode: {}".format(outcode))
    max_beds = 7

    # Keep track of a running total for rent prices by bed
    total_rents = {bed: 0 for bed in range(1, max_beds)}
    # Keep track of the number of properties by bed
    counts = {bed: 0 for bed in range(1, max_beds)}

    # Get rental property listings
    results = get_rental_properties(outcode)

    # Get running total and counts over results
    print("calculating average rent prices by bed")
    for r in results:
        if "beds" in r and r["beds"] in counts:
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
    print("finished calculating average rent by bed for outcode: {}\n".format(outcode))
    return average_rents

