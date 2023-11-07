import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

# Move the turtle with keypress -- 1
# Create and move the cars -- 4 
# Detect collision with car -- 5
# Detect when turtle reaches the other side --2  
# Create a scoreboard -- 3 

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

score = Scoreboard()

cars = CarManager()

start_prob = 7

game_is_on = True
while game_is_on:

    screen.listen()
    screen.onkey(key="Up", fun= player.move)

    if player.ycor()>=290:
        player.postion_reset()
        score.score_up()
        if start_prob > 2:
            start_prob  -= 1
        print(start_prob)

    make_car = randint(1,start_prob)

    if make_car == 1:
        cars.new_car()
    
    for car in cars.cars:
        if (car.xcor() < 35 and car.xcor() > -30) and (player.ycor() - car.ycor() <= 18 and player.ycor() - car.ycor() >= -20):
            # print("collide")
            game_is_on=False
            score.game_over()

    cars.car_move(current_score=score.score)

    time.sleep(0.1)
    screen.update()

screen.exitonclick()