"""Keep track of score"""
from turtle import Turtle

class ScoreBoard(Turtle):
    """Keep track of score"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.write(arg= f"Score: {self.score}",
                   move=False, 
                   align= "center", 
                   font=('Arial', 10, 'normal'))

    def update_score(self):
        """Update the Score"""
        self.clear()
        self.write(arg= f"Score: {self.score}",
                   move=False, 
                   align= "center", 
                   font=('Arial', 10, 'normal'))
        