# Graphical User Interfaces with Tkinter and Function Arguments

GUI - Graphical user interfaces
First - Mac Lisa
second - Windows 95

Xerox PARC was the first one to LAN, OOP(SMALLTALK-80), GUI, Mouse

## Advance Python Arguments

Arguments with Default Values: while defining the function we can assign a default value of the variables/ attributes and while calling the function it is optional to call its values

```py

def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c 

my_function(a=1, b=2, c=3)  # here when we are calling my_function it is important to provide the values of a,b,c because it does not have any default one


def my_function(a = 1, b = 2, c = 3):  # a,b,c has a default values
    #Do this with a
    #Then do this with b
    #Finally do this with c 

my_function()  # optional to specify a,b,c because it has default values



def foo(a, b=4, c=6): 
    print(a, b, c)

foo(4,6) # 4, 6, 6  

foo(1, 7, 9)  # 1 7 9

foo(20, c=6)  #20 4 6

```

### Function with Unlimited Arguments  *args

```py
# *args: Many Positional Arguments
def add(*args):
    for n in args:
        print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

add(3,4,5)  ##basically this input is in the form of tuple thats why it is also called positional arguments because position matters 

##basically this input is in the form of tuple thats why it is also called positional arguments because position matters 

def add(*args):
    print(args[0])

add(3,4,5) #output will be 3

def add(*args):
    print(args[1])

add(3,4,5) #output will be 4


```

### Function with many Keyword Arguments **kwargs

```py

def calculate(**kwargs):
    ## this tells that kwargs is dictionary 
    print(kwargs)
    
    ## using this we can loop through the dictionary kwargs
    for key, value in kwargs.items():
        print(key)
        print(value)
    
    print(kwargs["add"])  # this directly tap into the add input

calculate(add=3, multiply=5)  #{'add': 3, 'multiply': 5}   kwargs is a dictionary 


## example

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

```

### tkinter module
tkinter module is basically created using another technology called as tk, tk has every similar syntax as python
So, they took all the tk commands and options and turned them into the kwargs (optional keyword arguments)

thats why when we call any tkinter method it does not show any properties we can modify 


Creating a similar class like tkinter which takes kwargs(optional keyword arguments)

```py 

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GTR")

print(my_car.model)  # GTR

#but if we keep anyone empty it will give error
my_car = Car(make="Nissan")


## to resolve this use get(), get will give default value as none if not defined

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model) #None

```


```py
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64) #4 (7, 3, 0) {'x': 10, 'y': 64}



```