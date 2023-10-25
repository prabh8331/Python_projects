#The Hirst Painting Project 
# will use library called colorgram - https://pypi.org/project/colorgram.py/
#pip3 install colorgram.py

import colorgram

from turtle import Turtle, Screen, colormode

from random import choice, randint


colors = colorgram.extract(r'C:\Users\prabh\OneDrive\Desktop\Python_projects\Python100daycode\Day18\HirstPainting.jpg',40)

color_tuple = []

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r,b,g)
    color_tuple.append(new_color)

print(color_tuple)

# https://www.w3schools.com/colors/colors_rgb.asp

color_tuple = [(210, 109, 155), (52, 137, 95), (159, 48, 82), (222, 109, 209), (19, 58, 36), (127, 196, 163), (183, 28, 163), (54, 19, 30), (191, 159, 141), (126, 93, 69), (207, 70, 91), (47, 71, 128), (125, 155, 180), (159, 13, 22), (59, 42, 30), (128, 44, 27), (21, 43, 52), (192, 111, 91), (51, 99, 167), (41, 96, 61), (231, 188, 165), (26, 52, 92), (108, 170, 119), (226, 168, 177), (224, 5, 206), (10, 104, 87), (147, 191, 212), (64, 30, 80), (172, 217, 185), (56, 190, 146), (162, 215, 202)]




### TODO: paint 10 by 10 rows of spots 
### TODO: size of dot = 20   and space b/w the dots should be 50

screen = Screen()

#screen.screensize(500,500)
#screen.setup(width=700, height=700)

screen.setworldcoordinates(-250, -250, 250, 250)

#screen.tracer(0)

#print(screen.canvheight)

#print(screen.canvwidth)

colormode(255)

tim = Turtle()
# shape of the curser
#tim.shape("turtle")

#tim.pensize(20)

#tim.right(90)

steps  = 10

tim.speed("fastest")

y=0

tim.penup()

tim.hideturtle()

for _ in range(steps):
    #tim.penup()
    tim.setx(-225)
    tim.sety(-225+y)
    #tim.pendown()
    for _ in range(steps):
        tim.color(choice(color_tuple))
        #tim.left(angle)
        tim.dot(20)
        #tim.penup()
        tim.fd(50)
        #tim.pendown()
    y+=50

screen.update()

screen.exitonclick()
