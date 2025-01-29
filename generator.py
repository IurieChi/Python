def gen(): # simple generator function
    yield 1
    
# Generator gen() is an iterator: (dir() method)
print(dir(gen())) # __iter__ and __next__ are presented 

print(gen) # Outputs: <function __main__.gen()>
print(gen()) # Outputs: <generator object gen at 0x000001B945AAA7B0>
print((1 for _ in [])) # Outputs: <generator object <genexpr> at 0x000001B945AAA0B0>

def recurrent_sequence(a1: int, a2: int):
    while True:
        yield a1
        a1, a2 = a2, a1 + a2

# fib is an generator iterator that produce fibonacci sequence:
fib = recurrent_sequence(0, 1)
for i, f in zip(range(1, 20), fib):
    print(f"{i} - {f}", end="; ")



# Yield from
# yield from is an expression that can pass the execution, send() and throw() calls to another generator.
# Generator function chain() that "flattens" iterable objects passed to it:
def chain(*iterables):
    for iterable in iterables:
        yield from iterable

print(list(chain([1, 2], ("4", "5"), {"key1": "val1", "key2": "val2"}, "iter")))
# Outputs: [1, 2, '4', '5', 'key1', 'key2', 'i', 't', 'e', 'r']

# Another example is Sieve of Eratosthenes.
# Algorithm:
# Create a list of integers from 2 to n: (2, 3, 4, …, n). 
# Assign 2 to p (as 2 is the smallest prime number). 
# Mark all numbers that are divisible by p (the p itself should not be marked). 
# Find the smallest number in the list greater than p that is not marked. 
# If there was no such number, stop. Otherwise, assign this number (the next prime number) to p, and repeat from step 3. 
# The numbers remaining not marked in the list are all the primes below n. 

# natural_numbers() function returns a generator that simply produce natural numbers (step 1). 
# sieve() function implements the rest of the algorithm above (2-5 steps):

def natural_numbers(start=1): 
    while True: 
        yield start 
        start += 1 

for _, number in zip(range(10), natural_numbers(1)): 
    print(number, end=" ") # Outputs: 1 2 3 4 5 6 7 8 9 10 


def sieve(numbers): 
    prime = next(numbers) 
    yield prime 
    yield from sieve(p for p in numbers if p % prime != 0) 

for _, prime in zip(range(10), sieve(natural_numbers(2))): 
    print(prime, end=" ") # Outputs: 2 3 5 7 11 13 17 19 23 29 
    
# Lazy evaluations
# Some methods allow lazy evaluation strategy. It means that an expression is
#not evaluated until its value is needed. For example, there is no need to wrap generator expression
#(i for i in range(n)) into a list and keep all the values in memory to sum these values.
# More examples:

n = 10**7
sum([i for i in range(n)]) # keep all values in memory
sum(i for i in range(n)) # keep only the result and the next value from generator

sum(list(map(lambda x: x**2, [i for i in range(n)])))
sum(map(lambda x: x**2, [i for i in range(n)]))
print(sum(map(lambda x: x**2, (i for i in range(n))))) # the best way!
