#Dictionary and sets 

# Creating a dictionary
company = {
    "name": "getsky",
    "no_of_employees": 100,
    "Managers": ["Asghar", "Ali", "Saad"],
    "CEO": "Samad Laghari"
}

print (company)


#Sets 
subjects1 = {"English", "Maths", "Science", "Urdu", "Sindhi"}
subjects2 = {"English", "Maths", "Science", "Urdu", "Sindhi", "Islamiyat"}

print (subjects1.intersection(subjects2))

#notice : sets are immutable and unordered, so the order of elements may vary when printed
#also sets are mutable but the ekements inside the set are immutable
#cannot add lists and dictionaries inside a set because they are mutable