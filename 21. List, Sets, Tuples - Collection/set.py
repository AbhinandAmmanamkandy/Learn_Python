# Set - Order can be random but all are unique

fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# print(fruits[0]) - Cannot use indexing as they are unordered

fruits.add("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop() # Remove random element
print(fruits)