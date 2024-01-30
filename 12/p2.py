from main import lines
import re

total = 0
mem = {}


def decode(c: list) -> list:
    k = []
    counter = 0
    for elem in c:
        if elem == '#':
            counter += 1
        if elem == '.' and counter > 0:
            k.append(counter)
            counter = 0
    if counter > 0:
        k.append(counter)
    return k


def simplify(s: list) -> list:
    return list(re.sub(r'\.{2,}', '.', ''.join(s)))


def check_mem(c, k):
    s = ''.join(simplify(c))
    if s not in mem:
        mem[s] = count(c, k)
    return mem[s]


def count(c, k):
    if '?' not in c:
        return 1 if decode(c) == k else 0
    i = c.index('?')
    interval = c[: i]
    if i > 1 and '.' in interval:
        last_dot = [idx for idx, d in enumerate(interval) if d == '.'][-1]
        to_check = decode(c[: last_dot])
        if to_check != key[: len(to_check)]:
            return 0
    c[i] = '.'
    a = check_mem(simplify(c), k)
    c[i] = '#'
    b = check_mem(simplify(c), k)
    c[i] = '?'
    return a + b


for line in lines:
    mem = {}
    code = simplify(list('?'.join([line.split()[0]] * 5)))
    key = list(map(int, line.split()[1].split(',') * 5))
    arrangements = check_mem(code, key)
    total += arrangements
print(total)








