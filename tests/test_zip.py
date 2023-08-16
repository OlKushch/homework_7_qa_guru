import zipfile
from tests.conftest import joined_path
import os

def zip_func():
    current_zip_file = os.path.join(joined_path, 'new_hello.zip')
    with zipfile.ZipFile(current_zip_file, 'w') as one_zip:
        one_zip.write('Hello_zip.txt')
        print(one_zip.namelist())
        one_zip.extract('Hello_zip.txt')
        text = one_zip.read('Hello_zip.txt').decode('utf-8')
        print(text)

        assert text == 'привет'
