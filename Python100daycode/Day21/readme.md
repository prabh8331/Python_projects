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