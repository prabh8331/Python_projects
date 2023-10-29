from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Run")
screen.tracer(0)

snake = Snake()

food = Food()

score = ScoreBoard()

food.new_food()

screen.update()

game_is_on = True

while game_is_on:

    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

    snake.snake_move()
    #screen.update()

    if snake.head.distance(food) <5:
        score.score += 1
        food.new_food()
        score.update_score()

    screen.update()

    snake.key_pressed = False # this will ensure in each loop key is pressed only once
    ### this is an BUG fix: snake moving backward when you press keys quickly is likely
    # due to multiple key events being triggered before the snake completes its previous move.
    # This can happen if the key repeat rate of your keyboard is high,
    # causing multiple key events to be registered

    time.sleep(0.4)

screen.exitonclick()