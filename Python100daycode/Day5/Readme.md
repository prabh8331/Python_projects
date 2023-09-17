## Loops

### For loop , for item in list_of_items

``` py 
fruits = ["Cherry" ,"Apple" ,"Pair","Pineapple"]
for fruit in fruits:
    print(fruit)
    print(fruit+ " Pie")

```


#### Calculate the average student height from a list of heights. don't use len , sum funtions 

```py 
## Code to input the valuse 
# Input example ->  156 178 165 171 187
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

## average calcutaion code

total_students=0
height_total=0
for height in student_heights:
    height_total += height
    total_students += 1

average_height = round(height_total/total_students)
print(average_height)

#print(height_total)
#print(total_students)
#print(len(student_heights))
#print(sum(student_heights))

```

#### Find the highest score from a List of scores, don't use max function 

```py
## Code to input the valuse 
# Input example ->  78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score=0

for score in student_scores:
  if max_score < score:
    max_score=score

print(f"The highest score in the class is: {max_score}")  

```

### For loop , for number in range(a,b)

```py
for number in range(1,10): # this will out put 1:9 not 10
    print(number)

range(5) #0,1,2,3,4
range(1,11) #1,2,3...10
range(1,11,3) # here 3 is the step , 1,4,7,10

# get sum of 1to100 
total = 0 
for number in range(1,101):
    total += number

```

#### Write a program that calculates the sum of all the even numbers from 1 to 100

```py
#method 1
even_sum=0
for i in range(2,101,2):
    even_sum += i

print(even_sum)

#method 2

even_sum=0
for i in range(1,101):
    if i%2==0:
        even_sum += i

print(even_sum)

```

#### FizzBuzz

<details>
    <summary>Logic:</summary>
    When the number is divisible by 3 then instead of printing the number   it should print "Fizz".<br>
    When the number is divisible by 5, then instead of printing the number  it should print "Buzz".<br>
    And if the number is divisible by both 3 and 5 e.g. 15 then instead of  the number it should print "FizzBuzz"
</details>

```py

for i in range(1,101):
    if i%15 ==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

```


#### Password Generator Project 

```py
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password=""

for i in range(0,nr_letters):
    password+=letters[random.randint(0,len(letters)-1)]

for i in range(0,nr_numbers):
    password+=numbers[random.randint(0,len(numbers)-1)]

for i in range(0,nr_symbols):
    password+=symbols[random.randint(0,len(symbols)-1)]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

##Method 1 

password=[]

for i in range(0,nr_letters):
    password.append(random.choice(letters)) 

for i in range(0,nr_numbers):
    password.append(random.choice(numbers))

for i in range(0,nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

final_password=""
for i in password:
    final_password+=i

print(final_password)


##Method 2 
password=""

length_of_pass = nr_letters+nr_numbers+nr_symbols
count=0
while count<length_of_pass:
    choose = random.randint(1,3)
    if choose == 1 and nr_letters>0:
        password+=letters[random.randint(0,len(letters)-1)]
        count+=1
        nr_letters-=1
    elif choose == 2 and nr_numbers>0:
        password+=numbers[random.randint(0,len(numbers)-1)]
        count+=1
        nr_numbers-=1
    elif choose == 3 and nr_symbols>0:
        password+=symbols[random.randint(0,len(symbols)-1)]
        count+=1
        nr_symbols-=1

print(password)

```