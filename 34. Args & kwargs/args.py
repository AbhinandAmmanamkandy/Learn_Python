# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#           * unpacking operator
#           1. Positional, 2. Default, 3. Keyword, 4. ARBITRARY

#  args - arguments
#  kwargs - keyword arguments

# here args is a tuple

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 5, 6, 7, 8))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr", "Spongebob", "harold","Squarepants")