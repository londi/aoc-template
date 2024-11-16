import os
import string

ALPHABET_LIST = list(string.ascii_lowercase)

def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    words = input_text.split('\n')[:-1]

    letter_constructs = []
    for letter1 in ALPHABET_LIST:
        for letter2 in ALPHABET_LIST:
            letter_constructs.append(letter1 + letter2)

    letter_constructs_1 = []
    for letter1 in ALPHABET_LIST:
        for letter2 in ALPHABET_LIST:
            letter_constructs_1.append(letter1 + letter2 + letter1)

    for word in words:
        if any([word.count(letter_construct) > 1 for letter_construct in letter_constructs]) and any([word.count(letter_construct) == 1 for letter_construct in letter_constructs_1]):
            result += 1

    return result