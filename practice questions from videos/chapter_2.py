# String examples

name = "sana"
full_name = "Sana Hashmi"

print("Concatenation:", "Hello" + " " + "World")
print("Indexing:", name[0], name[-1])
print("Slicing:", full_name[0:4])
print("Capitalize:", "python programming".capitalize())
print("Replace:", "I love cats".replace("cats", "dogs"))
print("Find:", "Python".find("th"))
print("Count:", "banana".count("a"))

# Conditional statements examples

# Odd or even
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Multiple of 7
if number % 7 == 0:
    print(number, "is a multiple of 7")
else:
    print(number, "is not a multiple of 7")

# Grade calculator
marks = 82
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

# Nested if example
age = 20
citizen = True
if age >= 18:
    print("You are an adult")
    if citizen:
        print("You can vote")
    else:
        print("You are not a citizen")
else:
    print("You are under 18")
