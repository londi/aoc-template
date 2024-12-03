import os
import re
import sys
from pyparsing import Word, alphas, nums, Suppress, Group, delimitedList, Literal, oneOf


def main(test_input=False):
    sum = 0
    fileName = 'test_input.txt' if test_input else 'input.txt'
    
    allowed_keywords = oneOf("mul do_not_mul")
    token = Word(alphas)
    lparen = Suppress("(")
    rparen = Suppress(")")
    number = Word(nums)
    two_numbers = Group(number + Suppress(",") + number)
    token_pattern = allowed_keywords + lparen + two_numbers + rparen


    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + fileName, 'r') as input_file:
        for line in input_file:
            results = token_pattern.searchString(line)
            for r in results:
                sum = sum + calc_mul(r[1])
        
    return sum

def calc_mul(elements):
    print(elements)
    return int(elements[0]) * int(elements[1])


if __name__ == '__main__':
    test = len(sys.argv) > 1 and sys.argv[1] == 't'
    print(main(test))
    # 225858867 too high
    # 196826776 is right