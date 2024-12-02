
def main(input_text):
    result = 0

    for line in input_text.split('\n')[:-1]:
        levels = [int(level) for level in line.split(' ')]
        if levels[0] < levels[1]:
            levels.reverse()
        safe = True
        for i in range(len(levels) - 1):
            if levels[i] - levels[i + 1] > 3 or levels[i] - levels[i + 1] < 1:
                safe = False
        if safe:
            result += 1

    return result
