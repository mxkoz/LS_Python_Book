def multiply (number1, number2):
    return(number1 * number2)

def get_number(prompt):
    entry = input(prompt)
    return (float(entry))

first_number = get_number("Enter the first number: ")
second_number = get_number("Enter the second number: ")

product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')