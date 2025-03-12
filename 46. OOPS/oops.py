# Object - A "Bundle" of related attributes (variables) and methods (functions)
#       Ex: phone, cup, book
#       You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

car1.describe()