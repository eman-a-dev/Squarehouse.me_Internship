# #print numbers from 1 to 100

# number = 1
# while number <= 100:
#     print(number)
#     number += 1

# #print number from 100 to 1 
# number = 100
# while number >= 1:
#     print(number)
#     number -= 1

# #print multiplication table of n 

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

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# input_number = int(input("Enter a number to search in the tuple: "))

# i = 0 
# while i < len(tup):
#     if (input_number == tup[i]):
#         print("The number is found in the tuple at index ", i)
#         break
#     else:
#         print("finding")
#     i += 1

# #print the elements of the following input list using loop
# #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in list:
#     print(i)

# #search for a number x in this tuple using a loop
# #(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

input = int(input("Enter a number to search in the tuple: "))

for i in tup:
    if (input == tup[i]):
        print("The number is found in the tuple at index ", i)
        break
else:
    print("The number is not found in the tuple")