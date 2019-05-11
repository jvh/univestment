###############################################
# File: constants.py                          #
# Description: Holds constant values          #
###############################################

import os

# The root directory is set to be this particular file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Postgres parameters
POSTGRES_SUPER = 'postgres'
POSTGRES_SUPER_PASSWORD = 'WUdVu%mM*#4RQ3R'
POSTGRES_PASSWORD = 'r$B4wnH*HSB#v2W'
POSTGRES_USERNAME = 'comp6214_team'
POSTGRES_PORT = "5432"
POSTGRES_IP = "127.0.0.1"
POSTGRES_DATABASE = 'housing_data'
# Adzuna API id and ket
ADZUNAAPIKEY = "eedd7f406e1a43d0f25bddb4facfbf63"
ADZUNAAPIID = "d1b12649"
# Set to be True when development is occurring (False for production)
DEVELOPMENT = True
