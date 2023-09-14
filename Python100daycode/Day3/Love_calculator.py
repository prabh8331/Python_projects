# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

L1=name1.count("l")
O1=name1.count("o")
V1=name1.count("v")
E1=name1.count("e")

T1=name1.count("t")
R1=name1.count("r")
U1=name1.count("u")
E1=name1.count("e")



L2=name2.count("l")
O2=name2.count("o")
V2=name2.count("v")
E2=name2.count("e")

T2=name2.count("t")
R2=name2.count("r")
U2=name2.count("u")
E2=name2.count("e")

S1= L1+O1+V1+E1+L2+O2+V2+E2
S2= T1+R1+U1+E1+T2+R2+U2+E2

score = int(str(S2)+str(S1))

if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print (f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
