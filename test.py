
# Write a function called missing_numbers that takes a list of sequence of numbers as argument, and finds the missing numbers
# in the sequence. 
# The list above should return: [4, 8, 10, 13, 16, 29, 30]


list_sequence = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31] 

def missing_numbers(sequence  :list )->list:
    return set(range(sequence[0], sequence[-1])).difference(sequence)

print(missing_numbers(list_sequence))

