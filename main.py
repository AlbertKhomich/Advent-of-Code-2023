file_path = './text.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]


def trebuchet_string(array):
    counter = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in array:
        node = {"left": None, "right": None}
        l_cursor = 0
        r_cursor = -1
        while True:
            for word in words:
                if word in line[0: l_cursor+1] and node['left'] is None:
                    node["left"] = words.index(word) + 1
                if line[l_cursor].isdigit() and node['left'] is None:
                    node['left'] = line[l_cursor]
                if word in line[r_cursor:] and node['right'] is None:
                    node["right"] = words.index(word) + 1
                if line[r_cursor].isdigit() and node['right'] is None:
                    node['right'] = line[r_cursor]
            if node['left'] is None:
                l_cursor += 1
            if node['right'] is None:
                r_cursor -= 1
            if node['left'] is not None and node['right'] is not None:
                counter += int(f'{node['left']}{node['right']}')
                break
    return counter


def trebuchet(array):
    counter = 0
    for line in array:
        l_cursor = 0
        r_cursor = len(line) - 1
        while True:
            if not line[l_cursor].isdigit():
                l_cursor += 1
            if not line[r_cursor].isdigit():
                r_cursor -= 1
            if line[l_cursor].isdigit() and line[r_cursor].isdigit():
                break
        counter += int(str(line[l_cursor]+line[r_cursor]))
    return counter
