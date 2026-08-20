#functions

# #WAP to print length of a list is the parameter of a function

# def length_of_list(list):
#     print(len(list))
#     return list

# length_of_list([1,2,3,4,5,6,7,8,10])

# #WAP to print the elements of a list in a single line (list is the parameter)

# def elements(list):
#     for i in list:
#         print(i , end=" ")
#     return list

# elements(["apple", "banana", "orange", "kiwi"])

# #WAP to find the factorial of n (n is a parameter)

# def factorial(n):
#     factorial =1
#     for i in range(1, n+1):
#         factorial = factorial * i
#     print(factorial)
#     return factorial

# factorial(4)

# #WAP to convert USD to PKR 

# def USD_to_PKR_coverter():
#     PKR = 278
#     USD = int(input("Enter the amount you want to convert: "))
#     total_amount = USD * PKR
#     print(total_amount)

# USD_to_PKR_coverter()

#Write a function that takes two numbers and returns the larger one.

# def largest_num(num1, num2):
#     if(num1 > num2):
#         print(num1, "is greater than", num2)
#     else:
#         print(num2, "is greater than", num1)

# largest_num(3,6)

#Create a function that calculates the area of a rectangle using length and width.

# def area_rectangle(length, width):
#     area = length * width
#     print(area)


# area_rectangle(23,56)

#Create a function that accepts a list of numbers and returns their sum, average, maximum, and minimum.

# def maths_methods(list):
#     Sum = sum(list)
#     average = Sum / len(list)
#     print("Sum =", Sum)
#     print("Average =", average)
#     print("Maximum Value =",max(list))
#     print("Minimim Value =", min(list))
    

# number = [23, 67,4,8,34,90]
# maths_methods(number)


#Write a function that accepts a dictionary of student marks and returns the student with the highest mark.

# def highest_marks(dict):
#     max_marks = max(dict.values())
#     print(max_marks)

# marks = {
#     "std1": 60,
#     "std2": 70,
#     "std3": 80,
#     "std4": 90   
# }

# highest_marks(marks)

#Write a function that counts vowels in a string.

# def vowel_counter():
#     count = 0
#     string = input("Enter the sentence: ").lower()

#     for ch in string:
#         if ch in 'aeiou':
#             count += 1

#     print("The number of vowels are: ", count)

# vowel_counter()

#Write a function that checks whether a word is a palindrome.

# def palindrome():
#     words = input("Enter the word: ")
#     copy_words = words
#     print("The word Before reverse: ", copy_words)
#     reverse_words = words[::-1]
#     print("the string after reverse: ", reverse_words)
#     if (copy_words == reverse_words):
#         print("The string is a palindrome")
#     else:
#         print("The string is not a palindrome")

# palindrome()

#Create a function find_duplicates(items) that returns duplicate elements from a list using a set.

def find_duplicates(items):
    seen = set()
    duplicates = set()

    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


num = [1, 4, 8, 5, 6, 8, 6, 4, 2, 7, 8]

print(find_duplicates(num))

#Recursive functions

#calculate the sum of first natural number

# def sum_of_num(n):
#     if(n == 0):
#         return 0
#     return sum_of_num(n-1) + n



# print(sum_of_num(5))

#write a recursive functions to print all the elements of a list
# def elements(list, idx=0):
#     if(idx == len(list)):
#         return 
#     print(list[idx])
#     elements(list, idx + 1)

# veg = ["onion", "potato", "ladyfinger"]

# elements(veg)

