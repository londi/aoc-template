import os
import string


def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    words = input_text.split('\n')[:-1]

    for word in words:
        nice = True
        if (any([naughty_string in word for naughty_string in ['ab', 'cd', 'pq', 'xy']]) or
                not any([double_letter in word for double_letter
                         in [letter + letter for letter in list(string.ascii_lowercase)]]) or
                not sum([word.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u']]) > 2):
            nice = False
        if nice:
            result += 1

    return result