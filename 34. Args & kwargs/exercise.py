# Function contains tuple and dictionary args

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label(
    "Dr.",
    "SpongeBob",
    "SquarePants",
    "III",
    street="123 Fake Street",
    pobox="PO box 100",
    city="Detroit",
    state="MI",
    zip="54321"
)