print("======================================")
print("      RESTAURANT BILL SPLITTER        ")
print("======================================")

total_bill = int(input("Enter your total bill: "))
no_of_people = int(input("Enter number of people you want to divide the bill with: "))

splited_bill = total_bill / no_of_people 
print("-------------------------------")
print("The bill per person is: ", "Rs.", splited_bill)