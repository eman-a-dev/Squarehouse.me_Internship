# Write a Python program that checks password strength.
# • Ask user to enter a password
# • Apply these rules:
#   → If length < 6: "Weak — too short"
#   → If length >= 6 and < 10: "Medium — acceptable"
#   → If length >= 10: "Strong"
# • Additionally check:
#   → If password contains "@" or "#": print "Special character found ✓"
#   → Else: print "No special character — consider adding one"
# • Print the password length as well

password = input("Enter the password: ")

#additional checks
if "@" in password or "#" in password:
    print("special characters found")
else:
    print("No special character consider adding one")

if (len(password) < 6):
    print("passowrd is too short/weak")
elif(len(password) >= 6 and len(password) < 10):
    print("password is medium/acceptable")
elif(len(password) >= 10):
    print("password is strong")

print("your valid password: ", password)
print("your password length is: ", len(password))
