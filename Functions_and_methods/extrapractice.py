# Write a program that uses a `celsius_to_fahrenheit` function to convert temperatures.
# Ask the user to enter a temperature in Celsius, then output both temperatures.

# Sample output:
# $ python temp_converter.py
# Enter temperature in Celsius: 25
# 25°C = 77°F

def c_to_f(c):
    farenheit_conversion = (c*(9/5))+32
    return farenheit_conversion

def celsius_input(prompt):
    entry = input(prompt)
    return float(entry)

ask_user = celsius_input("What degree Celsius would you like to convert?")

print(f'We converted {ask_user} C to {c_to_f(ask_user)} F')
    