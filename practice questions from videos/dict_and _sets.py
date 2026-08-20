# # #print numbers from 1 to 100

# number = 1
# while number <= 100:
#     print(number)
#     number += 1

# #print number from 100 to 1 
# number = 100
# while number >= 1:
#     print(number)
#     number -= 1

#print multiplication table of n 

# n = int(input("Enter a number to print its multiplication table: "))
# i = 1
# while i <=10:
#     print(n, "x", i, "=", n*i)
#     i += 1

# #print the elements of the following input list using loop
# #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# #search for a number x in this tuple using a loop
# #(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

input_number = int(input("Enter a number to search in the tuple: "))

i = 0 
while i < len(tup):
    if (input_number == tup[i]):
        print("The number is found in the tuple at index ", i)
        break
    else:
        print("finding")
    i += 1

# # #print the elements of the following input list using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in list:
    print(i)

#search for a number x in this tuple using a loop
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

input = int(input("Enter a number to search in the tuple: "))

for i in tup:
    if (input == tup[i]):
        print("The number is found in the tuple at index ", i)
        break
else:
    print("The number is not found in the tuple")


# Create two sets of student names and find their union, intersection, and difference.

set1 = {"adil", "moiz", "salar", "naveed","Zainab"}
set2 = {"maryam", "javeria", "Areeba", "Zainab","adil"}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Given a list with repeated values, use a set to find the unique values.

number = [1,4,3,6,3,6,8,8,2,5,1,0]
print(set(number))


#Create a dictionary for a student with name, age, and grade; then print each key and value.

student = {
   "name": "Zainab",
   "age": 22,
   "grade": "A"
}
print(student)

#Add a new key-value pair to a dictionary and update an existing value

student = {
   "name": "Zainab",
   "age": 22,
   "grade": "A"
}
student.update({
    "age": 23,
    "grade": "A+"
})
print(student)

#Count how often each character occurs in a word using a dictionary.

# word = input("Enter a word: ")

count={}
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

#Given a dictionary of products and prices, find the most expensive product.

items = {
    "orange": 40,
    "apple": 60,
    "watermelon": 70,
    "peach": 50
}

print(max(items.values()))

#Merge two dictionaries into one.

section1 = {
    "std1": "zainab",
    "std2": "bilal",
    "std3": "nadia"
}
section2 = {
    "std4": "zareen",
    "std5": "ali",
    "std6": "huda"
}

merged = section1 | section2

print(merged)

#Print each character in a user-entered word.

word = input("Enter a word: ")

for char in word:
    print(char)

# Use a while loop to keep asking for a password until the correct one is entered.

correct_password = "sara56"
while True:
    password = input("Enter the password: ")
    if (password == correct_password):
        print("passowrd is correct")
        break

#Find the first number in a list that is divisible by 7, then stop the loop.

list = [3,4,5,8,6,7]

for i in list:
   if (i % 7 == 0):
      print("found the number", i)
      break

#Skip all numbers divisible by 3 from 1 to 30 using continue.
 
for i in range(1, 31):
    if(i % 3 == 0):
        continue
    else:
        print(i)
