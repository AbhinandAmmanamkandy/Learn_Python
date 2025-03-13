# Python file detection

import os

file_path = "stuff/test.txt"
absolute_file_path = "C:\\Users\\abhin\\Python\\59. File Detection\\stuff\\test.txt"

if os.path.exists(absolute_file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(absolute_file_path):
        print("This is a file")
    elif os.path.isdir(absolute_file_path):
        print("That is a directory")

else:
    print("That location doesn't exists")