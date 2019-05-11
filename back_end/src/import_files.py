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

    def read_file(self, file_path):
        """
        read a file and return a dataframe containing the contents of the file

        :param file_path: path to file from root data path
        :return: dataframe
        """
        if self.check_file(file_path):
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


# if __name__ == '__main__':
#     imp = ImportFiles()
#     print()
