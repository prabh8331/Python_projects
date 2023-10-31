# Class Inheritance

```py
#Class Inheritance - classes can inherit from other classes, inheriting attributes, inheriting methods

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

    def eat(self):
        print("Find and eat food.")
    
class Fish(Animal):              #### Animal is the super class and Fish is the subclass
    def __init__(self):
        super().__init__()         #### doing this will bring all the attributes and methods from the Animal class #e.g. is eat() method without defining we can access it 

    def breathe(self):
        super().breathe()    ## along with what happening with breathe() method in superclass
        print("doing this underwater.")  # this will add what extra needed to be done

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.eat()

```

## Slicing Lists

```py
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5]) #['c', 'd', 'e']

print(piano_keys[2:]) #["c", "d", "e", "f", "g"]

print(piano_keys[:5]) #['a', 'b', 'c', 'd', 'e']

print(piano_keys[1:6:2]) # here 2 is the increment #['b', 'd', 'f']

print(piano_keys[::2])   # every odd no ['a', 'c', 'e', 'g']

print(piano_keys[::-1])   # reversed list ['g', 'f', 'e', 'd', 'c', 'b', 'a']

#same works with tuple too
print(piano_tuple[1:])

```
