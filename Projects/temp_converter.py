print("================================")
print("         TEMP CONVERTER         ")
print("================================")

choose = input("Please select between the two below \n 1. Celcius to Fahrenhiet \n 2. Fahrenhiet to Celcius \n write 1 or 2 and press enter: ")

if (choose == "1"):
    celcius = float( input("Please Enter the temperature: "))
    print("-----------------------------------------------------")
    fahrenhiet = celcius * (9/5) + 32 
    print(fahrenhiet)
elif(choose == "2"):
    fahrenhiet = float( input("Please Enter the temperature: "))
    print("-----------------------------------------------------")
    celcius = (fahrenhiet - 32) * (5/9)
    print(celcius)
else:
    print("Invalid terms")