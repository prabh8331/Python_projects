## Randomisation and Python Lists 

```md
Python use **Mersenne Twister** pseudorandom rumber generator, we will use random module to genertae random numbers 
```

```md
In Python, a **module** is a file containing Python code that can include functions, classes,
and variables. Modules are used to organize and encapsulate related pieces of code into 
reusable units. They help in keeping code clean, maintainable, and logically structured. 
```


``` md 
`main.py` is usually the entry point, it could be different (`__init__.py`) but enty point is a file which will be executed when we run our code  
```

### Create your own module 
```py a_module.py
pi = pi = 3.14159246
```

``` py main.py
import a_module

print(a_module.pi)
```


``` py main.py

import random 

random_interger = random.randint(1,10)
print(random_interger)

```

