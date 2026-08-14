print("=============================")
print("       Welcome to ATM        ")
print("=============================")

initial_balance = 50000.00

name = input("Enter your name: ")
acc_num =int(input("Enter your account number: "))

deposit = float(input("How much deposit you want to add: "))
balance_after_deposit = deposit + initial_balance
print("your balance after deposit: ", balance_after_deposit )

withdrawl = float(input("How much money you want to withdrawl: "))
balance_after_withdrawl = balance_after_deposit - withdrawl
print("your balance after withdrawl: ", balance_after_withdrawl)

print(type(initial_balance))
print(type(name))
print(type(acc_num))
print(type(deposit))
print(type(balance_after_deposit))
print(type(withdrawl))
print(type(balance_after_withdrawl))




