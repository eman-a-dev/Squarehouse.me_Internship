print("====================================================")
print("            PASSWORD STRENGTH CHECKER")
print("====================================================")

password = input("Please enter your password here: ")


# length at least 8 characters hai?
length_valid = True

if len(password) < 8:
    length_valid = False


# uppercase letter hai?
uppercase_found = False

for i in password:
    if i.isupper():
        uppercase_found = True


# lowercase letter hai?
lowercase_found = False

for i in password:
    if i.islower():
        lowercase_found = True


# number found
number_found = False

for i in password:
    if i.isdigit():
        number_found = True


# special character
special_found = False

for char in password:
    if char in "!@#$%^&*":
        special_found = True


# space found
space_found = False

for i in password:
    if i.isspace():
        space_found = True


# Final Result
if not length_valid:
    print("Your password is Weak")
    print("Missing: Password length should be at least 8")

elif not uppercase_found:
    print("Your password is Weak")
    print("Missing: Password should contain an uppercase letter")

elif not lowercase_found:
    print("Your password is Weak")
    print("Missing: Password should contain a lowercase letter")

elif not number_found:
    print("Your password is Medium")
    print("Missing: Password should contain at least a number")

elif not special_found:
    print("Your password is Strong")
    print("Missing: Password should contain at least one special character")

elif space_found:
    print("Your password is Weak")
    print("Missing: Password should not contain any spaces")

else:
    print("Your password is Very Strong")