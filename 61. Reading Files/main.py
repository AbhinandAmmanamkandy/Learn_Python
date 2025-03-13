# Python redaing files (.txt, .json, .csv)

import json
import csv

file_path = "stuffs/output.csv"

try:
    with open(file_path, "r") as file:
        # Normal Text
        content = file.read() # for normal txt file

        # Json file
        # content = json.load(file)
        # print(content["age"]) 

        # CSV file
        # content = csv.reader(file)
        # for line in content:
        #     print(line[2]) # Indexing outputs column
except FileNotFoundError:
    print("File was not found")