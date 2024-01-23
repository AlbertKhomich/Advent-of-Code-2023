from main import lines
import numpy as np


def expand_universe(array):
    new_space = []
    for line in array:
        new_space.append(list(line))
        if '#' not in line:
            new_space.append(list(line))
    return new_space


def solve_part_1():
    # prepare expanded space
    new_space = np.array(expand_universe(lines))
    rotated_new_space = np.rot90(new_space)
    new_space = expand_universe(rotated_new_space)

    # collect universes coordinates in dictionary {1: (4, 0), 2: (9, 1), 3: (0, 2), ...}

    # calculate all paths between unique pairs and sum it: 1 and [2: 9], 2 and [3: 9] ...

    # find the shortest path


solve_part_1()







