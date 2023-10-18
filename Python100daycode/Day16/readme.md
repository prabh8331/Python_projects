# Object-Oriented Programming (OOP)

## Procedural Programming

- In procedural programming, we create procedures or functions that perform specific tasks.
- The computer follows a linear flow, moving from one procedure to the next, and sometimes jumping between functions.

## Object-Oriented Programming

- OOP is used to manage complexity in software by modeling real-world objects and their relationships.
- Imagine a virtual restaurant as an example. It involves various components like a Chef, Waiter, Cleaner, and a Manager to oversee these functions.

### Modeling Objects

- OOP aims to model real-world objects. For instance, we might want to model a "Waiter."
- An object has attributes (data) and methods (functions that perform specific tasks).

### Classes and Objects

- A class is like a blueprint for an object, defining its attributes and methods.
- From a class, we can create multiple instances or objects. For example, we can have a "Waiter" class and create individual waiters like Henry and Betty.

### Attributes of a Waiter

1. `is_holding_plate` (attribute) is a boolean indicating whether the waiter is holding a plate.
2. `tables_responsible` (attribute) is a list of table numbers the waiter is responsible for.

### Methods of a Waiter

1. `take_order(table, order)` (method) allows the waiter to take an order and send it to the chef.
2. `take_payment(amount)` (method) lets the waiter add money to the restaurant's earnings.

### Summary Table

- Here's a summary table of the "Waiter" class and its objects:

| Class  | Object        | Attributes and Methods          |
| ------ | ------------- | ------------------------------- |
| Waiter | Henry, Betty  | is_holding_plate, tables_responsible, take_order, take_payment |

In OOP, classes define the structure and behavior of objects, and objects are instances of those classes. This approach helps organize and manage complex programs by breaking them down into manageable, reusable components that mimic real-world entities.

Example 2-

| Class  | Object        | Attributes and Methods          |
| ------ | ------------- | ------------------------------- |
| CarBlueprint() (First letter of each word capitalized called Pascal case) | my_car | attributes-> speed=0, fuel=32  methods-> def move(): speed =60, def stop(): speed = 0 |

my_car = CarBlueprint() # object = class() <br>
my_car.speed # object.attribute <br>
my_car.shop() # object.method() <br>

We will see this Using to understands this using a library build by someone else

[Turtle library documentation](https://docs.python.org/3/library/turtle.html)

[Turtle Colors](https://cs111.wellesley.edu/reference/colors)

```py
## Turtle Graphics
## Turtle Graphics
# Its a Blueprint for the turtle with a Paintbrush on its back

# import turtle
from turtle import Turtle, Screen  # from Module import class
# here turtle is Module and Turtle is a class which is inside this Module
# Screen is the window where Turtle will show up

# timmy = turtle.Turtle()

timmy = Turtle()  # timmy is object and Turtle is class
timmy.shape("turtle")

timmy.color("MistyRose2")
# Change color -- > https://cs111.wellesley.edu/reference/colors
# know more about the turtle library read --> https://docs.python.org/3/library/turtle.html

# Move the turtle to draw 
timmy.fd(100) # distance 
timmy.lt(20) # 20 degree 
timmy.bk(60)

my_screen = Screen()  # object = class()

print(my_screen.canvheight)  # object.attribute
# my_screen is object and canvheight is attribute associated with screen

my_screen.exitonclick()  # object.method()

```

#### How to add python Packages and use Pypi

Python Packages allows us to get hold of external packages developed by other developers

Python Packages is different from module, it is a whole bunch of code that other people have written, lots and lots of files all packaged

Install python Packages `pip3 install PrettyTable`<br>
List of Packages `pip3 list`

[Pypi](https://pypi.org/) - Python Package Index (PyPI) is a repository of software for the Python programming language

[prettytable doc](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki)


[pokedex](https://pokemondb.net/pokedex/game/x-y)

```py

# import prettytable
from prettytable import PrettyTable

# create a PrettyTable object
table = PrettyTable()

# use method 
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# change the object's attribute e.g. change table attributes
table.align = "l"

print(table)


```
