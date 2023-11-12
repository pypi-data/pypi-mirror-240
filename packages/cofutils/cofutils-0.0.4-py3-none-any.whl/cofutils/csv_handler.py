import csv
class Cofcsv:
    def __init__(self) -> None:
        pass

    @staticmethod
    def save(data, path='result.csv'):
        '''
        data = [
            ['Name', 'Age', 'Gender'],
            ['Alice', 25, 'Female'],
            ['Bob', 30, 'Male'],
            ['Charlie', 35, 'Male']
        ]
        '''
        with open(path, 'w', newline='') as fp:
            writer = csv.writer(fp)
            for data_row in data:
                writer.writerow(data_row)

    @staticmethod
    def load(path='result.csv'):
        with open(path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            data = [row for row in csvreader]
        return data


cofcsv = Cofcsv()