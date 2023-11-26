# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("Python100daycode/Day30/Error_handeling_NATO_Phonetic_Alphabet/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# word = input("Enter a word: ").upper()

# wrong_input = True

# while wrong_input:
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         word = input("Enter a word: ").upper()
#     else:
#         print(output_list)
#         wrong_input = False


def Nato_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        Nato_phonetic()
    else:
        print(output_list)

Nato_phonetic()