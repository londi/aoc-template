import os

def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    floor = 0
    for char_index in range(len(input_text)):
        if input_text[char_index] == '(':
            floor += 1
        elif input_text[char_index] == ')':
            floor -= 1
        if floor < 0:
            result = char_index + 1
            break

    return result