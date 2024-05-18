from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_test = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_test, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quizongoing = True

while quizongoing:
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your Final score was: {quiz.score}/{quiz.question_number}")
