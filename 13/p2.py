from main import lines

input_data = []
buffer = []
total = 0
smudge = 1


def compare(arr_1, arr_2):
    global smudge
    counter = 0
    if not smudge:
        counter += 1
    if arr_1 == arr_2:
        return 0
    for i in range(len(arr_1)):
        if arr_1[i] != arr_2[i]:
            counter += 1
        if counter > 1:
            return -1
    smudge = 0
    return 1


def detect_mirror(array: list) -> int:
    global smudge
    for i in range(len(array) - 1):
        compare_res = compare(array[i], array[i + 1])
        if compare_res == -1:
            smudge = 1
            continue
        limit = min(i, len(array)-2 - i)
        for c in range(1, limit+1):
            compare_res = compare(array[i - c], array[i+1 + c])
            if compare_res == -1:
                limit = -1
                smudge = 1
                break
        if smudge:
            continue
        if limit > -1:
            return i + 1


def rotate(array):
    return [list(row) for row in zip(*array[::-1])]


for line in lines:
    if line == '':
        input_data.append(buffer)
        buffer = []
        continue
    buffer.append(list(line))
input_data.append(buffer)

for img in input_data:
    smudge = 1
    m = detect_mirror(img)
    if m is None:
        m = detect_mirror(rotate(img))
    else:
        m *= 100
    total += m
print(total)

# for st in rotate(input_data[0]):
#     print(''.join(st))

# x < 35598, 28806 = x
# .########..##
# .###..###.#.#
# ###....###.##
# #...##...##.#
# .########.#..
# #...##..#####
# #.##..##.#...
# ....##....#..
# ....##....#..
#
# ..##.##..
# ....#.###
# ..#.#.###
# ..#.#..##
# ##.###..#
# ##.###..#
# ..#.#..##
# ..#.#.###
# ...##.###
# ..##.##..
# ##.###.#.
# ...#..#.#
# ...#.####






