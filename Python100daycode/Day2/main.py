#print(len(12345))
#    print(len(12345))
#          ^^^^^^^^^^
#TypeError: object of type 'int' has no len()

#Data Types 

#Sting 

print("Hello"[0])

'Hello'[1]

print("123" + "345")

#Interger 

print(123+345)

print(123_123 + 1 + 1_1_1)

#Float 

3.13412

print(312_232.4232_32)

#Boolen 
True
False



#num_char = len(input("what is you name"))
num_char = 5
type(num_char)
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print (70+float("100.5"))

print(str(70)+str(1010))

print(int)


#Mathematical Operations 
3 + 5
7 - 4
3 * 2 
6 / 3 
2 ** 2

#Priorty order by (PEMDAS + Left to Right) 
#Parentheses ()
#Exponents **
#Multipliacation * and Division /
#Addition + and SUbtraction - 

print(3*3+3/3-3)

#what chnage you could make in above problem so that ans is 3 not 7 
print(3*(3+3)/3-3)


print(8/3)  # its output will be float
print(round(8/3))

print(round(8/3,2))

print (8//3) # its output will be int


result = 4/2
print(result)
#result = result / 2 --> another way of doing this is 
result /= 2
print(result)


score = 0 
score += 1
score = score + 1
print(score)

score *= 2
print(score)

score /= 2
print(score)

score -= 2
print(score)

score += 10 
heigh = 1.8
isWinning = True

#print("your score is" + score) # this will throw error TypeError  

#f-String
print(f"Your score is {score}, your height is {heigh}, you are winning is {isWinning}")
# we put f in frount of string quotes f"" and use curly brackets {variable} to put variable 

print(.1+.1+.1  == .3)  # False
print(round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1)) # False 
print(round(.1 + .1 + .1, 10) == round(.3, 10)) # True

# print(150 * 1.12)
# ans of above should be just 168 but its output is 168.00000000000003 this is how python works 
#why --> 

# Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. 
# For example, the decimal fraction 0.125 has value 1/10 + 2/100 + 5/1000, 
# and in the same way the binary fraction 0.001 has value 0/2 + 0/4 + 1/8. 
# These two fractions have identical values, the only real difference being that 
# the first is written in base 10 fractional notation, and the second in base 2.

