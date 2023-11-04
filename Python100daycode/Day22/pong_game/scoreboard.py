"""Keep track of score"""
from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 40, 'normal')

class ScoreBoard(Turtle):
    """Keep track of score"""
    def __init__(self):
        super().__init__()
        self.left_scoreboard = Turtle()
        self.left_score = 0
        self.left_scoreboard.color("white")
        self.left_scoreboard.hideturtle()
        self.left_scoreboard.penup()
        self.left_scoreboard.goto(-50,340)
        self.left_scoreboard.write(arg= f"{self.left_score}",
                   move=False,
                   align= ALIGN,
                   font=FONT)

        self.right_scoreboard = Turtle()
        self.right_score = 0
        self.right_scoreboard.color("white")
        self.right_scoreboard.hideturtle()
        self.right_scoreboard.penup()
        self.right_scoreboard.goto(50,340)
        self.right_scoreboard.write(arg= f"{self.right_score}",
                   move=False,
                   align= ALIGN,
                   font=FONT)

        self.line = Turtle()
        self.line.color("white")
        self.line.penup()
        y = 420
        self.line.goto(0,y)
        self.line.setheading(270)
        while y > -420:
            self.line.pendown()
            self.line.fd(20)
            self.line.penup()
            self.line.fd(20)
            y-=40


    def update_left_score(self):
        """Update the Score"""
        self.left_score += 1
        self.left_scoreboard.clear()
        self.left_scoreboard.write(arg= f"{self.left_score}",
                   move=False, 
                   align= ALIGN, 
                   font=FONT)


    def update_right_score(self):
        """Update the Score"""
        self.right_score += 1
        self.right_scoreboard.clear()
        self.right_scoreboard.write(arg= f"{self.right_score}",
                   move=False, 
                   align= ALIGN, 
                   font=FONT)
        
    def game_over(self):
        """Tells if game over"""
        self.line.penup()
        self.line.goto(0,0)
        if self.right_score == 10:
            self.line.write(arg = "RIGHT WON! GAME OVER.",
                    move = False,
                    align = ALIGN,
                    font=FONT)
        else:
            self.line.write(arg = "LEFT WON! GAME OVER.",
                    move = False,
                    align = ALIGN,
                    font=FONT)