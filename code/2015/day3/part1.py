import os

def main():

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    current_house = [0, 0]
    visited_houses = [[0, 0]]

    for direction in input_text:
        if direction == '^':
            current_house[1] += 1
        elif direction == 'v':
            current_house[1] -= 1
        elif direction == '>':
            current_house[0] += 1
        elif direction == '<':
            current_house[0] -= 1
        if not current_house in visited_houses:
            visited_houses.append([current_house[0], current_house[1]])

    return len(visited_houses)