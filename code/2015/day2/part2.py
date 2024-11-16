import os

def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    for line in input_text.split('\n')[:-1]:
        dimensions = sorted([int(e) for e in line.split('x')])
        result += dimensions[0] * dimensions[1] * dimensions[2] + 2 * dimensions[0] + 2 * dimensions[1]

    return result