# exception = An event that interrupts the flow of a program 
#           (ZeroDivitionError, TypeError, ValueError)
#           1. try, 2. except, 3. finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
finally:
    print("Do some clean up here!")