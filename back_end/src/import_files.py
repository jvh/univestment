import pandas as pd
from back_end.src import ROOT_DIR


class ImportFiles:

    def __init__(self):
        path = '{}/../..'.format(ROOT_DIR)
        self.root_data_path = '{}/open_datasets/'.format(path)
        self.admissions_data = self.clean_admissions()
        print(self.admissions_data)

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
        if self.check_file(file_path):
            data = pd.read_csv(self.root_data_path + file_path)
            return data
        else:
            raise FileNotFoundError('Please check that the filepath exists: {}'.format(file_path))

    def read_admissions(self):
        return self.read_file('admissions/admissions.csv')

    def clean_admissions(self):
        data = self.read_admissions()
        return data


    # def read_boxofficemojo(self):
    #     return self.read_file('boxofficemojo/boxoffice.csv')
    #
    # def read_file(self, file_path):
    #     if self.check_file(file_path):
    #         box_office_data = pd.read_csv(self.root_data_path + file_path)
    #         return box_office_data
    #     else:
    #         raise FileNotFoundError('Please check that the filepath exists: {}'.format(file_path))
    #
    # def get_boxoffice_record(self, record):
    #     """
    #     return a record or set of records (column/s) from the boxoffice datafile
    #     available records: rank, title, studio, lifetime_gross, year
    #
    #     :param record: string or list(string)
    #     :return: data record
    #     """
    #     if self.box_office_data is not None:
    #         try:
    #             data_record =  self.box_office_data[record]
    #             return data_record
    #         except ValueError:
    #             print('invalid record heading')
    #            return None


if __name__ == '__main__':
    imp = ImportFiles()
