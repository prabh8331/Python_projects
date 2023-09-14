
#if else 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller to ride.")


# in python single = is used when we have to do the value Assignment 
# and == used when check equality 

# >  greater than
# <  Less than
# >=  grater than or equal to
# <=  less than or equal to 
# ==  equal to
# !=   Not equal to 


# # nested if else 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#     print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay $7.") 
#   else:
#     print("Please pay $12.")   
# else:
#   print("Sorry, you have to grow taller to ride.")


# ##Multiple ifs 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   photo = input("Do you want Photo? is costs extra $3, y/n ")
#   if age < 12:
#     pay = 5
#   elif age <= 18:
#     pay = 7 
#   else:
#     pay = 12

#   if photo == "y":
#     print(f"pay ${pay+3}")
#   else:
#     print(f"pay {pay}")        
# else:
#   print("Sorry, you have to grow taller to ride.")




##Logical operators --> and   or    not  
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  photo = input("Do you want Photo? is costs extra $3, y/n ")
  if age < 12:
    pay = 5
  elif age <= 18:
    pay = 7 
  elif age >=45 & age <= 55:
    pay = 0
  else:
    pay = 12
    
  if photo == "y":
    print(f"pay ${pay+3}")
  else:
    print(f"pay {pay}")        
else:
  print("Sorry, you have to grow taller to ride.")
