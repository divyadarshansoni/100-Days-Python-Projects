from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)


print("Hello There!")
initial = input("Do you want to play the quiz game: (Yes/No):").lower()
if initial == "yes":
    print("All the best")
    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()
    print("The quiz is completed.")
    print(f"Your final score is: {quiz.score}/{len(question_bank)}")
    print("Congratulations!")
