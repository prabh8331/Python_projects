print("Welcome to the tip calculator.")
# total = input("What was the total bill? $")
# tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
# people = input("How many people to split the bill? ")

# total_pay = float(total) + float(total)*(float(tip)/100)

# each_bill = round(total_pay/float(people),2)

# print(f"Each person should pay: ${each_bill}")


total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_pay = total + total*(tip/100)
each_bill = round(total_pay/people)
each_bill = '{:.2f}'.format(each_bill)
print(f"Each person should pay: ${each_bill}")

