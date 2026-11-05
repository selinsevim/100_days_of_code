# TODO Asking the question
# TODO Checking if the answer was correct
# TODO Checking if we are at the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        """
        Retrieves at the current question_number from the question list
        Use the input() function to show the user Question text and ask for the user answer
        """
        current_question_item = self.question_list[self.question_number]
        current_text = current_question_item.text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_text} (True/False)")
        correct_answer = current_question_item.answer
        self.check_answer(user_answer, correct_answer)
        return user_answer

    def check_answer(self, user_answer_item, correct_answer_item):
        """
        Check if the user answer is the correct answer
        If yes, give them a +1 score
        """
        if user_answer_item == correct_answer_item:
            self.score += 1
            print("You are correct.")
            print(f"Your score is {self.score}")

    def still_has_questions(self):
        """
        Return a boolean depending on the value of question_number.
        Use the while loop to show the next question until the end
        """
        if self.question_number == len(self.question_list):
            return False
        else:
            print("Current question number is", self.question_number)
            return True
