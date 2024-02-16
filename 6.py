from main import lines


def take_numbers(input_data):
    return list(map(lambda data: data.split(':')[1].strip().split(), input_data))


# part 1
def organize(input_data):
    result = take_numbers(input_data)
    for i in range(len(result)):
        result[i] = list(map(lambda number: int(number), result[i]))
    return result


def organize_part_2(input_data):
    result = take_numbers(input_data)
    for s in range(len(result)):
        result[s] = [int(''.join(result[s]))]
    return result


def calculate(input_data):
    result = 1
    time = input_data[0]
    distance = input_data[1]
    for t in time:
        for j in range(1, t):
            if j * (t - j) > distance[time.index(t)]:
                result *= len([x for x in range(t)][j-1: -(j-1)])-1
                break
    return result


race = organize_part_2(lines)
result = calculate(race)
print(result)

