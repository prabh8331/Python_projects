## Randomisation and Python Lists 

```md
Python use **Mersenne Twister** pseudorandom rumber generator, we will use random module to genertae random numbers 
```

```md
In Python, a **module** is a file containing Python code that can include functions, classes,
and variables. Modules are used to organize and encapsulate related pieces of code into 
reusable units. They help in keeping code clean, maintainable, and logically structured. 
```


### Create your own module 
`a_module.py:`
```py 
pi = pi = 3.14159246
```

`main.py:`
``` py 
import a_module

print(a_module.pi)
```


`main.py` is usually the entry point, it could be different (`__init__.py`) <br> 
but enty point is a file which will be executed when we run our code


### Random Module
`main.py:`
``` py 

import random 

random_interger = random.randint(1,10)  #this will generate random interg b/w 1 and 10
print(random_interger)

random_float = random.random()   # this will generate random flaod b/w 0 and 1 but will not inclured 1 will be like 0.9999999 etc. 
print(random_float)

# Random b/w 0 and 5
random_float5=random_float*5
print(random_float5)

# example roll a dice  
dice_roll = random.randint(1,6)
print(f"you got {dice_roll}")

```

### Heads or Tails 

