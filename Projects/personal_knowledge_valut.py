# Personal Knowledge Vault
# Apne notes, ideas, links, aur learning resources ko organize karne wali terminal app banao.
# Features:
# - Note add karo: title, content, tags, date
# - Tags ko set mein store karo, taake duplicate tags na hon
# - Notes ko dictionary mein unique ID ke against save karo
# - Search by title, keyword, ya tag

def add_Note():
        title = input("Enter the Title of you note: ")
        content = input("Enter teh content of your note: ")
        tag_input = input("Enter the tags separated by commas: ")
        tags = {tag.strip() for tag in tag_input.split(",")}
        tags = set(tags)
        date = input("Enter the date (format DD-MM-YYYY): ")

        if diary:
            new_id = max(diary.keys()) + 1
        else:
            new_id = 1

        diary[new_id] = {
            "title": title,
            "content": content,
            "tags": tags,
            "date": date
        }

def view_Notes():
     for note_id, note in diary.items():
          print("================================")
          print("Notes ID: ", note_id)
          print("Title: ", note["title"])
          print("Content: ", note["content"])
          print("Tags: ", note["tags"])
          print("Date: ", note["date"])
          print("================================")

def Search():

    keyword = input("Enter the keyword you want to search for: ")

    found = False

    for note_id, note in diary.items():

        if (keyword.lower() in note["title"].lower()
                or keyword.lower() in note["content"].lower()
                or keyword.lower() in note["tags"]):

            print("================================")
            print("Note ID:", note_id)
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Tags:", ", ".join(note["tags"]))
            print("Date:", note["date"])
            print("================================")

            found = True

    if not found:
        print("Sorry, no note found.")

                 
diary = {}

while True:

    print("==============================================")
    print("            PERSONAL KNOWLEDGE VAULT")
    print("==============================================")

    print("""
1. Add Note
2. View Notes
3. Search Notes
4. Search by Tag
5. Tag Summary
6. Archive Note
7. Delete Note
8. Similar Notes
9. Exit
""")

    option = input("Please select one operation: ")

    if option == "1":
        add_Note()

    elif option == "2":
        view_Notes()

    elif option == "3":
        Search()

    elif option == "9":
        print("Goodbye!")
        break
    
