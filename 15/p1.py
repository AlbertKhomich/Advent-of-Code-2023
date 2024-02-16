from main import lines


inp = lines[0].split(',')
hash_table = {n: [] for n in range(256)}


def fill_table():
    for command in inp:
        if '=' in command:
            add(command)
        else:
            delete(command)


def add(string):
    lens = string.split('=')
    idx = hash_string(lens[0])
    bucket = hash_table[idx]
    for x in bucket:
        if lens[0] == x[0]:
            x[1] = lens[1]
            return
    bucket.append(lens)


def delete(string):
    label = string[:-1]
    idx = hash_string(label)
    bucket = hash_table[idx]
    for i, lens in enumerate(bucket):
        if label in lens:
            bucket.pop(i)


def hash_string(string) -> int:
    curr_val = 0
    for c in string:
        curr_val = (curr_val + ord(c)) * 17 % 256
    return curr_val


# p1
def mult_hash(arr) -> int:
    result = 0
    for s in arr:
        result += hash_string(s)
    return result


def calc_focus_power():
    total = 0
    for k, v in hash_table.items():
        for i, lens in enumerate(v):
            total += (k + 1) * (i + 1) * int(lens[1])
    return total


fill_table()
print(calc_focus_power())



















