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