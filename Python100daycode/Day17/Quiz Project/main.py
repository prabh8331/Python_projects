"""Main Program"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for qn in question_data:
#     question_bank.append(Question(qn["text"], qn["answer"]))

#here we are converting string key "text" into an object 

question_data = question_data["results"]  ## addition to make new format of data work


for qn in question_data:
    # txt = qn["text"]
    # ans = qn["answer"]
    txt = qn["question"]   #addition to make new data work
    ans = qn["correct_answer"]   #addition to make new data work
    new_question = Question(txt,ans)
    question_bank.append(new_question)


quiz=QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")