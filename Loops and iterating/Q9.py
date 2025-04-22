# Write a function that computes and returns the factorial of a number by using a for or while loop.
# The factorial of a positive integer n, signified by n!, 
# is defined as the product of all integers between 1 and n, inclusive:

# n!	Expansion	Result
# 1!	1	1
# 2!	1 * 2	2
# 3!	1 * 2 * 3	6
# 4!	1 * 2 * 3 * 4	24
# 5!	1 * 2 * 3 * 4 * 5	120
# You may assume that the argument is always a positive integer.


# function should compute and return factorial of a number using a for or while loop
# function parameter is a number
# what's a way to calculate what numbers are needed in a factorial?
    # take 10 for example...
    # need a place to store the output (factorial)

def factorial_cruncher(number):
    counter = 1
    for number in range(number, 1, -1):
        counter = number * counter
    return counter
    
print(factorial_cruncher(25))