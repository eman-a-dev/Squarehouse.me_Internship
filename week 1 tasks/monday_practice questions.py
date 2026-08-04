#Write a Python program to print your name using a string variable.
name = "Eman Arif"
print("My name is:", name)

#Create two strings and join them using +.
a = "Beutiful"
b = "Lady"

print("Concatenated string:", a + " " + b)

#Print the first and last character of a string.

name = " Eman Arif"
print("First character:", name[0])
print("Last character:", name[-1])

#Use slicing to print the first 3 characters of a word.

word = "playground"
print("First 3 characters:", word[0:3])

#Write code to count how many times the letter "a" appears in a word.

word = "banana"
count_a = word.count("a")   

#Write a program that takes two strings as input and prints them together with a space in between.

name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Full name:", name + " " + last_name)

#Write a program that takes a number as input and prints whether it is positive, negative, or zero.

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")    
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    

             