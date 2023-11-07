from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)
        # print(f"player {self.ycor()}")

    def postion_reset(self):
        self.goto(STARTING_POSITION)
        