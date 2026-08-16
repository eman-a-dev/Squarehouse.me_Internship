# Contact Book
# Build a dictionary-based phonebook.Add a contact: name, phone number, email
# Search by name
# Update or delete a contact
# Display all contacts using loops


print("==================================")
print("          CONTACT BOOK            ")
print("==================================")

contacts = {

    "zainab" :  {
        "name": "zainab",
        "contact": "00897437",
        "email": "zainab@cgmail.com"
    },
    "sadi" : {
            "name": "sadi",
            "contact": "379279823",
            "email": "sadi@cgmail.com"
        },
    "bilal" :  {
            "name": "bilal",
            "contact": "027362892",
            "email": "bilal@cgmail.com"
        }
}

searched_contact = input("Enter the contact name: ")

for i in contacts:
    if (searched_contact == i):
        print(contacts[i]["name"])
        print(contacts[i]["contact"])
        print(contacts[i]["email"], "\n")

contacts.update({
    "zainab": {
        "email": "zainab02@gmail.com"
    },
    "adil": {
        "name": "adil",
        "contact": "08462622",
        "email": "adil@cgmail.com"
    }
})

print("updated Contacts\n", contacts,"\n")

del contacts["sadi"]
print( "Contact after deleteion \n", contacts)

