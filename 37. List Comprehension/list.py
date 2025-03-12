# List comprehension = A consise way to create lists in python 
#                   Compact and easier to read than traditional loops
#                   [expression for value in iterable if condition]

# This block is way too much
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

doubles = [x*2 for x in range(1, 11)]
triples = [y*3 for y in range(1, 11)]
squares = [z*z for z in range(1, 11)]

print(squares)
