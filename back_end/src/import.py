import pandas as pd


class Import:

    def __init__(self):
        self.root_data_path = '../open_datasets/'
        self.box_office_data = self.read_box_office()

    def check_file(self, file_path):
        '''
        Check if a data file exists

        :param file_path: path to the data file starting from root_data_path
        '''
        try:
            open(self.root_data_path + file_path, 'r')
            return True
        except FileNotFoundError:
            return False

    def read_box_office(self):
        '''
        Read in boxofficemojo dataset. Store file as: 'boxoffice.csv'

        :returns the data file
        '''
        file_path = 'boxofficemojo/boxoffice.csv'
        if self.check_file(file_path):
            box_office_data = pd.read_csv(self.root_data_path + file_path)
            return box_office_data
        else:
            print('import for boxofficemojo failed')
            return None

    def get_boxoffice_record(self, record):
        '''
        return a record (column) from the boxoffice datafile

        :param record: string or list(string)
        :return: data record
        '''
        if self.box_office_data is not None:
            try:
                data_record =  self.box_office_data[record]
                return data_record
            except ValueError:
                print('invalid record heading')
                return None


#if __name__ == '__main__':
#    import_data = Import()
