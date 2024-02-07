from main import lines


mem = {}


def move(dish, x):
    string = list(list(zip(*dish))[x])
    for i, elem in enumerate(string):
        if elem == 'O':
            while i > 0 and string[i - 1] == '.':
                string[i] = '.'
                string[i - 1] = 'O'
                i -= 1
    return string


def tilt(dish):
    new_lines = []
    for x in range(len(dish[0])):
        new_col = move(dish, x)
        new_lines.append(new_col)
    b = [list(elem) for elem in zip(*new_lines)]
    return b


def count_load(dish):
    total = 0
    for i, line in enumerate(dish[::-1]):
        total += ((i+1) * line.count('O'))
    return total


def p1():
    return count_load(tilt(lines))


def rotate(dish):
    return [list(row) for row in list(zip(*dish[::-1]))]


def cycle(dish):
    for _ in range(4):
        dish = tilt(dish)
        dish = rotate(dish)
    return dish


def p2():
    result = lines
    for i in range(1, 1000000001):
        result = cycle(result)
        token = ''.join([''.join(row) for row in result])
        if token in mem:
            j = (1000000000 - i) % (i - mem[token])
            for m in range(j):
                result = cycle(result)
            return result
        mem[token] = i
    return result


p2_dish = p2()
print(count_load(p2_dish))




















