#Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.


my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

item = 0
member = 0
new_list = []
while item < len(my_list):
    while member < len(my_list[item]):
        number = my_list[item][member]
        if number % 2 == 0:
            print(number)
        member += 1
    item += 1

print(new_list)