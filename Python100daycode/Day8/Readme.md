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


Get the index of the list: <https://www.w3schools.com/python/ref_list_index.asp>

- Breakdown1: Create a encrypt function which takes "text" and "shift" as input. Bug alert: if encode "z" it will give the "IndexError: list index out of range" error
- Breakdown2: Create a decrypt function and when direction is "decode" then call decrypt else if its "encode" call encrypt function 

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            if new_position > 25:
                  multiple=(new_position+1)//26
                  new_position=new_position-26*multiple
            cipher_text+=alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
            position=alphabet.index(letter)
            new_position=position-shift_amount
            if new_position < 0:
                  multiple=(new_position+1)//26
                  new_position=new_position-26*multiple
            plain_text+=alphabet[new_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
      encrypt(text,shift)
elif direction == "decode":
      decrypt(text,shift)
else:
      print("Wrong input!")

```

- Breakdown3: As encrypt and decrypt both are smiler function and logic is matching merge both the above tasks. Create function caesar(), which takes inputs of  'text', 'shift' and 'direction'.

```py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(input_text,shift_amount,which_direction):
    output_text=""
    if which_direction == "decode":
          shift_amount*=-1
    for letter in input_text:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            if new_position > 25 or new_position < 0:
                  multiple=(new_position+1)//26
                  new_position=new_position-26*multiple
            output_text+=alphabet[new_position]
    if which_direction in ["encode","decode"]:
        print(f"The {which_direction}d text is {output_text}")
    else:
        print("Wrong Input, Try again!")

caesar(text,shift,direction)

```

- Breakdown4: Final code
