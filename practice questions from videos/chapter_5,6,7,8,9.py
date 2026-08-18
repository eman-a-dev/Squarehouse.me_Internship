# CHAPTER 5: LOOPS 

# 1. While Loops 
# timer = 1
# while timer <= 5 :
#     print("Timer is at:", timer)
#     timer += 1

# print("timers up!!!")

#for loop
company = "SQUAREHOUSE.ME"

# for i in company:
#     print(i)

#continue and break 

# emotions = ["happy", "sad", "angry", "excited", "bored"]

# for i in emotions:
#     if i == "excited":
#         print("emotion" , i , "found")
#         break
#     else:
#         print("finding emotion")

# emotions = ["happy", "sad", "angry", "excited", "bored"]

# for i in emotions:
#     if i == "excited":
#         print("emotion" , i , "found")
#         continue
#     else:
#         print("finding emotion")

#pass is used for those loops which we create but there is no logic in it so 
#we write pass in it to avoid any error and write the logic in future

#CHAPTER 6 : FUCNTIONS AND RECURSION

#calculate the average of 3 numbers

# def average(num1, num2, num3):
#     sum = num1 + num2 + num3
#     avg = sum /3
#     print("The average of the 3 numbers is: ", avg)
#     return avg

# average(10, 20, 30)



# num = int(input("Enter the Number: "))
# def even_or_odd(num):
#     if (num % 2 == 0):
#         print("The number is even")
#     else:
#         print("The number is odd")
#     return num

# even_or_odd(num)


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

def highest_marks(dict):
    max_marks = max(dict.values())
    print(max_marks)




marks = {
    "std1": 60,
    "std2": 70,
    "std3": 80,
    "std4": 90   
}

highest_marks(marks)

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

