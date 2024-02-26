from main import lines
from heapq import heappop, heappush

grid = [list(map(int, list(line))) for line in lines]
seen = set()
queue = [(0, 0, 0, 0, 0, 0)]

while queue:
    heat, row, col, dir_row, dir_col, steps = heappop(queue)

    if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
        print(heat)
        break

    if (row, col, dir_row, dir_col, steps) in seen:
        continue

    seen.add((row, col, dir_row, dir_col, steps))

    if steps < 3 and (dir_row, dir_col) != (0, 0):
        next_row = row + dir_row
        next_col = col + dir_col
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
            heappush(queue, (heat + grid[next_row][next_col], next_row, next_col, dir_row, dir_col, steps + 1))

    for next_dir_row, next_dir_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if (next_dir_row, next_dir_col) != (dir_row, dir_col) and (next_dir_row, next_dir_col) != (-dir_row, -dir_col):
            next_row = row + next_dir_row
            next_col = col + next_dir_col
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                heappush(queue, (heat + grid[next_row][next_col], next_row, next_col, next_dir_row, next_dir_col, 1))


