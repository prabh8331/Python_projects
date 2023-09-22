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