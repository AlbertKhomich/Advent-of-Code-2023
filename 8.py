from main import lines
import math


def write_route(input_data):

    def decode(m):
        if m == 'L':
            return 0
        else:
            return 1

    navigation_map = [direction for direction in input_data[0]]
    decoded_map = list(map(decode, navigation_map))
    return decoded_map


def write_map(input_data):

    def make_destination(string_destination):
        arr_destination = [string_destination[1:4], string_destination[6: 9]]
        return arr_destination

    result = {d.split(' = ')[0]: make_destination(d.split(' = ')[1]) for d in input_data[2:]}
    return result


my_route = write_route(lines)
my_map = write_map(lines)


def move_p1():
    steps = 0
    current_point = 'AAA'
    destination = "ZZZ"
    while destination != current_point:
        for d in my_route:
            steps += 1
            current_point = my_map[current_point][d]
            if current_point == 'ZZZ':
                return steps


def move_p2():
    steps = []
    for k, v in my_map.items():
        if k[2] == 'A':
            current_position = k
            s = 0
            while current_position[2] != 'Z':
                for d in my_route:
                    s += 1
                    current_position = my_map[current_position][d]
                    if current_position[2] == 'Z':
                        steps.append(s)
                        break
    return math.lcm(*steps)


print(move_p2())



