import zipfile
from tests.conftest import joined_path
import os


def test_zip_func():
    list_resources = os.listdir(joined_path)
    current_zip_file = os.path.join(joined_path, 'new_hello.zip')
    with zipfile.ZipFile(current_zip_file, 'w') as one_zip:
        for file in list_resources:
            path_to_file = os.path.join(joined_path, file)
            one_zip.write(path_to_file, arcname=file)
        list_zip_arch = one_zip.namelist()

        assert list_zip_arch == list_resources

        os.remove(os.path.join(joined_path, 'new_hello.zip'))
