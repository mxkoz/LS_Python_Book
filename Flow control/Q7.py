#Write a function that takes a single integer argument and prints a message that describes whether:

#the value is between 0 and 50 (inclusive)
#the value is between 51 and 100 (inclusive)
#the value is greater than 100
#the value is less than 0

def describe_the_integer(integer):
    if integer >= 0 and integer <= 50:
        print("This value is between 0 and 50")
    elif integer >50 and integer <= 100:
        print("This value is between 51 and 100")
    elif integer >100:
        print("This value is greater than 100")
    else:
        print("This value is less than 0")

describe_the_integer(-1)
describe_the_integer(104)
describe_the_integer(42)