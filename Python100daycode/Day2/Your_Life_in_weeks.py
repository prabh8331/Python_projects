# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Create a program that tells us how many days, weeks, months we have left if we live until 90 years old.

remaining_age = 90 - int(age)
#print(remaining_age)

days_in_a_year = 365
weeks_in_a_year = 52 
months_in_a_year = 12 

print(f"You have {days_in_a_year*remaining_age} days, {weeks_in_a_year*remaining_age} weeks, and {months_in_a_year*remaining_age} months left.")