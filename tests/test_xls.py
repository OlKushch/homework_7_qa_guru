
import os
import xlrd
from tests.conftest import joined_path
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def book_workbook():
    book = xlrd.open_workbook(os.path.join(joined_path,'file_example_XLS_10.xls'))

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
    list_rx = []
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
        list_rx.append(sheet.row(rx))

    assert book.nsheets == 1
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=3, colx=2) == 'Gent'
    assert book.sheet_names() == ['Sheet1']
    assert len(list_rx) == 10
