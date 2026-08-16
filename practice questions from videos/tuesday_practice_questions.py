#WAP to ask the user to enter names of their 3 favourite movies and store them in a list 

input_movies = input("enter the names of your 3 favourite movies separated by commas: " )
movies = [input_movies]
print (movies)
print (type(movies))


#WAP to check if a list contains a palindrome of elements. 

#one working case
alphabets =[1, 2, 1]

copy_alphabets = alphabets.copy()
print (copy_alphabets)
reverse_alphabets = list(reversed(copy_alphabets))
print (reverse_alphabets)
if copy_alphabets ==  reverse_alphabets:
    print ("The list contains a palindrome of elements")
else:
    print ("The list does not contain a palindrome of elements")

#one non-working case
alphabets =[1, 2, 3]

copy_alphabets = alphabets.copy()
print (copy_alphabets)
reverse_alphabets = list(reversed(copy_alphabets))
print (reverse_alphabets)
if copy_alphabets ==  reverse_alphabets:
    print ("The list contains a palindrome of elements")
else:
    print ("The list does not contain a palindrome of elements")


#WAP to count the number of students with the "A" grade in the following tuple
#["C", "D", "A", "A", "B", "B", "A"]

grades = ("C", "D", "A", "A", "B", "B", "A")
print ("The number of students with the 'A' grade is: ", grades.count("A"))

#store the above values in lista nd sort them Ato D

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print ("The sorted grades are: ", grade)


#yahan dictionary wale solved hain!!

#WAP to enter marks of 3 subjects from the user and store them in a dictionary start with an empty dictionary and add one by one user subject names as key and marks as value 

marks = {}
subject1 = input("Enter the name of subject 1: ")
marks[subject1] = int(input("Enter the marks of subject 1: "))
subject2 = input("Enter the name of subject 2: ")
marks[subject2] = int(input("Enter the marks of subject 2: "))
subject3 = input("Enter the name of subject 3: ")
marks[subject3] = int(input("Enter the marks of subject 3: "))
print (marks)


#figureout a way to store 9 and 9.0 as separate values in a set use builtin datatype for this 
numbers = {"round_number": (9, 9.0)}
print (numbers)