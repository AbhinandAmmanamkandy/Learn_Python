# Two unpacking operator - **
# **kwargs type is a dict (dictionary)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    street="123 Fake Street", 
    apt="100",
    city="Detroit", 
    state="MI", 
    zip="54321"
)