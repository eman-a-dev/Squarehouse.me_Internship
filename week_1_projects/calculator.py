print ("----------------Hello-----------------")

num1 = int(input("Enter the first number: "))
print("----------------------------------------")
num2 = int(input("Enter the seconf number: "))
print("----------------------------------------")
operator = input("Enter the operator '+,-,*,/ : ")
print("----------------------------------------")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Error")