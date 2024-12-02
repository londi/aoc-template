import os
import re

def main(test_input=False):
    sum = 0
    fileName = 'test_input.txt' if test_input else 'input.txt'
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + fileName, 'r') as input_file:
        left_list = []
        right_list = []
        for line in input_file:
            elements = line.replace("\n", "").split("   ")
            # print(elements)
            left_list.append(elements[0])
            right_list.append(elements[1])
        left_list.sort()
        right_list.sort()

    while len(left_list) > 0:
        sum = sum + abs(int(left_list.pop(0)) - int(right_list.pop(0)))

    return sum


if __name__ == '__main__':
    print(main(False))