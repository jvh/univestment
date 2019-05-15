


def get_ads_near_uni(university):
    query = "SELECT postcode FROM uni-addresses-data WHERE establishmentname = '{}';".format(university)
