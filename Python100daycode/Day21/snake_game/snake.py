from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        self.head = self.the_snake[0]
        self.key_pressed = False


    def extend_snake(self):
        new_snake_tail = Turtle(shape="square")
        new_snake_tail.color("white")
        new_snake_tail.penup()
        self.the_snake.append(new_snake_tail)
        # snake_length = len(self.the_snake)
        # pos = (self.the_snake[snake_length-2].xcor(),self.the_snake[snake_length-2].ycor())
        # self.the_snake[snake_length-1].goto(pos)
        pos = (self.the_snake[-2].xcor(),self.the_snake[-2].ycor())
        self.the_snake[-1].goto(pos)

    def move_up(self):
        if self.head.heading() != DOWN and not self.key_pressed:
            self.head.setheading(UP)
            self.key_pressed = True

    def move_down(self):
        if self.head.heading() != UP and not self.key_pressed:
            self.head.setheading(DOWN)
            self.key_pressed = True

    def move_left(self):
        if self.head.heading() != RIGHT and not self.key_pressed:
            self.head.setheading(LEFT)
            self.key_pressed = True

    def move_right(self):
        if self.head.heading() != LEFT and not self.key_pressed:
            self.head.setheading(RIGHT)
            self.key_pressed = True

    def snake_move(self):
        """Moves the snake"""

        pos = (self.the_snake[0].xcor(),self.the_snake[0].ycor())
        self.the_snake[0].fd(20)

        for i in range(1,len(self.the_snake)):
            pos2 = (self.the_snake[i].xcor(), self.the_snake[i].ycor())
            self.the_snake[i].goto(pos)
            pos = pos2