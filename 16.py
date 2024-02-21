from main import lines
import sys

sys.setrecursionlimit(3000)

data = [list(x) for x in lines]
total_light = 0
light_cords = set()
mem = []


def draw():
    for line in data:
        print(''.join(line))
    print()


def move(x=0, y=0, direction='>'):
    global light_cords, mem

    if x == len(data[0]) or x < 0 or y == len(data) or y < 0:
        return 1

    light_cords.add((x, y))

    token = f'{str(x)}x{str(y)}y{direction}'
    if token in mem:
        return 1
    mem.append(token)

    curr_pos = data[y][x]

    if curr_pos == '.':
        data[y][x] = direction
    elif curr_pos == '|':
        if direction == '^':
            return move(x, y-1, direction)
        elif direction == 'v':
            return move(x, y+1, direction)
        elif direction in '><':
            a = move(x, y-1, '^')
            b = move(x, y+1, 'v')
            return a + b
    elif curr_pos == '-':
        if direction == '>':
            return move(x+1, y, direction)
        elif direction == '<':
            return move(x-1, y, direction)
        elif direction in 'v^':
            a = move(x+1, y, '>')
            b = move(x-1, y, '<')
            return a + b
    elif curr_pos == '\\':
        if direction == '>':
            return move(x, y+1, 'v')
        elif direction == '^':
            return move(x-1, y, '<')
        elif direction == 'v':
            return move(x+1, y, '>')
        elif direction == '<':
            return move(x, y-1, '^')
    elif curr_pos == '/':
        if direction == 'v':
            return move(x-1, y, '<')
        elif direction == '>':
            return move(x, y-1, '^')
        elif direction == '^':
            return move(x+1, y, '>')
        elif direction == '<':
            return move(x, y+1, 'v')

    if direction == '>':
        x += 1
    elif direction == 'v':
        y += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y -= 1

    return move(x, y, direction)


def p1():
    move()
    draw()
    result = len(light_cords)
    return result


def clean_data():
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in '<>^v':
                data[y][x] = '.'
    return 1


def check_mult(x1, y1, x2, y2, direction):
    global light_cords, data
    light_power = 0
    for m in range(y1, y2):
        for n in range(x1, x2):
            move(n, m, direction)
            light_p = len(light_cords)
            if light_p > light_power:
                light_power = light_p
            light_cords = set()
            clean_data()

    return light_power


def p2():
    len_y = len(data)
    len_x = len(data[0])

    a = check_mult(0, 0, len_x, 1, 'v')
    b = check_mult(0, len_y-1, len_x, len_y, '^')
    c = check_mult(0, 0, 1, len_y, '>')
    d = check_mult(len_x-1, 0, len_x, len_y, '<')

    return max(a, b, c, d)


print(p2())
