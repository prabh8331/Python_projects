print("Welcome to Rock Paper Scissors!!!")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_instruments= [rock,paper,scissors]

human_choice = int(input("What do you choose? TYpe 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

if human_choice >=3 or human_choice <0:
    print("Invalid input You lost")
else: 
    print(game_instruments[human_choice])
    print(f"Computer chose: {computer_choice}")
    print(game_instruments[computer_choice])

    if computer_choice == human_choice :
        print("Game Draw")
    elif human_choice == 2 and computer_choice == 0:
        print("You Lost")
    elif human_choice == 0 and computer_choice == 2:
        print("You Win")
    elif human_choice > computer_choice:
        print("You Win")
    elif computer_choice > human_choice:
        print("You Lost")


## not so good

#if computer_choice == 0:
#    if human_choice == 1:
#        print("You Win")
#    elif human_choice == 2:
#        print("You Lost")
#    else: 
#        print("Game Draw")
#elif computer_choice == 1:
#    if human_choice == 2:
#        print("You Win")
#    elif human_choice == 0:
#        print("You Lost")
#    else: 
#        print("Game Draw")
#elif computer_choice == 2:
#    if human_choice == 0:
#        print("You Win")
#    elif human_choice == 1:
#        print("You Lost")
#    else: 
#        print("Game Draw")
