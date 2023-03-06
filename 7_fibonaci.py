#Fibonaccci using recursion 

# Fn = Fn-1 + Fn-2
# Thus, the Fibonacci term in the nth position is equal to the term 
# in the nth minus 1 position plus the term in the nth minus 2 position.


def fib(n):
    """retunt number in Fibonacci sequence"""
    if n <=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
    
n = int(input("Entrt numbrt ot terms: "))
print('Fibonacci sequence:')
for i in range(n):
    print(fib(i))

    

