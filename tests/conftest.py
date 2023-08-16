import os
# current_directory = os.path.dirname(os.path.abspath('docs-pytest-org-en-latest.pdf'))
#
# print(current_directory)

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
joined_path = os.path.join(current_directory, 'resources')
print(joined_path)
print(current_file_path)
print(current_directory)