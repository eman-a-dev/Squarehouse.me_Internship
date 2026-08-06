#this project will check if you are eligible for the movie also the ticket price 


print("================================================")
print(          "WELCOME TO MOVIE THEATER"              )
print("================================================")

movies = input("Select the movie you want to watch \n 1. Jumanji \n 2. Spiderman \n 3. Lucy \n 4. Fast and Furious \n write teh selcted number and press enter: ")

if(movies =="1" or movies == "2"):
    age = int(input("Enter your age: "))
    if(age <= 18):
        print("you are eligible for the movie")
        print("your ticket price is Rs. 500")
    else:
        print("ages greater than 18 are also eligible")
        print("your ticket price is Rs. 1500")
elif(movies == "3" or movies == "4"):
    age = int(input("Enter your age: "))
    if(age >= 18):
        print("you are eligible for the movie")
        print("your ticket price is Rs. 1000")
    else:
        print("you are not eligible")
else:
    ("invald choice")
    