# Compund Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle: "))
    if principle < 0:
        print("Principle cannot be less than zero")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than zero")
    else:
        break

while True:
    time = float(input("Enter time in years: "))
    if time < 0:
        print("Time cannot be less than to zero")
    else:
        break


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")