from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question_data with the question objects
# write a for loop to iterate through the list
# create question object from each entry in question_data
# append each question object into the question_bank

question_bank = []

for question_item in question_data:
    question_bank.append(Question(question_item["text"], question_item["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()
