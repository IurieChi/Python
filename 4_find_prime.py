#Find Prime number
# Prime Finding
# Write a function that returns a list of all primes up to a given number.
# For each number, in order to determine if it is prime, take the following steps:
# Find the square root of the number
# Find all the primes up to that square root
# Test to see if any of those primes are divisors
# If a number has no prime divisors, it is prime!


# type number
num = int(input("Please provide number: "))
# function 
def primesUpTo(num):
    primes = [2]
    for number in range(3,num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor ==0:
                #not prime
                break
            if factor > sqrtNum:
                #it's prime
                primes.append(number)
                break
    return primes
print(primesUpTo(num))



