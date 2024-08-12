import time

# Define the directions and their corresponding movements
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Parse the input
input_data = []
with open('text.txt', 'r') as file:
    for line in file:
        if line.strip():  # Ensure the line is not empty
            direction, length, color = line.split()
            input_data.append((direction, int(length), color))

def parse_hex_instructions(input_data):
    parsed_instructions = []
    for hex_code in input_data:
        hex_code = hex_code[2][2:]  # Remove the leading '#'
        distance = int(hex_code[:5], 16)
        direction_digit = int(hex_code[5], 16)
        if direction_digit == 0:
            direction = 'R'
        elif direction_digit == 1:
            direction = 'D'
        elif direction_digit == 2:
            direction = 'L'
        elif direction_digit == 3:
            direction = 'U'
        else:
            raise ValueError(f"Invalid direction digit: {direction_digit}")
        parsed_instructions.append((direction, distance, 'color'))
    return parsed_instructions

def get_trench_vertices(input_data, directions):
    x, y = 0, 0
    vertices = [(x, y)]
    for direction, length, _ in input_data:
        dx, dy = directions[direction]
        x += dx * length
        y += dy * length
        if (x, y) not in vertices:  # Check if the new vertex is not already in the list
            vertices.append((x, y))
    return vertices

def shoelace_formula(points):
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    return abs(area) / 2

def calculate_perimeter(points):
    perimeter = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        perimeter += abs(x2 - x1) + abs(y2 - y1)
    return perimeter

def solve(input_data):
    # Get the trench vertices
    vertices = get_trench_vertices(input_data, directions)

    # Calculate the area using the Shoelace formula
    area = shoelace_formula(vertices)

    # Calculate the perimeter
    perimeter = calculate_perimeter(vertices)

    # Calculate the total area including the border
    total_area = int(area + perimeter / 2 + 1)

    print(f"Total area including border: {total_area}")

def p1():
    solve(input_data)

def p2():
    input_data_p2 = parse_hex_instructions(input_data)
    solve(input_data_p2)

start_time = time.time()
p1()
p2()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")