username = input("enter your username: ")

username = username.strip().lower()

if(len(username) < 5):
    print("Username is too short")
elif "@" in username:
    print("username should not contain @")
else:
    print("valid username: ", username)
