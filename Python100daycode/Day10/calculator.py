from art import logo
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
  print(logo)
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
      

calculator()