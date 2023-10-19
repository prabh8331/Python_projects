"""This is a question bank"""

question_data_old = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

####  trivia database -->  https://opentdb.com/    --> API ---> update the API parameters (select type = True/false)--> 
#### Generate the api url -->copy anp and paste on new tab --> copy that data and paste here . 

### following is the data in JSON format i.e. java script object notation 

question_data = {
    "response_code": 0,
    "results": [
        {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Peter Molyneux was the founder of Bullfrog Productions.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "Science & Nature",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The sum of all the numbers on a roulette wheel is 666.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "History",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The United States Department of Homeland Security was formed in response to the September 11th attacks.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "History",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Adolf Hitler was a german soldier in World War I.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "Entertainment: Board Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "&quot;PAYDAY: The Heist&quot; is a sequel to the board game &quot;Payday&quot;.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "History",
            "type": "boolean",
            "difficulty": "hard",
            "question": "The USS Missouri (BB-63) last served in the Korean War.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "Animals",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Finnish Lapphund dogs were used for herding reindeer.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        }
    ]
}


# print(question_data["results"][0]["question"])
# print(question_data["results"][0]["correct_answer"])