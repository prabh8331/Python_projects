"""Ball Movement"""
from turtle import Turtle
from random import randint,choice

UPLEFT = 135
UPRIGHT = 45
DOWNRIGHT = 315
DOWNLEFT = 225

LEFT = [135,225]
RIGHT = [45,315]

class Ball(Turtle):
    """Ball Movement"""
    def __init__(self):
        super().__init__() 
        self.shape("circle") 
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.setheading(choice(LEFT))

    def reset_ball(self): 
        """will generate new food
        """
        ball_x = 0
        ball_y = randint(-19,19)*20
        self.goto(ball_x,ball_y)


    def move_ball(self):
        self.fd(20)

    def ball_heading(self):
        if 390 - self.ycor() < 20 :
            #print(self.heading())
            if self.heading() == UPLEFT:
                self.setheading(DOWNLEFT)
            if self.heading() == UPRIGHT:
                self.setheading(DOWNRIGHT)

        if self.ycor() + 390 < 20:
            #print(self.heading())
            if self.heading() == DOWNLEFT:
                self.setheading(UPLEFT)
            if self.heading() == DOWNRIGHT:
                self.setheading(UPRIGHT)
