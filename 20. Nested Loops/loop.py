# Nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner_loop:

# Print defaults new line as end

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()