# Quiz Game
# Create a multiple-choice quiz.Store questions and answers in a dictionary
# Use loops to ask every question
# Track score and incorrect answers
# Use a set to keep categories or answered-question IDs
# Show result and grade at the end


print("=====================================")
print("           QUIZ GAME                 ")
print("=====================================")

quiz_questions = {
    "q1": {
        "question":"1. sets elements are enclosed in",
        "A": "square brackets",
        "B": "curly brackets",
        "C": "round brackets",
        "D": "None",
        "answer": "B"
    },
    "q2": {
            "question":"2. Dictionaries are used to store",
            "A": "key and value pairs",
            "B": "numbers only",
            "C": "strings only",
            "D": "sets",
            "answer": "A"
        },
        "q3": {
                "question":"3. dict.items method is used to ",
                "A": "return all keys in a dictionary",
                "B": "return all values in a dictionary",
                "C": "return the dictionary as tuple",
                "D": "All of the Above",
                "answer": "C"
            }
}

q1_correct_answer = quiz_questions["q1"]["answer"]
q2_correct_answer = quiz_questions["q2"]["answer"]
q3_correct_answer = quiz_questions["q3"]["answer"]
score = 0
incorrect_opt_count = 0

for i in quiz_questions:
    print(quiz_questions[i]["question"])
    print("A", quiz_questions[i]["A"])
    print("B", quiz_questions[i]["B"])
    print("C", quiz_questions[i]["C"])
    print("D", quiz_questions[i]["D"])

    selected_opt = input(
        "Type only the correct option as A,B,C,D: "
    )

    correct_answer = quiz_questions[i]["answer"]

    if selected_opt == correct_answer:
        print("correct answer")
        score += 1
    else:
        print("wrong answer")
        incorrect_opt_count += 1

print("==========================")
print("        RESULTS           ")
print("==========================")
print("your score is: ", score)
print("incorrect option count", incorrect_opt_count)

if(score == 3):
    print("your grade is A")
elif(score == 2):
    print("Your grade is B+")
elif(score == 1):
    print("your grade is B")
else:
    print("All incorrect Better luck next time")

        


