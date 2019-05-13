import uuid
from back_end.src.database.database_main import DatabaseHandler


def get_property_args(p):
    params = (p['id'], p['beds'], p['description'], p['image_url'], p['is_furnished'], p['latitude'], p['longitude'],
              p['postcode'], p['property_type'], p['redirect_url'], p['sale_price'], p['title'], 'x', True)
    return params


if __name__ == '__main__':
    r = {
        "__CLASS__": "Adzuna::API::Response::Property",
        "adref": "eyJhbGciOiJIUzI1NiJ9.eyJpIjoxMTEwODU0Nzc1LCJzIjoiczdhUGt3a0dUcWF1M0tQbkRxSUpqQSJ9.n-gh4ivOsFhnOyKyTLd8d0z5xF83IPAqql-vG5dax_E",
        "beds": 2,
        "category": {
            "__CLASS__": "Adzuna::API::Response::Category",
            "label": "For Sale",
            "tag": "for-sale"
        },
        "created": "2019-03-24T11:57:32Z",
        "description": "A MUCH IMPROVED & EXTREMELY WELL MAINTAINED PARK HOME, WITH DIRECT VIEWS TO THE REAR OVER SURROUNDING COUNTRYSIDE: Gas central heating (mains gas), UPVC double glazing, refitted kitchen and refitted shower room, parking space alongside and additional visitors parking",
        "id": 1110854775,
        "image_url": "https://imganuncios.mitula.net/medium/2_bedroom_park_home_for_sale_3690036544105370517.jpg",
        "is_furnished": "0",
        "latitude": 50.781898,
        "location": {
            "__CLASS__": "Adzuna::API::Response::Location",
            "area": [
                "UK",
                "South East England",
                "Hampshire",
                "Lymington",
                "Pilley"
            ],
            "display_name": "Pilley, Lymington"
        },
        "longitude": -1.53677,
        "postcode": "SO415QJ",
        "property_type": "house",
        "redirect_url": "https://property.adzuna.co.uk/land/ad/1110854775?se=s7aPkwkGTqau3KPnDqIJjA&utm_medium=api&utm_source=d1b12649&v=6320493AF733426822804849A1DB61DE2650D730",
        "sale_price": 179950,
        "title": "2 bed house for sale in Fleur De Lys Park",
        "university": "University of Winchester"
    }

    params = 'results_per_page=10&where=SO173RZ&category=for-sale&search_student_lets=true&radius_from=20&km_away_from_uni=2'
    query_id = uuid.uuid3(uuid.NAMESPACE_DNS, str(params))

    args = (r['id'],)

    # Identify if the property advertisement has already been seen by the table
    seen_property_listing = "SELECT id FROM seen_adverts WHERE id=%s;"
    seen_before = DatabaseHandler.query_database(seen_property_listing, args)

    # If it has been seen, update date
    if seen_before:
        search_property_query = "UPDATE seen_adverts SET date_of_insertion=DEFAULT WHERE id=%s;"
        DatabaseHandler.insert_to_db(search_property_query, args)
    else:
        # Add it to the table
        add_property_query = "INSERT INTO seen_adverts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                             "%s, %s, %s, DEFAULT, %s);"
        args = get_property_args(r)
        DatabaseHandler.insert_to_db(add_property_query, args)