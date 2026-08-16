
#User Profile Generator: Prompt the user for their name and age. If the age is 18 or older, print "Eligible to register"
#and display the length of their name using the len() function 

print("====================================")
print("         VOTE ELIGIBILTY            ")
print("====================================")

name = input("Enter your name: ")
age = int(input ("enter your age: "))

if(age >= 18):
    print("Your are eligible to vote")
    print("your length is: " , len(name))
else:
    print("You are not eligible")
    