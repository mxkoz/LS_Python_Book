#Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
#The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

original_tuple = (1,2,3,4,5)
reversed_tuple = tuple(reversed(original_tuple))
trimmed_and_reversed = reversed_tuple[1:len(reversed_tuple)-1]
print(trimmed_and_reversed)

+ reversed_tuple = tuple(reversed(original_tuple))
+ trimmed_and_reversed = reversed_tuple[1:len(reversed_tuple)-1]
