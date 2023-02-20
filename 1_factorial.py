# This is simple factorial calculator
# The factorial function gives the number of possible arrangements of a set of items of length "n"
# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# etc.
# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1



# Function returns the value of the factorial of num if it is defined, otherwise, print enter integer number

def factorial(num):
    fact =1
    if type(num) is not int:    
        print("Please enter integer number")
    elif num<0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num ==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print("The factorial of",num,"is",fact)

        
num = int(input("Enter a number: "))
factorial(num)


# Similar function ca be done using recursion 


# def factorial(num):
#     if type(num) is not int:
#         return None
#     if num < 0:
#         return None
#     if num == 0:
#         return 1
    
#     return num * factorial(num - 1)