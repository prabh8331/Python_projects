# Class Creation and Object Initialization

## Syntax of Class Creation and Creating an Object from a Class

To create a class & object, use the following syntax:

For the naming of class use PascalCase
    PascalCase- Every first letter of every word capitalized
    camelCase- Every first letter of every word capitalized but not first letter of the first word
    snake_case - Every letter in lower and each word separated by underscore "_"

```python
class MyUser:
    pass  # If there is nothing to include in the class, use 'pass'

# create object from the class
user_1 = MyUser()
```

## Creating Class Attributes

### Method 1: Tapping into Object

You can create attributes for a class by directly assigning values to an object:

```python
class MyUser:
    pass

user_1 = MyUser()

# attribute creation  
user_1.id = "001"
user_1.username = "prabh"
print(user_1.username)

```

### Method 2: Using Constructors

When we need to specify starting pieces of information for an object, we use Constructor. A constructor is a special method named `__init__` within a class.

Constructor: what should happen when object is constructed also called as Initializing an object

```python
class Car:
   def __init__(self):
      print("Test if runs as object is created")

my_car=Car()  # every time object is created __init__ method is called 

```

## Example:

```python
class User:
   def __init__(self, user_id, username):
      self.id = user_id
      self.username = username  # general guideline is attribute name should be same as parameter but if different that is fine 
      self.follower = 0  # if we don't want a variable which have to be provided at initializing of object , we set it to a default value 

#Create an object with attributes:

user = User("001", "prabh")
user_2 = User("001", "prabh")
# if we don't pass all the attribute we defined in __init__ 
# it will give error --> missing required positional argument

print(user_2.id)
print(user_2.follower)

```

## Creating Class Methods

To create methods in a class, define them within the class. A method always needs a `self` parameter to refer to the object that called it.

```python
class ClassName:
   def method_name(self, parameter1, parameter2):
      # Method logic here
```

## Example:

```python
class User:
   def __init__(self, user_id, username):  
      self.id = user_id  
      self.username = username  
      self.followers = 0
      self.following = 0
   
   def follow(self, user):
      user.followers += 1
      self.following +=1


user_2 = User("001", "prabh")
user_3= User("002","komal")

user_2.follow(user_3)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)
```
