class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        print("Q", self.question_number, ")", end=" ")
        print(current_question.question, "True/False", end=" ")
        ans = input().lower()

        if self.check_answer(ans, correct_answer):
            self.score += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, ans, corr_ans):
        if ans.lower() == corr_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is: {corr_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")