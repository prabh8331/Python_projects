from turtle import Turtle

class Food(Turtle):
    """Food class is going to know how to render itself as a small circle on the screen.
    And then every time the snake touches the food, then that food is going to move to a new random location. """
    def __init__(self):
        #self.food = Turtle()    # instead of creating it as an attribute in this class, we actually inherited from turtle class
        super().__init__()  # so now food have all the capabilities of the turtle class , now we will tell it some specific thing how to do so it behaves like food 
        self.shape("circle")   # I can directly use method from Turtle class (superclass) inside the Food class (subclass) now
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("navajo white")  
        self.speed("fastest  bn   ")