## Breakdown a Complex problem into a flow chart 
Make Flow charts here: <https://app.diagrams.net/>

<details>
    <summary>Summary of main Learnings:</summary>
    1. First breakdown the complex problem into small tasks <br>
    2. Create a flow chart of problem <br>
    3. Achieve each subtasks and see if logic is working fine    <br>
    4. Once we got all the logic down and everything is working as expected , <br> 
    5. Then only we will add the full functionality. <br>
    6. Once complete functionality is integrated remove the unwanted comments and testing code, <br>
    7. Keep the comment which explains the code.
<details>


### Hangman Game coding

<details>
    <summary>Game Rules:</summary>
    1. The word to guess is represented by a row of dashes representing each letter or number of the word. <br>
    2. Rules may permit or forbid proper nouns, such as names, places, brands, or slang. <br>
    3. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions. <br>
    4. If the suggested letter does not occur in the word, the other player removes (or alternatively, adds) one element of a hanged stick figure as a tally mark. <br>
    5. Generally, the game ends once the word is guessed, or if the stick figure is complete — signifying that all guesses have been used.<br>
    6. The player guessing the word may, at any time, attempt to guess the whole word. <br>
    7. If the word is correct, the game is over and the guesser wins. <br>
    8. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. <br>
    9. On the other hand, if the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses. <br>
    10. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed<br>
</details>

[`Flow Chart Rules`](Flow_chart/Flow_chart_rules.png)

[`First try on Hangman flow chart`](Flow_chart/Hangman_my_first_try.png) : Issue with this is I am trying to show how I will write a code and this makes it more complex, but in flow chart it is better to draw a logic and it is easy to understand, example is below: 

#### Hangman Flow chart 
<img src="Flow_chart/Hangman_Flowchart.png" alt="Hangman flow" width="400" >


#### Breakdown 1 - Picking a Random Words and Checking Answers 

Python Lists Hint: <https://developers.google.com/edu/python/lists#range>

```py
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a letter: ").lower()


print(guess)

for letter in chosen_word:
    if letter == guess:
        print(True)
    else:
        print(False)

```

#### Breakdown 2 - Replacing Blanks with Guesses

```py
#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

word_length= len(chosen_word)

display = []

display = ["_"]*len(chosen_word)

print(display)

# display = []
# for i in range(len(chosen_word)):
#     display.append("_")

# print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for i in range(word_length):
    letter=chosen_word[i]
    if letter == guess:
        display[i]=letter


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

```

#### Breakdown 3 - Checking if the player has won 

```py
#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


while "_" in display:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

display_final = ""

for i in display:
    display_final+=i

if display_final == chosen_word:
    print("You Win!!")

```

#### Breakdown 4 - Keep track of the Player's Lives

```py
#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives=6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives-=1
        print(lives)
        if lives == 0:
            print("You lose.")
            end_of_game=True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

```


#### Breakdown 5 - Improve the User Experience 

Till now we have just got the code functioning , <br>
Now once we got all the logic down and everything is working as expected , <br> 
Then only we will add the full functionality. 

Once complete functionality is integrated remove the unwanted comments and testing code, <br>
Keep the comment which explains the code.

import statement documentation: <https://www.askpython.com/python/python-import-statement>

```py
#Step 5
import os 
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

#Method1
# from hangman_words import word_list
# chosen_word = random.choice(word_list)

#Method2
# import hangman_words
# word_list=hangman_words.word_list
# chosen_word = random.choice(word_list)

#Method3
import hangman_words
chosen_word = random.choice(hangman_words.word_list)


word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#from hangman_art import logo, stages
import hangman_art


print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You have already guessed, {guess}.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that;s not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

```