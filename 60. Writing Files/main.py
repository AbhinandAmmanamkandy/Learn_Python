# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"
file_path = "output.txt"

with open(file_path, "a") as file:
    file.write("\n" + txt_data)
    print(f"txt file {file_path} was created!")