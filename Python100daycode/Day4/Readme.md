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


##### `main.py` is usually the entry point, it could be different (`__init__.py`) but enty point is
##### a file which will be executed when we run our code  


``` py main.py

import random 

random_interger = random.randint(1,10)
print(random_interger)

```

