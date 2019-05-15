"""
Imports CSV files to a pandas dataframe for further processing
"""
import pandas as pd

from back_end.src import ROOT_DIR


class ImportFiles:

    def __init__(self):
        path = '{}/../..'.format(ROOT_DIR)
        self.root_data_path = '{}/open_datasets.nosync/'.format(path)
        self.admissions_data = self.read_admissions()
        self.uni_addresses = self.read_uni_addresses()

    def check_file(self, file_path):
        """
        Check if a data file exists

        :param file_path: path to the data file starting from root_data_path
        """
        try:
            open(self.root_data_path + file_path, 'r')
            return True
        except FileNotFoundError:
            return False

    def read_file(self, file_path, chunksize=None, names=None):
        """
        read a file and return a dataframe containing the contents of the file

        :param file_path: path to file from root data path
        :param chunksize: How many records we insert into the database at a time
        :param names: Defining the column names
        :return: dataframe
        """
        if self.check_file(file_path):
            if chunksize:
                data = pd.read_csv(self.root_data_path + file_path, chunksize=chunksize, names=names)
            else:
                data = pd.read_csv(self.root_data_path + file_path)
            return data
        else:
            raise FileNotFoundError('Please check that the filepath exists: {}'.format(file_path))

    def read_admissions(self):
        """
        Read data file containing admission data and return contents in dataframe

        :return: dataframe
        """
        try:
            return self.read_file('admissions/admissions.csv')
        except FileNotFoundError:
            return None

    def read_uni_addresses(self):
        """
        Read data file containing university address data and return contents in dataframe

        :return: dataframe
        """
        try:
            file = self.read_file('university_addresses/university_addresses.csv')
            return file
        except FileNotFoundError:
            return None

    @staticmethod
    def print_dataframe(data):
        """
        Pretty prints a Pandas dataframe

        :param data: The dataframe
        """
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(data)

    def read_property_data(self):
        """
        Read data file containing historic property data and return contents in dataframe
        :return: dataframe
        """
        chunksize = 20000
        names = ["iden", "price", "date_of_transfer", "postcode", "property_type", "is_newly_built", "duration",
                 "primary_addressable_object_name", "secondary_addressable_object_name", "street", "locality",
                 "town_city", "district", "county", "price_paid_transaction_type", "record status"]
        try:
            return self.read_file('price_paid_data/pp-complete.csv', chunksize=chunksize,
                                  names=names)
        except FileNotFoundError:
            return None
