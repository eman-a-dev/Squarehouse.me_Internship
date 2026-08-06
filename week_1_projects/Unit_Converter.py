print("================================")
print("          UNIT CONVERTER        ")
print("================================")

choose = input("Please select from the options below \n - LENGTH \n 1. Meter -> Kilometer \n " 
"2. Kilometer -> Meter \n - WEIGHT \n 3. Kilogram -> Gram \n 4. Gram -> Kilogram \n - TEMPERATURE \n 5. Celsius ->Fahrenheit \n " 
"6. Fahrenheit -> Celsius \n write the seleted number and press enter: ")
print("----------------------------------------------------------------")
# FOR LENGTH
if(choose == "1"):
   kilometer = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   meter = kilometer * 1000
   print(meter)
elif(choose == "2"):
   meter = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   kilometer = meter / 1000
   print(kilometer)
#FOR WEIGHT
elif(choose == "3"):
   kilogram = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   gram = kilogram * 1000
   print(gram)
elif(choose == "4"):
   gram = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   kilogram = gram / 1000
   print(kilogram)
#FOR TEMPERATURE
elif(choose == "5"):
   celcius = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   fahrenhiet = celcius * (9/5) + 32 
   print(fahrenhiet)
elif(choose == "6"):
   fahrenhiet = float(input("Enter the number you want to convert: "))
   print("---------------------------------------------------------")
   celcius = (fahrenhiet - 32) * (9/5)  
   print(fahrenhiet)
else:
   print("invalid choice")
   
   
  


