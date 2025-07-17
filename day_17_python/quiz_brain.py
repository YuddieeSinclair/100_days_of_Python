class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_input)

    def check_answer(self, current_answer, user_input):
        if  user_input.lower() == current_answer.lower():
            self.score += 1
            print("you are correct")
        else:
             print("that is incorrect")
        print(f"the correct answer is {current_answer}")
        print(f"Your score is {self.score}/{self.question_number}")