import csv


def dump_csv(data_matrix, file_path = 'result.csv', format_fun=None):
    '''
    data = [
        ['Name', 'Age', 'Gender'],
        ['Alice', 25, 'Female'],
        ['Bob', 30, 'Male'],
        ['Charlie', 35, 'Male']
    ]
    '''
    with open(file_path, 'w', newline='') as fp:
        writer = csv.writer(fp)
        for data_row in data_matrix:
            if format_fun is None:
                writer.writerow(data_row)
            else:
                writer.writerow([format_fun(data) if isinstance(data, float) else data for data in data_row ])