# Converting Hexadecimal to Decimal
# Hexadecimal or base 16 uses all of the numbers 0 - 9, plus a few others to signify higher numbers:


hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    
    if len(hexNum) == 2:
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
    
    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]]
 #number input   
num = input("Enter a number: ")
print (f"Hexadecimal {num} in decimal is {hexToDec(num)}")

#     # Another solution!

# def hexToDec(hexNum):
#     for char in hexNum:
#         if char not in hexNumbers:
#             return None
    
#     exponent = 0
#     decimalValue = 0
#     for char in hexNum[::-1]:
#         decimalValue = decimalValue + hexNumbers[char] * (16**exponent)
#         exponent = exponent + 1
    
#     return decimalValue