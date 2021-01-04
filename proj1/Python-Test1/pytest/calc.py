from math import ceil, floor
from time import sleep
def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

print("module imported")


def is_palindrome(input):
    input = str.strip(input)
    if input ==  "":
        return True
    elif len(input)%2 == 1:
        if input[:len(input)%2] == input[((len(input)%2)+1):]:
            return True
    elif len(input)%2 == 0:
        if input[:len(input) % 2] == input[(len(input) % 2):]:
            return True
    else:
        return False

def is_palindrome(input):
    sleep(1)
    input = input.replace(" ","")

    if input ==  "":
        return True
    elif len(input) == 1:
        return True
    else:
        x = list(z.lower() for z in input[:floor(len(input) / 2)])
        y = list(z.lower() for z in input[ceil(len(input) / 2):])
        if x == y[::-1]:
            return True
        else:
            return False

