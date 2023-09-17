#method 1
even_sum=0
for i in range(2,101,2):
    even_sum += i

print(even_sum)

#method 2

even_sum=0
for i in range(1,101):
    if i%2==0:
        even_sum += i

print(even_sum)