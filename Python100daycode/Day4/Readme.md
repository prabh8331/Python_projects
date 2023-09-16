## Randomisation and Python Lists 

```md
Python use **Mersenne Twister** pseudorandom rumber generator, we will use random module to genertae random numbers 
```

```md
In Python, a **module** is a file containing Python code that can include functions, classes,
and variables. Modules are used to organize and encapsulate related pieces of code into 
reusable units. They help in keeping code clean, maintainable, and logically structured. 
```


### Create your own module 
`a_module.py:`
```py 
pi = pi = 3.14159246
```

`main.py:`
``` py 
import a_module

print(a_module.pi)
```


`main.py` is usually the entry point, it could be different (`__init__.py`) <br> 
but enty point is a file which will be executed when we run our code


### Random Module
Documentation = <https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences>

`main.py:`
``` py 

import random 

random_interger = random.randint(1,10)  #this will generate random interg b/w 1 and 10
print(random_interger)

random_float = random.random()   # this will generate random flaod b/w 0 and 1 but will not inclured 1 will be like 0.9999999 etc. 
print(random_float)

# Random b/w 0 and 5
random_float5=random_float*5
print(random_float5)

# example roll a dice  
dice_roll = random.randint(1,6)
print(f"you got {dice_roll}")

```

### Heads or Tails 
```py
import random
coin = random.randint(0,1)

if coin == 0: 
    print("Tails")
elif coin == 1:
    print("Heads")
```


## Python Lists 
documentation  = <https://docs.python.org/3/tutorial/datastructures.html>

It is a datastructure in pyton which can store 

`syntex:`
```py
fruits = ["Cherry" ,"Apple" ,"Pair","Pineapple"]
print(fruits)

print(fruits[0] )#Cherry 
print(fruits[-1] )#Pineapple
print(fruits[1] )# Apple 

fruits[2] = "Pear"
print(fruits)

fruits.append("Grapes")
print(fruits)

fruits.extend(["Watermelon","Strawberry","Banana"])
print(fruits)

total_fruits = len(fruits) 

print(fruits[total_fruits-1]) #Banana
#print(fruits[total_fruits]) #IndexError: list index out of range

# Nested list
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits,vegrtables]

print(dirty_dozen)

print(dirty_dozen[1][1])
```

if our data has a order or relation lists also have a order with it 
list count start from 0 , then 1,2,3,4...n 
reason to start from 0 it shows the shift from left 



### write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill

```py
import random

names_string = input("Give me everybody's names, separated by a comma. ")
#Angela, Ben, Jenny, Michael, Chloe
names = names_string.split(", ")

random_selection=random.randint(0,len(names)-1)

will_pay=names[random_selection]

print(f"{will_pay} is going to buy the meal today!")


person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")

```


### write a program that will mark a spot with an X with the provideed position of matrix

```py

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


x=int(position[0])-1
y=int(position[1])-1

map[y][x]="X"

print(f"{row1}\n{row2}\n{row3}")

```
 

### Write a program to play rock paper scissors with computer 

    Rock wins against scissors.
    Scissors win against paper.
    Paper wins against rock.


```py 
print("Welcome to Rock Paper Scissors!!!")


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

```