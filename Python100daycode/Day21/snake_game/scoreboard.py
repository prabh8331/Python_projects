"""Keep track of score"""
from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 10, 'normal')

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
                   align= ALIGN,
                   font=FONT)

    def update_score(self):
        """Update the Score"""
        self.clear()
        self.write(arg= f"Score: {self.score}",
                   move=False, 
                   align= ALIGN, 
                   font=FONT)
    
    def game_over(self):
        """Tells if game over"""
        self.goto(0,0)
        self.write(arg = "GAME OVER.",
                   move = False,
                   align = ALIGN,
                   font=FONT)