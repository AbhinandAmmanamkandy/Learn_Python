# Dictionary = a collection of {key:value} pairs
#               orderes and changeable. No duplicates

capitals = {
    "USA" : "Washington D.C",
    "India" : "New Delhi",
    "China" : "Beijing",
    "Russia" : "Moscow"
}

# Get value
# print(capitals.get("Japan"))

# Check value exists
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# Update - change or insert
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})

# Remove
# capitals.pop("China")
# capitals.popitem() # remove latest key value pair inserted
# capitals.clear()

# Get all keys
# keys = capitals.keys()

# Get all values
# values = capitals.values()

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")