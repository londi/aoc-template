
def main(input_text):
    result = 0
    for line in input_text.split('\n')[:-1]:
        levels = [int(level) for level in line.split(' ')]
        report_checks = [check_report(levels)]
        index = 0
        while index < len(levels):
            report_checks.append(check_report(levels[:index] + levels[index + 1:]))
            if any(report_checks):
                result += 1
                break
            index += 1
    return result


def check_report(levels):
    if levels[0] < levels[1]:
        levels.reverse()
    for i in range(len(levels) - 1):
        if levels[i] - levels[i + 1] > 3 or levels[i] - levels[i + 1] < 1:
            print(levels)
            print(levels[i], levels[i + 1])
            return False
    return True
