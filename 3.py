from main import lines


def gear_ratios_2(array):
    counter = 0
    # find all element around *
    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] == '*':
                numbers = []
                for i in range(max(y-1, 0), min(y+2, len(array))):
                    for j in range(max(x-1, 0), min(x+2, len(array[0]))):
                        if array[i][j].isdigit():
                            numbers.append([j, i])
                nums = set()
                # found unic numbers
                for coord in numbers:
                    coord_buffer = []
                    coord_x = int(coord[0])
                    coord_y = int(coord[1])
                    coord_position_left = max(coord_x-1, 0)
                    coord_position_left_left = max(coord_x-2, 0)
                    coord_position_right = min(coord_x+1, len(array[0])-1)
                    coord_position_right_right = min(coord_x+2, len(array[0])-1)
                    if array[coord_y][coord_position_left].isdigit():
                        coord_buffer.append(coord_position_left)
                        if array[coord_y][coord_position_left_left].isdigit():
                            coord_buffer.append(coord_position_left_left)
                    if array[coord_y][coord_position_right].isdigit():
                        coord_buffer.append(coord_position_right)
                        if array[coord_y][coord_position_right_right].isdigit():
                            coord_buffer.append(coord_position_right_right)
                    coord_buffer.append(coord_x)
                    coord_buffer.sort()
                    nums.add(int(array[coord_y][coord_buffer[0]:coord_buffer[-1]+1]))
                # count
                if len(nums) > 1:
                    a = 1
                    for elem in nums:
                        a *= elem
                    counter += a
    return counter


def gear_ratios(array):
    coords_numbers = []
    total = 0
    # collect coordinates of numbers in double array
    for n in range(len(array)):
        y = n
        number = []
        for m in range(len(array[n])):
            if array[n][m].isdigit():
                x = m
                number.append([x, y])
            else:
                if len(number) > 0:
                    coords_numbers.append(number)
                    number = []
        if len(number) > 0:
            coords_numbers.append(number)
    # find all chars around number in double array
    for coord in coords_numbers:
        buffer = []
        for dot in coord:
            y1 = max(dot[1] - 1, 0)
            y2 = min(dot[1] + 2, len(array))
            x1 = max(dot[0] - 1, 0)
            x2 = min(dot[0] + 2, len(array[0]))
            for i in range(y1, y2):
                for j in range(x1, x2):
                    buffer.append(array[i][j])
    #     check buffer for symbols and sum numbers
        for symbol in buffer:
            if symbol in '!@#$%^&*()_+-=<>?,/`~':
                number = int(array[coord[0][1]][coord[0][0]: coord[-1][0]+1])
                total += number
                break
    return total
