# Word Frequency Counter
# Ask the user for a sentence or paragraph.Split it into words
# Use a dictionary to count each word
# Use a set to show unique words
# Find the most frequently used word


print("=============================================")
print("           WORD FREQUENCY COUNTER            ")
print("=============================================")

sentence = input("Enter the Sentence: ")

splited_sentence = sentence.split()

dictionary = {}

for i in splited_sentence:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)

print(set(dictionary))

most_used = max(dictionary, key=dictionary.get)

print("This is your most frequently used word:", most_used)