#1.TODO: Welcome the user
#2.TODO: Ask user if want easy or Hard level , for easy give 10 turns and for hard give 5 turns 
#3.TODO: choose a number randomly from 1 to 100 
#4.TODO: define a function which will input level, random number and will iterate as per the level, if win return true else false 
import os 
from art import LOGO
import random

##Welcome the user 
os.system('cls')
print(LOGO)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 to 100.")

##choose the level 
if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
    level = 10
else:
    level = 5

##random number b/w 1 to 100
number=random.randint(1,100)

##define the game function 
def game():
    result = False  # this is a local variable 

    for i in range(level):  # using global variable locally 
        print(f"You have {level-i} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess == number: # using global variable locally
            result = True
            return result
        elif guess<number:
            print("Too low.")
        elif guess>number:
            print("Too high.")
        if level-i != 1:
            print("Guess again.")

    return result

## call the game function and compare the values 
if game() == False:
    print("You've run out of guesses, you lose.")
else:
    print(f"You got it! The answer was {number}")