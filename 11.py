from main import lines
import numpy as np

coordinates_empty_space = {'x': [], 'y': []}
SCALE_SPACE = 999999


def expand_universe(array):
    new_space = []
    for line in array:
        new_space.append(list(line))
        if '#' not in line:
            new_space.append(list(line))
    return new_space


def collect_universes(space):
    coordinates_universes = {}
    counter_universes = 0

    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] == '#':
                counter_universes += 1
                coordinates_universes[counter_universes] = (x, y)

    return coordinates_universes


def rotate_space(space):
    space = np.array(space)
    rotated_new_space = np.rot90(space, k=-1)

    return rotated_new_space


def find_empty_space(address, space):
    for i in range(len(space)):
        if '#' not in space[i]:
            coordinates_empty_space[address].append(i)


def calculate_small_path(first_universe_x, second_universe_x, first_universe_y, second_universe_y):
    current_path = abs(first_universe_x - second_universe_x) + abs(first_universe_y - second_universe_y)

    return current_path


def calc_factor(x1, x2, coord: str):
    factor = len([m for m in range(min(x1, x2)+1, max(x1, x2)) if m in coordinates_empty_space[coord]])

    return factor


def calculate_large_path(first_universe_x, second_universe_x, first_universe_y, second_universe_y):
    x_factor = calc_factor(first_universe_x, second_universe_x, 'x')
    y_factor = calc_factor(first_universe_y, second_universe_y, 'y')
    path = ((SCALE_SPACE * x_factor) +
            (SCALE_SPACE * y_factor) +
            calculate_small_path(first_universe_x, second_universe_x, first_universe_y, second_universe_y))

    return path


def calculate_paths(coordinates_universes, calc_method):
    sum_path = 0

    last_universe = list(coordinates_universes.keys())[-1]
    for i in range(1, last_universe + 1):
        first_universe_x = coordinates_universes[i][0]
        first_universe_y = coordinates_universes[i][1]
        for j in range(i + 1, last_universe + 1):
            second_universe_x = coordinates_universes[j][0]
            second_universe_y = coordinates_universes[j][1]
            current_path = calc_method(first_universe_x, second_universe_x, first_universe_y, second_universe_y)
            sum_path += current_path

    return sum_path


def solve_part_1():

    # prepare expanded space
    expanded_space = expand_universe(lines)
    rotated_new_space = rotate_space(expanded_space)
    expanded_space = expand_universe(rotated_new_space)

    # collect universes coordinates in dictionary {1: (4, 0), 2: (9, 1), 3: (0, 2), ...}
    coordinates_universes = collect_universes(expanded_space)

    # calculate all paths between unique pairs and sum it: 1 and [2: 9], 2 and [3: 9] ...
    sum_path = calculate_paths(coordinates_universes, calculate_small_path)

    return sum_path


def solve_part2():

    # collect all universes in dict
    coordinates_universes = collect_universes(lines)

    # find coordinates of all empty spaces {x: [], y: []}
    find_empty_space('y', lines)
    rotated_space = rotate_space([list(s) for s in lines])
    find_empty_space('x', rotated_space)

    # calculate all paths
    paths_sum = calculate_paths(coordinates_universes, calculate_large_path)

    return paths_sum


result = solve_part2()
print(result)





