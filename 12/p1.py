from main import lines
from functools import lru_cache


def valid(code, key):
    variant = []
    counter = 0
    for c in code:
        if c == '#':
            counter += 1
        if c == '.' and counter > 0:
            variant.append(counter)
            counter = 0
    if counter > 0:
        variant.append(counter)
    return variant == key


def decrypt(code_key: tuple, cache=None) -> int:
    if cache is None:
        cache = {}
    code, key = code_key
    token = ''.join(code) + ''.join(map(str, key))
    if token in cache:
        return cache[token]
    if '?' not in code:
        return 1 if valid(code, key) else 0
    i = code.index('?')
    code[i] = '#'
    a = decrypt((code, key), cache)
    code[i] = '.'
    b = decrypt((code, key), cache)
    code[i] = '?'
    result = a + b
    cache[token] = result
    return result


counter = 0
for line in lines:
    code = list(line.split()[0])
    key = list(map(lambda x: int(x), line.split()[1].split(',')))
    counter += decrypt((code, key))












