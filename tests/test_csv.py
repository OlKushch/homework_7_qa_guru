import csv
import os
from tests.conftest import joined_path
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_write_csv():
    with open(os.path.join(joined_path, 'new_csv.csv'), 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(joined_path, 'new_csv.csv')) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        csv_list = []
        for row in csvreader:
            print(row)
            csv_list.append(row)
            print(csv_list)

        assert csv_list[0] == ['Bonny', 'Born', 'Peter']
        assert csv_list[1] == ['Alex', 'Serj', 'Yana']
