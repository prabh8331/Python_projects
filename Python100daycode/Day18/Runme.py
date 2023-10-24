from turtle import Turtle, Screen, colormode

from random import choice, randint

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


color_list = ["red","green","blue","purple","orange","pink","yellow","brown","cyan","magenta","lime","turquoise","gold","indigo","violet","teal","maroon","navy","coral","olive","sienna","tomato","steelblue","darkgreen","chocolate","slategray","darkorange","firebrick","skyblue","thistle"]

# Draw the multiples polygons 

# for i in range(3,5):
#     tim.color(choice(color_list))
#     tim.setheading(0)
#     for j in range(i):
#         if(j%2==0):
#             tim.fd(100)
#         else:
#             tim.bk(100)
#         tim.left((180 * (i - 2)) / i)

# tim.setheading(0)


# for i in range(5,11):
#     tim.color(choice(color_list))
#     for j in range(i):
#         tim.fd(100)
#         tim.right(360/i)



# TODO: adjust the thickness of the line 
tim.pensize(7)

# TODO: speed up the turtle 
#tim.speed(100)
tim.speed("fastest")

steps = 360

angles=[0,90,180,270]


# set random color of turtle 
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)


# my_tuple=(1,3,5)
# print(my_tuple[2])
# Tuples are Ordered (elements in a tuple maintain their order), 
# Immutable (once you create a tuple, you cannot change, add, or remove elements from it), 
# Heterogeneous, can contain elements of different data types


## ####Random walk  #########

# for _ in range(steps):
#     #tim.color(choice(color_list))
#     #tim.left(choice(angles))
#     tim.color(random_color())
#     tim.setheading(choice(angles))
#     tim.forward(30)


#### Draw a spirograph 
# steps=100
# angle = 360/steps
# tim.pensize(1)

# for _ in range(steps):
#     tim.color(random_color())
#     #tim.left(angle)
#     tim.circle(100)
#     tim.setheading(tim.heading()+angle)






screen = Screen()

screen.exitonclick()
