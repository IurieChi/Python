#Find Prime number
# Prime Finding
# Write a function that returns a list of all primes up to a given number.
# For each number, in order to determine if it is prime, take the following steps:
# Find the square root of the number
# Find all the primes up to that square root
# Test to see if any of those primes are divisors
# If a number has no prime divisors, it is prime!


# type number
number = int(input("Please provide number: "))
# function 
def primesUpTo(number):
    primes = [2]
    for numberr in range(3,number):
        sqrtNum = numberr ** 0.5
        for factor in primes:
            if numberr % factor ==0:
                #not prime
                break
            if factor > sqrtNum:
                #it's prime
                primes.append(numberr)
                break
    return primes
print(primesUpTo(number))


# find a prime number till 20

def is_prime(num):
   for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
        return True

def test():
    for i in range(1, 20):
        if is_prime(i + 1):
            print(i + 1, end=" ")
    print()


test()


