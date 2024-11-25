
def main(input_text):
    result = 0

    light_grid = [[False for _ in range(1000)] for _ in range(1000)]

    for line in input_text.split('\n'):
        line_split = line.split(' ')
        if 'toggle' in line:
            start_coords = [int(coord) for coord in line_split[1].split(',')]
            end_coords = [int(coord) for coord in line_split[3].split(',')]
            for x in range(start_coords[0], end_coords[0] + 1):
                for y in range(start_coords[1], end_coords[1] + 1):
                    light_grid[y][x] = not light_grid[y][x]
        elif 'turn on' in line:
            start_coords = [int(coord) for coord in line_split[2].split(',')]
            end_coords = [int(coord) for coord in line_split[4].split(',')]
            for x in range(start_coords[0], end_coords[0] + 1):
                for y in range(start_coords[1], end_coords[1] + 1):
                    light_grid[y][x] = True
        elif 'turn off' in line:
            start_coords = [int(coord) for coord in line_split[2].split(',')]
            end_coords = [int(coord) for coord in line_split[4].split(',')]
            for x in range(start_coords[0], end_coords[0] + 1):
                for y in range(start_coords[1], end_coords[1] + 1):
                    light_grid[y][x] = False

    for line in light_grid:
        for light in line:
            if light:
                result += 1

    return result
