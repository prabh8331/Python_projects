from turtle import Turtle

UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0
PADDLE_LIMIT =340

class Paddle:
    """Models the paddle of pong game"""
    def __init__(self):
        self.left_paddle = []
        self.right_paddle = []
        x_left = -380
        x_right = 373
        y_left = [0,-20,20,40,-40]
        y_right = [0,-20,20,40,-40]

        for i in range(5):
            left_paddle_body = Turtle(shape="square")
            left_paddle_body.color("white")
            left_paddle_body.penup()
            self.left_paddle.append(left_paddle_body)
            self.left_paddle[i].goto(x_left,y_left[i])
        
        for i in range(5):
            right_paddle_body = Turtle(shape="square")
            right_paddle_body.color("white")
            right_paddle_body.penup()
            self.right_paddle.append(right_paddle_body)
            self.right_paddle[i].goto(x_right,y_right[i])
        

    def left_up(self):
        if self.left_paddle[0].ycor()<PADDLE_LIMIT:
            for paddle in self.left_paddle:
                paddle.setheading(UP)
                paddle.fd(40)

    def right_up(self):
        if self.right_paddle[0].ycor()<PADDLE_LIMIT:
            for paddle in self.right_paddle:
                paddle.setheading(UP)
                paddle.fd(40)

    def left_down(self):
        if self.left_paddle[0].ycor()>-PADDLE_LIMIT:
            for paddle in self.left_paddle:
                paddle.setheading(DOWN)
                paddle.fd(40)

    def right_down(self):
        if self.right_paddle[0].ycor()>-PADDLE_LIMIT:
            for paddle in self.right_paddle:
                paddle.setheading(DOWN)
                paddle.fd(40)