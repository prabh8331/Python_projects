from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = 280

class CarManager():
    def __init__(self) -> None:
        self.cars = []
        self.new_car()

    def new_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(choice(COLORS))
        y = randint(-25,25)*10
        new_car.turtlesize(stretch_wid=1,stretch_len=2)
        new_car.setheading(180)
        new_car.goto(X, y)
        self.cars.append(new_car)
        # print(y)

    def car_move(self,current_score):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*(current_score))
