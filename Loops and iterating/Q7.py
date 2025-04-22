#Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# Original answer commented out – used a for loop, which worked, but wasn't as efficient!
# def find_integers(tuple):
#     integer_list = []
#     for item in tuple:
#         if type(item) is int:
#             integer_list.append(item)
#     return integer_list

# integers = find_integers(my_tuple)
# print(integers)                  

def find_integers(things):
    return [element for element in things if type(element is int)]

