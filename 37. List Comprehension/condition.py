numbers = [1, -2, 3, -4, 5, -6]

positive = [num for num in numbers if num>=0]
negative = [num for num in numbers if num<0]

even = [num for num in numbers if num%2==0]
odd = [num for num in numbers if num%2==1]

print(even)
print(odd)