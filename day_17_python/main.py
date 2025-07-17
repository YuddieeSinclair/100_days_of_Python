#THIS IS MY QUESTION AND ANSWER GAME USING CLASSES
from data import question_data
import question_model
from quiz_brain import QuizBrain

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer



question_bank = []

for element in question_data:
    question = element['text']
    answer = element['answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz, your final score was \n {quiz.score}/{len(quiz.question_list)}")