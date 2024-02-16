from main import lines


result = 0


def organize_input(array):
    return list(map(lambda x: list(map(lambda y: int(y), x.split())), array))


def solve_p1(array):
    new_array = [array[n+1] - array[n] for n in range(len(array)-1)]
    if all(x == 0 for x in new_array):
        return array[-1]
    return array[-1] + solve_p1(new_array)


# 2 solving
for line in organize_input(lines):
    reversed_line = list(reversed(line))
    result += solve_p1(reversed_line)
print(result)
# 884

#  1 solving
# for line in organize_input(lines):
#     result += solve_p1(line)
# print(result)
# 1974913369







