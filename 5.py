from main import lines


locations = []


def arr_to_int(array):
    return list(map(lambda n: int(n), array))


def detect_seeds(array):
    seeds = arr_to_int(array[0].split(':')[1].strip().split(' '))
    return seeds


def organize_input(array):
    maps = []
    buffer = []
    for i in range(2, len(array)):
        if array[i] == '':
            maps.append(buffer)
            buffer = []
            continue
        if array[i][0].isalpha():
            continue
        if array[i][0].isdigit():
            buffer.append(arr_to_int(array[i].split()))
    maps.append(buffer)
    return maps


def compress_seed(seeds):
    for j in range(1, len(seeds)):
        if seeds[j-1][0] <= seeds[j][0] <= seeds[j-1][1]:
            seeds[j-1][1] = seeds[j][1]
            seeds.pop(j)
            break
        if j == len(seeds) - 1:
            return seeds
    return compress_seed(seeds)


def inspect(bucket, maps, maps_index=0):
        x1 = bucket[0]
        y1 = bucket[1]
        for v in range(maps_index, len(maps)):
            for interval in maps[v]:
                x2 = interval[1]
                y2 = interval[1] + interval[2] - 1
                shift = interval[0] - x2
                if x2 <= x1 <= y2:
                    x1 += shift
                    if x2 <= y1 <= y2:
                        y1 += shift
                        break
                    else:
                        locations.append(inspect([y2 + 1, y1], maps, v))
                        y1 = y2 + shift
                        break
                elif x2 <= y1 <= y2:
                    locations.append(inspect([x2, y1], maps, v))
                    y1 = x2 - 1
        return [x1, y1]


def seed_part_two(array):
    seeds = []
    seeds_ranges = detect_seeds(array)
    maps = organize_input(array)
    for i in range(0, len(seeds_ranges), 2):
        x = seeds_ranges[i]
        y = seeds_ranges[i] + seeds_ranges[i+1] - 1
        seeds.append([x, y])
    sorted_seeds = sorted(seeds, key=lambda m: m[0])
    compress_sorted_seed = compress_seed(sorted_seeds)
    for seed_interval in compress_sorted_seed:
        location = inspect(seed_interval, maps)
        locations.append(location)
    min_loc = min(list(map(lambda loc: loc[0], locations)))
    return min_loc


print(seed_part_two(lines))

# 69323688

# Part one
# def seed(array):
#     seeds = detect_seeds(array)
#     maps = organize_input(array)
#     return min(solve(seeds, maps))

# def solve(array_seeds, array_maps):
#     locations = set()
#     for number in array_seeds:
#         curr_location = prepare_seed(number, array_maps)
#         locations.add(curr_location)
#     return locations

# def prepare_seed(number_seed, array_maps):
#     curr_location = number_seed
#     for v in array_maps.values():
#         for m in v:
#             if m[1] <= curr_location <= m[1] + m[2]:
#                 curr_location = curr_location - m[1] + m[0]
#                 break
#     return curr_location



