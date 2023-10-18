"""create a Question Class which will attribute question text and answer"""


class Question:
    """we are going to model question """
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# new_q=Question("Is this question?","True")
# print(new_q.text)
# print(new_q.answer)
