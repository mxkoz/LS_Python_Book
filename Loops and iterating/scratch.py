names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)

numbers = [1,2,3]
numbers_2 = numbers
print(id(numbers))
print(id(numbers_2))