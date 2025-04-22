my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

# Write a comprehension that creates a dict object whose keys are strings and 
# whose values are the length of the corresponding key. Only keys with odd lengths
#  should be in the dict. Use the set given by my_set as the source of strings.


def dict_generator(set):
    return {key: len(key) for key in set if (len(key) % 2 != 0)}

new_dict = dict_generator(my_set)
print(new_dict)