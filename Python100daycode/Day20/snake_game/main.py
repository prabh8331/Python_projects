from turtle import Screen, Turtle
from snake import Snake

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Run")
screen.tracer(0)

snake=Snake()

screen.update()

game_is_on = True

while game_is_on:

    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up) 
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

    snake.snake_move()
    screen.update()
    time.sleep(0.4)

screen.exitonclick()