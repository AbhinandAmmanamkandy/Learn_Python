# Format Specifiers = {value: flags} format a value based on what 
#                   flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many space
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive values
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma seperator

price1 = 30000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1: {price1:+,.2f}")
print(f"Price 2: {price2:+,.2f}")
print(f"Price 3: {price3:+,.2f}")