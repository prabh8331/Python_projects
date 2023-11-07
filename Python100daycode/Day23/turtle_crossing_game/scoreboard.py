from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(-260,260)
        self.write(arg= f"Level: {self.score+1}",
                   move=False,
                   font=FONT)
        
    def score_up(self):
        self.clear()
        self.score += 1 
        self.write(arg= f"Level: {self.score+1}",
                   move=False,
                   font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg= "GAME OVER",
                   align="center",
                   move=False,
                   font=FONT)
   
