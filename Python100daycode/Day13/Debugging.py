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
