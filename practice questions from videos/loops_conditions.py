
# Write a Python program to check whether a number is even or odd.
x = 3
remainder = x % 2
if(remainder == 0):
    print("the number is even")
else:
    print("the number is odd")


# Write a Python program to check whether a given number is prime or not.
number = int(input("please Enter the number: "))

if number <= 1:        #checks ifthe number is 1 or less than 1 so that it doesn't go through the logic and tells the user taht the number si not prime 
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(number ** 0.5) + 1): #this is because we only have to check prime number til the squareroot of a number 
        if number % i == 0: #check the remainder if the remainder is 0 teh prime becomes false 
            prime = False   # and the loop breaks and prints not prime from the below logic
            break

    if prime:               #if the rwmainder is not zero then prime  is true and prints Prime
        print("The number is Prime")
    else:
        print("The Number is Not Prime")

# Write a Python function to calculate the factorial of a number.
num = int(input("Please Enter the Number: "))

fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("The factorial of ", num, "is ", fact)

# Write a Python program to reverse a string without using built-in reverse functions.
str = "Squarehouse"

print(str[::-1])

# Write a Python program to count the number of vowels in a string.
string = input("Please enter the text: ").lower()

count = 0

for ch in string:
    if ch in "aeiou":
        count += 1

print("The number of vowels is:", count)

# Write a Python program to find the largest element in a list without using max().
list = [23, 1, 5, 34, 0, 3, 56]

sorted_list = list.sort

print(list[-1])

# Write a Python program to remove duplicate elements from a list.
numbers = [23, 1, 1, 0, 5, 34, 0, 3, 2, 56, 2]

numbers.sort()

i = 0
j = 1

while j < len(numbers):

    if numbers[i] == numbers[j]:
        numbers.pop(j)
    else:
        i += 1
        j += 1

print(numbers)  

# Write a Python program to generate the Fibonacci sequence up to n terms.
term = int(input("Enter the Term: "))

a=0
b=1
for i in range(term):
    print(a, end=" ")

    c = a + b
    a=b
    b=c

# Write a Python program to check whether a string is a palindrome.
text = input("Enter the word: ")

reverse_str = text[::-1]

if(text == reverse_str):
    print("Teh string is a Palindrome")
else:
    print("The string is not a Palindrome")

# Write a Python program that takes a student's marks as input and prints the grade using if-elif-else
marks = int(input("Enter your marks: "))
if (marks >=80):
    print("Your grade is A+")
elif(marks >=70):
    print("your grade is A")
elif(marks >= 56):
    print("your grade is B")
else:
    print("sorry better luck next time")