unit = input("Celcius or Fahrenheit: ")
temp = float(input("Enter temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Farenheit: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")