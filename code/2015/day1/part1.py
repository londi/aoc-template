import os

def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    for char in input_text:
        if char == '(':
            result += 1
        elif char == ')':
            result -= 1

    return result