# Validate user input execise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contains digits

user_name = input("Enter username: ")

if len(user_name) > 12:
    print("Username must be less than 12 characters")
elif not user_name.find(" ") == -1:
    print("Username cannot contains spaces")
elif not user_name.isalpha():
    print("Username cannot contain digits")
else:
    print(f"Welcome {user_name}")