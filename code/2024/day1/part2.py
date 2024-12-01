
def main(input_text):
    result = 0
    left_list = []
    right_list = []

    for line in input_text.split('\n')[:-1]:
        location_ids = line.split('   ')
        left_list.append(location_ids[0])
        right_list.append(location_ids[1])

    for location_id in left_list:
        result += int(location_id) * right_list.count(location_id)

    return result