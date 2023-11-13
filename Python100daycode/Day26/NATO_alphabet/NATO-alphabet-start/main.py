#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_data = pandas.read_csv("Python100daycode/Day26/NATO_alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

word = input("Enter the word to get the NATO code: ")
# print(word)

nato_list = [nato_dict[char.upper()]  for char in word]
print(nato_list)