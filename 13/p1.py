from main import lines

input_data = []
buffer = []
total = 0


def detect_mirror(array):
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            mirror_coord = i
            l_cursor = i
            r_cursor = i + 1
            while True:
                if array[l_cursor] == array[r_cursor]:
                    if l_cursor == 0 or r_cursor == len(array)-1:
                        return mirror_coord + 1
                else:
                    break
                l_cursor -= 1
                r_cursor += 1


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
    smudge = True
    m = detect_mirror(img)
    if m is None:
        m = detect_mirror(rotate(img))
    else:
        m *= 100
    total += m
print(total)

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








