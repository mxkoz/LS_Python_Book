from pprint import pprint
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for number in my_list:
    if number %2 == 0:
        new_list.append('even')
    if number %2 != 0:
        new_list.append('odd')

pprint(new_list)