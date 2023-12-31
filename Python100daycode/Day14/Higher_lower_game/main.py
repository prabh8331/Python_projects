import random as r
from art import logo, vs
from game_data import data
from os import system

# 1. breakdown the problem
# 2. Make a todo list
# 3. Start with the easiest one
# 4. turn the problem into comments
# 5. Write code --> Run code--> Fix code  and repeat
# 6. Next Task

# Welcome msg import logo & vs from art.py

print(logo)

# make a random variable selection function which will 
# also ensure new name is not repeated but if all the names in variable are covered this function
# then reset and again do the same

record = []
word1 = r.randint(0, len(data) - 1)
record.append(word1)
word2 = r.randint(0, len(data) - 1)

while word2 in record:
    word2 = r.randint(0, len(data) - 1)

record.append(word2)


def word2_selection(word1_input, word2_input):
    if len(data) == len(record):
        record.clear()
        record.append(word1_input)
        word2_input = r.randint(0, len(data) - 1)
        while word1_input == word2_input:
            word2_input = r.randint(0, len(data) - 1)
    else:
        while word2_input in record:
            word2_input = r.randint(0, len(data) - 1)

    return word2_input


# a variable = True which become False when player give wrong input 
continue_game = True
score = 0

# Create a while loop which will run until game is over
while continue_game is True:
    print(f"Compare A: {data[word1]['name']}, a {data[word1]['description']}, from {data[word1]['country']}.")
    print(vs)
    print(f"Against B: {data[word2]['name']}, a {data[word2]['description']}, from {data[word2]['country']}.")
    compare = input("Who has more followers? Type 'A' or 'B': ").lower()

    system('cls')
    print(logo)

    if compare == 'a':
        if data[word1]['follower_count'] > data[word2]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")

    elif compare == 'b':
        if data[word2]['follower_count'] > data[word1]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

    word1 = word2

    word2 = word2_selection(word1, word2)

    record.append(word2)

# TODO b/w word 1 and word 2 there should be vs

# there should be two variables word 1 and word 2, after all the ans word 1 should = word 2   and word 2 be random

# if condition - is player ans is wrong then this condition will get true and variable = False

# FIXME

# NOTE
# BUG
