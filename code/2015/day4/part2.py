import hashlib
import os

def main():
    result = 0

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read().replace('\n', '')

    while True:
        if hashlib.md5((input_text + str(result)).encode()).hexdigest()[:6] == '000000':
            break
        result += 1

    return result