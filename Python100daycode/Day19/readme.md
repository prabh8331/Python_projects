# Turtle graphics

## Higher Order Functions & Event Listeners

```py
from turtle import Turtle, Screen 

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)

screen.listen()

screen.onkey(key="space", fun=move_forwards) ##onkey is event lister 

#onkey is also a higher order function 

screen.exitonclick()
```

Function as Inputs

```py

def function_a(something):
    #do this with something 
    #then do this
    #Finally do this

def function_b():
    #Do this


function_a(function_b)

```

Higher Order Functions - a function that can work with other functions 

```py

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1+n2

def multiply(n1,n2):
    return n1+n2

def divide(n1,n2):
    return n1+n2

def calculator(n1, n2, func): # this is a higher order function
    return func(n1,n2)

# calculator inputs different values and function and work with that function inside it body

result = calculator(n1=2,n2=3,func=add) # for such functions use keyword Arguments   instead of positional Argument(eg, calculator(1,2,add)) 

print(result)

```

Etch-A-Sketch

```py

## Etch-A-Sketch

# TODO: W = forward , S = Backwards , a = turn left , d = turn right, c = reset 

from turtle import Turtle, Screen 

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def turn_left():
    tim.rt(5)

def turn_right():
    tim.lt(5)

def clear():
    #screen.reset()
    # tim.setheading(0)
    # tim.goto(0,0)
    # tim.home()
    tim.clear()


screen.listen()

screen.onkey(key="w", fun=move_forwards) 
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()

```

Object State and Instances

We can have separate objects of class and these each separate objects can have there own state

1. These Separate objects are called as Instances
2. And all these multiple instances can have different set of variable and doing different things this is called the **State** of these **instances**

```py
## Turtle race

# Turtle coordinate system 
#E = 0, N = 90, W=180, S = 270
# center is (0,0) and follow x,y graph coordinate system

from turtle import Turtle, Screen 

from random import randint

screen = Screen()

screen.setworldcoordinates(llx=-250,lly=-250,urx=250,ury=250)

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]

new_turtle = []

total_turtles=6

start=((400/total_turtles)/2)*(total_turtles-1)
move = 0
#print(start)

for i in range(0,total_turtles):
    new_turtle.append(Turtle(shape="turtle"))
    new_turtle[i].color(colors[i])
    new_turtle[i].penup()
    new_turtle[i].goto(x=-225,y=start-move)
    move += (400/total_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in new_turtle:
        turtle.fd(randint(0,10))
        # print(turtle.ycor())

        if turtle.xcor() >= 240:
            is_race_on = False
            if user_bet == turtle.color()[0]: 
                print(f"You've won! The {turtle.color()[0]} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.color()[0]} turtle is the winner!")


#If user_bet has a value (i.e., it is defined and not empty), 
# the if statement evaluates to True, 
# and the code inside the if block is executed. 
# If user_bet is not defined or empty 
# (i.e., the user hasn't entered anything), 
# the if statement evaluates to False, 
# and the code inside the if block is skipped

# tim.setx(-225)
# jim.setx(-225)
# kim.setx(-225)
# sim.setx(-225)

# tim.sety(50)
# jim.sety(-50)
# kim.sety(150)
# sim.sety(-150)

# tim.pendown()
# jim.pendown()
# kim.pendown()
# sim.pendown()

screen.exitonclick()

```
