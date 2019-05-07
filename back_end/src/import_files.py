import pandas as pd


class ImportFiles:

    def __init__(self):
        self.root_data_path = '../open_datasets/'
        self.box_office_data = self.read_boxofficemojo()

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

    def read_boxofficemojo(self):
        return self.read_file('boxofficemojo/boxoffice.csv')

    def read_file(self, file_path):
        if self.check_file(file_path):
            box_office_data = pd.read_csv(self.root_data_path + file_path)
            return box_office_data
        else:
            print('import for boxofficemojo failed')
            return None

    def get_boxoffice_record(self, record):
        """
        return a record or set of records (column/s) from the boxoffice datafile
        available records: rank, title, studio, lifetime_gross, year

        :param record: string or list(string)
        :return: data record
        """
        if self.box_office_data is not None:
            try:
                data_record =  self.box_office_data[record]
                return data_record
            except ValueError:
                print('invalid record heading')
                return None


#if __name__ == '__main__':
#    import_data = Import()
