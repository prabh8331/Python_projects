from turtle import Turtle, Screen, colormode

from random import randint

tim = Turtle()

# shape of the curser
tim.shape("turtle")

# color of the curser
tim.color("red")

# move the curser
#timmy_the_turtle.forward(100)

# turn the curser
#timmy_the_turtle.right(90)

# Draw the square

# for _ in range(4):
#     tim.fd(100)
#     tim.lt(90)


# Draw the dashed lines

# for _ in range(30):
#     tim.fd(5)
#     tim.penup()
#     tim.fd(5)
#     tim.pendown()

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
tim.color(r, g, b)

# Draw the multiples polygons 

for i in range(3,11):
    tim.setheading(0)
    for j in range(i):
        if(j%2==0):
            tim.fd(100)
        else:
            tim.bk(100)
        tim.left((180 * (i - 2)) / i)




screen = Screen()
screen.exitonclick()
