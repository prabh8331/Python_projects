
#### Calculator project 

##add
def add(n1,n2):
    return n1+n2

##subtract
def subtract(n1,n2):
    return n1-n2

##multiply
def multiply(n1,n2):
    return n1*n2

##divide
def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))

  for operation in operations:
    print(operation)

  should_continue=True

  while should_continue==True:

    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    calculation_function=operations[operation_symbol]

    answer=calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() =="y":
        num1=answer
    else:
        should_continue=False
        calculator()
      


## Infinite loop warning for recursive functions - there should be some sort of condition which should met to call/exit from recursive function 

#Recursion functions , a recursive function is a function that calls itself e.g. 


def factorial(n):
    # Base case: If n is 0 or 1, return 1.
    if n == 0 or n == 1:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1).
    else:
        return n * factorial(n-1)

  
