### Namespaces: Local vs. Global Scope 

```py

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



```

#### Local Scope 

```py
def drink_potion():
  potion_strength = 2 
  print(potion_strength)

drink_potion()
print(potion_strength) # this will give error  ## NameError 
#It's trying to print a variable that is local to drink_portion() function and is only available inside the function. so it will give NameError 
```

#### Global scope 
```py
player_health = 10 # this is global variable because it it assigned at the top level 

def drink_potion():  
  potion_strength = 2 
  print(player_health)

drink_potion()
print(player_health)
```

Namespace is anting we define, and namespace can be accessed within the certain scope 

#### There is no Block Scope in python 
```py
game_level = 3 

enemies= ["Skeleton","Zombie","Alien"]

if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)  ## if variable is defined inside if or any loop, 
#then it does not have any different block scope , it does not count as any septate local scope 
```

#### How to Modify a Global Variable 
```py

enemies = 1 # this is a global variable 

def increase_enemies():
  enemies = 2  # this is a local variable   
  # its not a good idea to define local variable name same as global variable 
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

## if we want to modify global variable inside the function we mention it is a global variable 
def increase_enemies():
  global enemies  # it is ok to use the global variable inside the function but not a good idea to modify it inside the local scope because it is very easy to make an error doing so 
  enemies += 2  # not recommended 
  print(f"enemies inside function: {enemies}")


## We can use return to actualy achive this 

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1 

enemies = increase_enemies()
print(f"enemies inside function: {enemies}")

```

#### Global Constants 
We should be careful with variables that have global scope, 
but global scope can be incredibly useful in case of global constants 

Global constants are variables which we define and never planning to change it ever again 

```py
PI = 3.14159  # it is recommended to use upper case for the Global constants 
URL = "https:www.google.com"

def cal():
    PI

```
