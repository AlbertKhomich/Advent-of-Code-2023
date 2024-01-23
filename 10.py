from main import lines
from shapely.geometry import Point, Polygon
import math


up = ['7', '|', 'F', 'S']
right = ['J', '-', '7', 'S']
down = ['J', '|', 'L', 'S']
left = ['L', '-', 'F', 'S']
steps_count = 0
result = None


def find_start_point():
    x, y = None, None
    for i in range(len(lines)):
        if 'S' in lines[i]:
            y = i
            x = lines[i].index('S')
            break
    return x, y


def move(start_points_array, back_points_array):
    global steps_count
    new_start_points = []
    back_points = []

    def check_up():
        if point[1] > 0:
            x_step = point[0]
            y_step = point[1] - 1
            if (x_step, y_step) not in back_points_array:
                if lines[y_step][x_step] in up:
                    if (x_step, y_step) in new_start_points:
                        return False
                    new_start_points.append((x_step, y_step))
        return True

    def check_down():
        if point[1] < len(lines) - 1:
            x_step = point[0]
            y_step = point[1] + 1
            if (x_step, y_step) not in back_points_array:
                if lines[y_step][x_step] in down:
                    if (x_step, y_step) in new_start_points:
                        return False
                    new_start_points.append((x_step, y_step))
        return True

    def check_left():
        if point[0] > 0:
            x_step = point[0] - 1
            y_step = point[1]
            if (x_step, y_step) not in back_points_array:
                if lines[y_step][x_step] in left:
                    if (x_step, y_step) in new_start_points:
                        return False
                    new_start_points.append((x_step, y_step))
        return True

    def check_right():
        if point[0] < len(lines[0]) - 1:
            x_step = point[0] + 1
            y_step = point[1]
            if (x_step, y_step) not in back_points_array:
                if lines[y_step][x_step] in right:
                    if (x_step, y_step) in new_start_points:
                        return False
                    new_start_points.append((x_step, y_step))
        return True

    steps_count += 1
    for point in start_points_array:
        current_position = lines[point[1]][point[0]]
        if current_position == 'S':
            if not check_up() or not check_right() or not check_down() or not check_left():
                return steps_count
        elif current_position == '7':
            if not check_left() or not check_down():
                return steps_count
        elif current_position == '|':
            if not check_down() or not check_up():
                return steps_count
        elif current_position == 'F':
            if not check_down() or not check_right():
                return steps_count
        elif current_position == 'J':
            if not check_up() or not check_left():
                return steps_count
        elif current_position == '-':
            if not check_left() or not check_right():
                return steps_count
        elif current_position == 'L':
            if not check_up() or not check_right():
                return steps_count
        back_points.append(point)
    return new_start_points, back_points


def part_one_lose():
    global result
    while not isinstance(result, int):
        result = move(result[0], result[1])
    return result


def angle_from_center(point, center):
    x, y = point[0] - center[0], point[1] - center[1]
    return math.atan2(y, x)


def find_peaks(border_points):
    unique_points = set(border_points)
    center_x = sum(x for x, y in unique_points) / len(unique_points)
    center_y = sum(y for x, y in unique_points) / len(unique_points)
    center = (center_x, center_y)

    sorted_points = sorted(unique_points, key=lambda point: angle_from_center(point, center))
    print(sorted_points)
    return sorted_points


def find_points_to_check(points_of_polygon):
    points_to_check = []
    max_x = max(points_of_polygon, key=lambda p: p[0])[0]
    min_x = min(points_of_polygon, key=lambda p: p[0])[0]
    max_y = max(points_of_polygon, key=lambda p: p[1])[1]
    min_y = min(points_of_polygon, key=lambda p: p[1])[1]

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            point = (x, y)
            points_to_check.append(point)
    return points_to_check


# collect all coordinates and organize peaks in clockwise (remake logic from part 1)
def collect_polygon_peaks():
    peaks = []
    s = find_start_point()
    peaks.append(s)
    x = s[0]
    y = s[1]
    while True:
        if y-1 >= 0 and (x, y-1) not in peaks and lines[y-1][x] in up and lines[y][x] in down:
            y -= 1
            peaks.append((x, y))
        elif x+1 < len(lines[0]) and (x+1, y) not in peaks and lines[y][x+1] in right and lines[y][x] in left:
            x += 1
            peaks.append((x, y))
        elif y+1 < len(lines) and (x, y+1) not in peaks and lines[y+1][x] in down and lines[y][x] in up:
            y += 1
            peaks.append((x, y))
        elif x-1 >= 0 and (x-1, y) not in peaks and lines[y][x-1] in left and lines[y][x] in right:
            x -= 1
            peaks.append((x, y))
        else:
            break
    return peaks


all_coordinates = collect_polygon_peaks()
# points to check
points_inside = find_points_to_check(all_coordinates)

# calculate how many tiles are contained within the loop
polygon = Polygon(all_coordinates)
points_inside_polygon = [
    point for point in points_inside
    if polygon.contains(Point(point))
]
print(len(points_inside_polygon))

# part 1
# result = [[find_start_point()], []]
# print(part_one_lose())







