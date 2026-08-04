#WAP to ask the user to enter names of their 3 favourite movies and store them in a list 

# input_movies = input("enter the names of your 3 favourite movies separated by commas: " )
# movies = [input_movies]
# print (movies)
# print (type(movies))


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