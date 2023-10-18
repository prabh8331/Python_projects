"""Main Program"""

from question_model import Question
from data import question_data

question_bank = []

# for qn in question_data:
#     question_bank.append(Question(qn["text"], qn["answer"]))

#here we are converting string key "text" into an object 

for qn in question_data:
    txt = qn["text"]
    ans = qn["answer"]
    new_question = Question(txt,ans)
    question_bank.append(new_question)
