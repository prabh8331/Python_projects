from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

 
paddles = Paddle()

scoreboard = ScoreBoard()

ball = Ball()
ball.reset_ball()

game_is_on = True

UPLEFT = 135
UPRIGHT = 45
DOWNRIGHT = 315
DOWNLEFT = 225

LEFT = [135,225]
RIGHT = [45,315]

while game_is_on:

    screen.listen()
    screen.onkey(key="Up", fun= paddles.right_up)
    screen.onkey(key="Down", fun= paddles.right_down)
    screen.onkey(key="w", fun= paddles.left_up)
    screen.onkey(key="s", fun= paddles.left_down)
    
    ball.move_ball()

    ball.ball_heading()

    for paddle in paddles.left_paddle:
        # print(ball.distance(paddle))
        if ball.distance(paddle) < 25 and ball.heading()==UPLEFT:
            ball.setheading(UPRIGHT)
        if ball.distance(paddle) < 25 and ball.heading()==DOWNLEFT:
            ball.setheading(DOWNRIGHT)

    for paddle in paddles.right_paddle:
        # print(ball.distance(paddle))
        if ball.distance(paddle) < 25 and ball.heading()==UPRIGHT:
            ball.setheading(UPLEFT)
        if ball.distance(paddle) < 25 and ball.heading()==DOWNRIGHT: 
            ball.setheading(DOWNLEFT)

    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.update_right_score()

    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.update_left_score()

    if scoreboard.right_score == 10 or scoreboard.left_score == 10:
        scoreboard.game_over()
        game_is_on = False


    screen.update()

    time.sleep(0.01)


screen.exitonclick()