# Keyword arguments = an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positional, 2. Default, 3. KEYWORD, 4. arbitrary

# Function key is provided with arguments
# Positional Arguments are provided first
# Here "Hello" is positional, rest is keyword

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", last="SquarePants", first="SpongeBob")
hello("Hello", title="Mr.", last="John", first="James")