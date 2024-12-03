import os
import re
import sys
from pyparsing import Word, alphas, nums, Suppress, Group, delimitedList, Literal, oneOf, Optional


def main(test_input=False):
    sum = 0
    fileName = 'test_input.txt' if test_input else 'input.txt'
    
    allowed_keywords = oneOf("mul do don't")
    token = Word(alphas)
    lparen = Suppress("(")
    rparen = Suppress(")")
    number = Word(nums)
    two_numbers = Group(number + Suppress(",") + number)
    optional_values = Optional(two_numbers)
    token_pattern = allowed_keywords + lparen + optional_values + rparen


    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + fileName, 'r') as input_file:
        enabled = True
        for line in input_file:
            results = token_pattern.searchString(line)
            for r in results:
                # print(r)
                token = r[0]
                if token == 'do':
                    enabled = True
                elif token == "don't":
                    enabled = False
                elif enabled:
                    sum = sum + calc_mul(r[1])
        
    return sum

def calc_mul(elements):
    # print(elements)
    return int(elements[0]) * int(elements[1])



if __name__ == '__main__':
    test = len(sys.argv) > 1 and sys.argv[1] == 't'
    print(main(test))
    # too high 114961848
    # 106780429 is right