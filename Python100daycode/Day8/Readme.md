### Caesar Cipher 
<details>
    <summary> Caesar Cipher: </summary>
    The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”.
</details>

#### Functions with Inputs

```py
# Create a function called greet(). 
# Write 3 print statements inside the function.
def greet(name) :
    print(f"Hello {name}")
    print(f"How are you doing {name}?")
    print(f"Bye! {name}")

# Call the greet() function and run your code.

greet("Prabh")

```

Arguments & Parameter 
In above example name is `Parameter` 
And when we call greet function with "Prabh" this "Prabh" is `Argument`

Parameter is the name of variable which is passed in 
and Argument is the actual value 

so basically in above use case first we are creating a variable called name and we are assigning it a value of "Prabh" (name="Prabh")

#### Function with more than 1 inputs 
```py
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Prabh","Panjab")
#Positional Arguments, Position of these Parameters matter

### Function with Keyword Argument - here position can alter 
greet_with(location="Panjab", name="Singh")
```

#### Paint the wall 

<details>
    <summary> Instructions: </summary>
    You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

    number of cans = (wall height x wall width) ÷ coverage per can.
</details>

```py

# Define a function called paint_calc() so that the code below works.   
import math

def paint_calc (height, width, cover):
    number_of_cans= math.ceil((height*width)/cover)
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

```

#### Find all the prime numbers till the given numbers   
```py
def prime_numbers(number):
    prime=[]
    numbers=[]
    numbers.append(1)
    prime_current=2
    for j in range(2,number+1):
        if j not in numbers:
            prime.append(j)
            prime_current=j
            i=prime_current
            while i <= number:
                i+=prime_current
                if i not in numbers and i<=number:
                    numbers.append(i)
    print(prime)

n = int(input("Find the Prime numbers till: "))
prime_numbers(number=n)
```

### optimized version of the prime numbers calculate 
link of the algo: <https://www.geeksforgeeks.org/sieve-of-eratosthenes/>
```py
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
    
    for number in range(2, limit + 1):
        if is_prime[number]:
            primes.append(number)
    
    return primes

def prime_numbers(number):
    if number < 2:
        return []
    
    primes = sieve_of_eratosthenes(number)
    print(primes)

n = int(input("Find the Prime numbers till: "))
prime_numbers(number=n)


```


#### Check if given number is prime number 
```py

#Write your code below this line 👇

def prime_checker(number):
  prime=True
  for i in range(2, round(number/2)):
    if number % i == 0:
      prime=False
  
  if prime == True:
    print("It's a prime number.")
  else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


```
