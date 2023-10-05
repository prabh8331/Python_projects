### Debugging 

1. Describe the Problem 

```py
# # Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
# What the for-loop doing?  > for loop will run from 1 to 19 
# When is the function meant to print "You got it"? --> print statement will run when i == 20, which is not happening  
# What are your assumptions about i? --> Here assumption is I will include 20 , but that is not the case to increase the range by making ranger 1 to 21

# solution  
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

```

2. Reproduce the Bug 

```py
# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
# When we run the above code some times it works but occasionally we get's the error 
# this is usually the difficult bug in code 
# once you get the error capture the error and see when it occur 

######## error msg #########
# Traceback (most recent call last):
#   File "c:\Users\prabh\OneDrive\Desktop\Python_projects\Python100daycode\Day13\Debugging.py", line 17, in <module>
#     print(dice_imgs[dice_num])
#           ~~~~~~~~~^^^^^^^^^^
# IndexError: list index out of range

### here we are trying to reproduce the error case 
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
dice_num = 6
print(dice_imgs[dice_num])

### Fixed code 
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


```

3. Play Computer 

```py
# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

## We pick some random inputs and specially those which are used in conditions e.g 1979, 1980 , 1981 , 1990, 1994, 2000 and we play computer and run code one by one line
# by running above code I find if value is 1980 or above nothing will print which is kind of ok because we don't expect some to be alive of that age 
# but if someone is putting 1994 if and elif both are failing # i.e 1994 is not captured in any bucket 

#fixed code 
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

```


4. Fix the Errors 
# resolve others bug on stack overflow and discod channels
```py
# # Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

#1. fix the errors in editor
age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}.")

#2. console error - 1. capture the error , understand (ask google/chatgpt) and resolve  , we can see below it expected int but was given string 
# TypeError: '>' not supported between instances of 'str' and 'int'

age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")

#3. Bug when expected some other behavior but not working as expected , here example is we want to print actual age but printing {bug}

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

```

5. Print is Your Friend

```py

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

### print output at each steps to check the result 

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page)  ## here value is 0 because in above statement we are not assigning anything but comparing 
total_words = pages * word_per_page
print(total_words)

# fix 
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

```

6. Using a online debugger 
<https://pythontutor.com/render.html#mode=edit>

```py

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# use online debugger to run code by line by line 
#https://pythontutor.com/render.html#mode=edit

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # this append was running at last so only 13*2 is getting stored ,
    #but we wanted to store complete list so gave the intend here to bring it inside the for loop
  print(b_list)

mutate([1,2,3,5,8,13])

```

7. Take a Break 
8. Ask a Friend 
9. Run Often ## run the code every steps  
10. Ask StackOverflow # last resort if no one has actually asked 


### Problem 1. 

```py 

## 1. Debugging odd and even 
# number = int(input())

if number % 2 = 0:
    print("THis is an even number.")
else:
    print("This is an odd number.")

#Error msg 
#   SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

# fixed 

number = int(input())

if number % 2 == 0:
    print("THis is an even number.")
else:
    print("This is an odd number.")
```

### Problem 2. 

```py 
#Which year do you want to check?
year = input()

if year % 4 == 0:
    if year % 100:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

##TypeError: not all arguments converted during string formatting  

# Fixed error

#Which year do you want to check?
year = int(input("year: "))

if year % 4 == 0:
    if year % 100:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

```

#### problem 4 

```py

# # Fizzbuzz game - if number is divisible by 3 then fizz in by 5 then buzz if divisible by both then fizzbuzz, else number 
# target= int(input("Target: "))

# for number in range(1, target+1):
#     if number % 3 == 0 or number % 5 == 0:
#         print("Fizzbuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])


## Solution: 
target= int(input("Target: "))

for number in range(1, target+1): 
    if number % 3 == 0 and number % 5 == 0: # or to and
        print("Fizzbuzz")    
    elif number % 3 == 0: # if to elif
        print("Fizz")
    elif number % 5 == 0: # if to elif
        print("Buzz")
    else:
        print(number) # remove square brackes []


```