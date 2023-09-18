## Code Blocks, Funtions & While Loops 

### Functions 
Python built-in functions --> <https://docs.python.org/3/library/functions.html>

`Examples of Functions:` 
```py
print("Hellow)
len("Hello")
```

Create a own functions:
```py
# Defining Functions 
def my_function(): 
    print("Hello")
    print("Bye")

#calling the functions
my_function()
```

### Reeborg's World
Link- <https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json>

<details>
    <summary>Instructions to play this game:</summary>
    There are some prebuilt commands (funtions) and can use python language to tell reeborg to do stuff. 
    We can create our own functions and there are different world which and chalanges 
</details>

`Create functions and make square:`
```py
# turn around function define
def turn_around():
    turn_left()
    turn_left()

#turn right function
def turn_right():
    turn_around()
    turn_left()

#Numbers of steps to take
def steps(step):
    for i in range(step):
        move()

#Draw square
turn_left()
steps(1)
turn_right()
steps(1)
turn_right()
steps(1)
turn_right()
steps(1)
```


`Reeborg's Hurdles race:`

<details>
    <summary>Instructions:</summary>
    There will be a map, we have to write a code to command Reeborg to follow few steps and over come hurdles to complete the race.
<details>



#### Hurdle race 1 
Link: <https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json>

`Reeborg's programming to complete race:`
```py
# turn around function define
def turn_around():
    turn_left()
    turn_left()

#turn right function
def turn_right():
    turn_around()
    turn_left()

#Numbers of steps to take
def steps(step):
    for i in range(step):
        move()

# Jump the hurdles of length of n block:
def jump(block):
    turn_left()
    steps(block)
    turn_right()
    steps(1)
    turn_right()
    steps(block)
    turn_left()

for i in range(6):
    steps(1)
    jump(1)

```


### Indentations
Most common type of error in python can be indentation error, this simply mean the spacing should be good, in other language {} is common way but not in python


### While Loops 

#### while condition_is_ture

#### Hurdle race 2 # here goal possition is random
Link:<https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json>

`Reeborg's programming to complete race:`
```py
# turn around function define
def turn_around():
    turn_left()
    turn_left()

#turn right function
def turn_right():
    turn_around()
    turn_left()

#Numbers of steps to take
def steps(step):
    for i in range(step):
        move()

# Jump the hurdles of length of n block:
def jump(block):
    turn_left()
    steps(block)
    turn_right()
    steps(1)
    turn_right()
    steps(block)
    turn_left()

#while at_goal()==False:
while not at_goal():
    steps(1)
    jump(1)

```

`note:`
use **for loop** when we know how many time we want to loop, where loop iteration is constant or we are looping over some list <br>
and we use **while loop** when we don't know the how many time we want to iterate but we know when this contion is false then stop the loop . <br>
while loop are bit of dangrous and we need to be very carefull while makeing this loop because if that conditions never fail we can face a **Infinite Loop** <br>
best practice is print out the loop conditions to know what is happening in your loop 


#### Hurdle race 3 # here Hurdle possition is random
<https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json>

`Reeborg's programming to complete race:`
```py
# turn around function define
def turn_around():
    turn_left()
    turn_left()

#turn right function
def turn_right():
    turn_around()
    turn_left()

#Numbers of steps to take
def steps(step):
    for i in range(step):
        move()

# Jump the hurdles of length of n block:
def jump(block):
    turn_left()
    steps(block)
    turn_right()
    steps(1)
    turn_right()
    steps(block)
    turn_left()

#while at_goal()==False:
while not at_goal():
    if front_is_clear():
        steps(1)
    elif wall_in_front():
        jump(1)

```

#### Hurdle race 4 # here Hurdle height is variable
<https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json>

`Reeborg's programming to complete race:`
```py
# turn around function define
def turn_around():
    turn_left()
    turn_left()

#turn right function
def turn_right():
    turn_around()
    turn_left()

#Numbers of steps to take
def steps(step):
    for i in range(step):
        move()

# Jump the hurdles of length of n block:
# Method 1 of Jump 
#def jump(block):
#    hurdle_size=0
#    while wall_in_front():
#        turn_left()
#        steps(block)
#        turn_right()
#        hurdle_size+=1
#    steps(1)
#    turn_right()
#    steps(hurdle_size)
#    turn_left()

# Method2 
def jump(block):
    hurdle_size=0
    turn_left()
    while wall_on_right():
        steps(block)
        hurdle_size+=1
    turn_right()
    steps(1)
    turn_right()
    steps(hurdle_size)
    turn_left()


#Method 2 of Jump

#while at_goal()==False:
while not at_goal():
    if front_is_clear():
        steps(1)
    elif wall_in_front():
        jump(1)

```


#### Reeborg escape the maze 
Link: <https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json>

<details>
    <summary>World Info:</summary>
    Lost in a maze
    Reeborg was exploring a dark maze and the battery in its flashlight ran out.
    Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
</details>

```py
#turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Reeborg can stuck in such position it might just loop in one place only in circles 
# to avoid such issue in starting of the code it will search for any wall and once it finds a wall it will turn left so that in its right there is a wall
# then then it can follow along the right edge till it find the goal 
if not wall_on_right() and front_is_clear():
    turn_left()
    turn_left()
    if not wall_on_right() and front_is_clear():
        move()
        if wall_in_front():
            turn_left()
        else:
            while not wall_in_front():
                move()
            turn_left()
    elif not wall_in_right():
        turn_left()

elif not wall_on_right():
    turn_left()

# easy and better solution # find a wall in front first and turn left , above code is doing same 
# while not wall_in_front:
#     move()
# turn_left()

#in this condition are first checking if there is a wall on right if there is a wall of right then turn right and if front is clear move 
# then if there is wall on right then just move 
# if there is no wall on right and can't move to frount then turn_left

while not at_goal():
    if not wall_on_right():
        turn_right()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()


```