
def main(input_text):
    result = 0
    left_list = []
    right_list = []

    for line in input_text.split('\n')[:-1]:
        location_ids = line.split('   ')
        left_list.append(location_ids[0])
        right_list.append(location_ids[1])

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        result += abs(int(left_list[i]) - int(right_list[i]))

    return result