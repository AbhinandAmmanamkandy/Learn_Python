# Conditional Expression - A one line shortcut for if else statement (ternary operator)
#                           Print or assign one of two values based on condition
#                           X if condition else Y

num = 10
a = 6
b = 7

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num%2==0 else "ODD"
print(result)

max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)

age = 4
status = "Adult" if age>=18 else "Child"
print(status)

temp = 1
weather = "HOT" if temp > 20 else "COLD"
print(weather)

user_role = "guest"
access_level = "FULL ACCESS" if user_role=="admin" else "LIMITED ACCESS"
print(access_level)