from turtle import Turtle
class Snake:
    """Models the snake"""
    def __init__(self):
        self.the_snake = []
        self.xpos=0
        for i in range(3):
            new_snake_tail = Turtle(shape="square")
            new_snake_tail.color("white")
            new_snake_tail.penup()
            self.the_snake.append(new_snake_tail)
            self.the_snake[i].goto(self.xpos,0)
            self.xpos -= 20

    def move_up(self):
        if self.the_snake[0].heading() == 270:
            pass
        else:
            self.the_snake[0].setheading(90)

    def move_down(self):
        if self.the_snake[0].heading() == 90:
            pass
        else:
            self.the_snake[0].setheading(270)

    def move_left(self):
        if self.the_snake[0].heading() == 0:
            pass
        else:
            self.the_snake[0].setheading(180)

    def move_right(self):
        if self.the_snake[0].heading() == 180:
            pass
        else:
            self.the_snake[0].setheading(0)

    def snake_move(self):
        """Moves the snake"""

        pos = (self.the_snake[0].xcor(),self.the_snake[0].ycor())
        self.the_snake[0].fd(20)    

        for i in range(1,len(self.the_snake)):
            pos2 = (self.the_snake[i].xcor(), self.the_snake[i].ycor())
            self.the_snake[i].goto(pos)
            pos = pos2