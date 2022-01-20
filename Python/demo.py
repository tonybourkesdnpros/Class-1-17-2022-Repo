
import yaml

    # # Variables

    # # Simple Variables

    # # Integers

    # i = 1

    # #print(i)

    # # Strings

    # z = '192.168.1.10'
    # x = 'spine1-dc1'

# Booleans

n = True
m = False

# Complex Variables

# List

band = ['John', 'Paul', 'George', 'Ringo']

prime = [3, 5, 7, 11, 13, 17, 19, 23]

# for member in band:
#     print("A member of the Beetles is:", member)

# print("")
# print("Here is a list of prime numbers")

# for number in prime:
#     print(number)

# Dictionaries

file = open('obvious.yml', 'r')

obvious = yaml.safe_load(file)

# for key, value in obvious.items():
#     print("The key is", key, 'and the value is', value)

# Functions

def add_num(x, y):
    z = x + y
    return z

result = add_num(5, 10)

print(result)
    





