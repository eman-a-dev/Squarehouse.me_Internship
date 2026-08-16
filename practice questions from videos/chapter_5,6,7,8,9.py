# CHAPTER 5: LOOPS 

# 1. While Loops 
timer = 1
while timer <= 5 :
    print("Timer is at:", timer)
    timer += 1

print("timers up!!!")

#for loop
company = "SQUAREHOUSE.ME"

for i in company:
    print(i)

#continue and break 

emotions = ["happy", "sad", "angry", "excited", "bored"]

for i in emotions:
    if i == "excited":
        print("emotion" , i , "found")
        break
    else:
        print("finding emotion")

emotions = ["happy", "sad", "angry", "excited", "bored"]

for i in emotions:
    if i == "excited":
        print("emotion" , i , "found")
        continue
    else:
        print("finding emotion")

#pass is used for those loops which we create but there is no logic in it so 
#we write pass in it to avoid any error and write the logic in future

#CHAPTER 6 : FUCNTIONS AND RECURSION

#calculate the average of 3 numbers

def average(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum /3
    print("The average of the 3 numbers is: ", avg)
    return avg

average(10, 20, 30)






