import os

def main():

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt', 'r') as input_file:
        input_text = input_file.read()

    santa_current_house = [0, 0]
    robo_santa_current_house = [0, 0]
    visited_houses = [[0, 0]]

    santa_move = True
    for direction in input_text:
        if santa_move:
            if direction == '^':
                santa_current_house[1] += 1
            elif direction == 'v':
                santa_current_house[1] -= 1
            elif direction == '>':
                santa_current_house[0] += 1
            elif direction == '<':
                santa_current_house[0] -= 1
            if not santa_current_house in visited_houses:
                visited_houses.append([santa_current_house[0], santa_current_house[1]])
        else:
            if direction == '^':
                robo_santa_current_house[1] += 1
            elif direction == 'v':
                robo_santa_current_house[1] -= 1
            elif direction == '>':
                robo_santa_current_house[0] += 1
            elif direction == '<':
                robo_santa_current_house[0] -= 1
            if not robo_santa_current_house in visited_houses:
                visited_houses.append([robo_santa_current_house[0], robo_santa_current_house[1]])
        santa_move = not santa_move

    return len(visited_houses)