import os
import re

def main(test_input=False):
    sum = 0
    fileName = 'test_input.txt' if test_input else 'input.txt'
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + fileName, 'r') as input_file:
        
        for line in input_file:
            pass
        
    return sum


if __name__ == '__main__':
    print(main(False))