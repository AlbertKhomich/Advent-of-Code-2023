from main import lines


def scratchcards_2(array):
    pocket_of_cards = {i: 1 for i in range(len(array))}
    for i in range(len(array)):
        card_counter = 0
        card_points = extract_points(array[i])
        win_points = card_points[0]
        my_points = card_points[1]
        for point in my_points:
            if point in win_points:
                card_counter += 1
        for j in range(i+1, i + card_counter + 1):
            pocket_of_cards[j] += pocket_of_cards[i]
    count = 0
    for k, v in pocket_of_cards.items():
        count += v
    return count


def scratchcards(array):
    total = 0

    for card in array:
        card_counter = 0
        card_points = extract_points(card)
        win_points = card_points[0]
        my_points = card_points[1]
        for point in my_points:
            if point in win_points:
                if card_counter > 0:
                    card_counter *= 2
                else:
                    card_counter = 1
        total += card_counter
    return total


def extract_points(string):
    points = string.split(':')[1].split('|')
    win_points = points[0].strip().split(' ')
    my_points = points[1].strip().split(' ')
    remove_all(my_points, '')
    remove_all(win_points, '')
    return [win_points, my_points]


def remove_all(array, symbol_to_remove):
    for e in array:
        if e == symbol_to_remove:
            array.remove(e)
