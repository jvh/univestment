###############################################
# File: constants.py                          #
# Description: Holds constant values          #
###############################################

import os

# The root directory is set to be this particular file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Zoopla's API key
ZOOPLAAPIKEY = "x3augy4g7kxxm3m3tcanc5xd"
POSTGRES_PASSWORD = 'r$B4wnH*HSB#v2W'
POSTGRES_USERNAME = 'comp6214_team'
POSTGRES_PORT = "5432"
POSTGRES_IP = "127.0.0.1"
POSTGRES_DATABASE = 'housing_data'
# Set to be True when development is occurring (False for preduction)
DEVELOPMENT = True
