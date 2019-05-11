import pandas as pd
from back_end.src import ROOT_DIR


class ImportFiles:

    def __init__(self):
        path = '{}/../..'.format(ROOT_DIR)
        self.root_data_path = '{}/open_datasets/'.format(path)
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

    def read_file(self, file_path, skiprows=None, chunksize=None, names=None):
        """
        read a file and return a dataframe containing the contents of the file

        :param file_path: path to file from root data path
        :return: dataframe
        """
        if self.check_file(file_path):
            if skiprows is not None and chunksize is not None:
                data = pd.read_csv(self.root_data_path + file_path, skiprows=skiprows, chunksize=chunksize, names=names)
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
            return self.read_file('university_addresses/university_addresses.csv')
        except FileNotFoundError:
            return None

    def read_property_data(self, skiprows):
        """
        Read data file containing historic property data and return contents in dataframe

        :return: dataframe
        """
        chunksize = skiprows + 500
        names = ["price",
               "date_of_transfer",
               "postcode",
               "property_type",
               "is_newly_built",
               "duration",
               "primary_addressable_object_name",
               "secondary_addressable_object_name",
               "street",
               "locality",
               "town_city",
               "district",
               "county",
               "price_paid_transaction_type"]
        try:
            return self.read_file('price_paid_data/pp-complete.csv', skiprows=skiprows, chunksize=chunksize,
                                  names=names)
        except FileNotFoundError:
            return None


# if __name__ == '__main__':
#     imp = ImportFiles()
#     print()
