from main import lines


def power_sets(sets):
    points = 0
    games = []
    spliters = [',', ';']
    for s in sets:
        # ' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        game = [s.split(':')[1]]
        for spliter in spliters:
            buffer = []
            for cube in game:
                buffer.extend(cube.split(spliter))
            game = buffer
        games.append(game)

    for game in games:
        rgb = {'red': 1, "green": 1, "blue": 1}
        for throw in game:
            cube = throw.split()
            if rgb[cube[1]] < int(cube[0]):
                rgb[cube[1]] = int(cube[0])
        points += (rgb['red'] * rgb['green'] * rgb['blue'])

    return points


def cube_conundrum(text):
    points = 0
    rules = {'red': 12, 'green': 13, 'blue': 14}
    games = {
        game.split(':')[0]: [
            {
                cube.strip().split(' ')[1]: cube.strip().split(' ')[0]
                for cube in (elem.split(','))
            }
            for elem in game.split(':')[1].split(';')]
        for game in text
    }
    for game, cubes in games.items():
        cheat_flag = False
        for cube_set in cubes:
            if cheat_flag:
                break
            for color, num in cube_set.items():
                if int(num) > rules[color]:
                    cheat_flag = True
                    break
        if not cheat_flag:
            points += int(game.split(' ')[1])
    return points
