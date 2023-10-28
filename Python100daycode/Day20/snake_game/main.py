from turtle import Screen, Turtle

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Run")

screen.tracer(0)


# import time  # Import the time library for controlling snake movement speed.

# # In the Turtle library, after each action, the screen is updated to display the new state. 
# # By setting the tracer to 0, we disable the automatic animation update after each action.
# screen.tracer(0)

# # Manually update the current state of the screen.
# screen.update()

# # Introduce a sleep of 0.4 seconds to control the time interval between updates, 
# # which helps control the speed of the snake's movement.
# time.sleep(0.4)



##### the snakes boby ####
the_snake = []

xpos=0

for i in range(3):
    new_snake_tail = Turtle(shape="square")
    new_snake_tail.color("white")
    new_snake_tail.penup()
    the_snake.append(new_snake_tail)
    the_snake[i].goto(xpos,0)
    xpos -= 20   # dimension of turtle/curser is 20*20 pixel 

screen.update()
# starting_position = [(0, 0), (-20, 0), (-40, 0)]

# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)

def move_up():
    the_snake[0].setheading(90)

def move_down():
    the_snake[0].setheading(270)

def move_left():
    the_snake[0].setheading(180)

def move_right():
    the_snake[0].setheading(0)

###### Move the snake 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.4)
    
    screen.listen()
    screen.onkey(key="w", fun=move_up) 
    screen.onkey(key="s", fun=move_down)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)

    pos = (the_snake[0].xcor(),the_snake[0].ycor())
    the_snake[0].fd(20)    

    for i in range(1,len(the_snake)):
        pos2 = (the_snake[i].xcor(), the_snake[i].ycor())
        the_snake[i].goto(pos)
        pos = pos2
        


screen.exitonclick()