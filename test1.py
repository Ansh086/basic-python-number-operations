import random
n = random.randint(1,15)

def guessfunc():
    return int(input("guess the number: "))
def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
def fibonacci(n):
    if n<=1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


#number guessing
for i in range(5):
    guess = guessfunc()
    if guess==n:
        print("correct!")
        break
    else:    
        print(f"wrong...number is {'higher' if guess<n else 'lower'}....{str(4-i)} turns left")
print(f"number was {n}")

#tell if fibonacci
fib = input("would you like to see the fibonacci sequence of this number?)(y/n): ")
if fib == ('y' or 'Y'):
    for i in range(n):
        print(fibonacci(i),end=" ")
elif fib == ('n' or 'N'):
    pass
else:
    print("\ninvalid input")
print()

#tell if prime
prime = input("would you like to see if the number is prime or not?)(y/n): ")
if prime == ('y' or 'Y'):
    print("number is prime " if isprime(n) else "number is not prime ")
elif prime == ('n' or 'N'):
    pass
else:
    print("\ninvalid input")

#tells the multiplication table
multi_t = input("would you like to see the multiplication table of the number?)(y/n): ")
if multi_t == ('y' or 'Y'):
    for i in range(10):
        print(f"{n} * {i+1} = {n*(i+1)}")
elif multi_t == ('n' or 'N'):
    pass
else:
    print("\ninvalid input")

#tell factorial
facto = input("would you like to see the factorial of the number?)(y/n): ")
if facto == ('y' or 'Y'):
    print(fact(n))
elif facto == ('n' or 'N'):
    pass
else:
    print("\ninvalid input")
