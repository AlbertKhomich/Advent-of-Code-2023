from main import lines


points = {'5': 6, '4': 5, '3x2': 4, '3': 3, '2x2': 2, '2': 1}
points_buffer = []
bonus_point = 0


def organize(input_data):
    result = {hand.split()[0]: int(hand.split()[1]) for hand in input_data}
    return result


# with Jocker
def count_points(hand):
    global points_buffer, bonus_point

    def clean_buffers():
        global points_buffer, bonus_point
        points_buffer = []
        bonus_point = 0

    if len(hand) < 1:
        if len(points_buffer) > 0:
            result = 0
            if bonus_point == 0:
                result = points_buffer
            if bonus_point > 0:
                points_buffer[0] = points_buffer[0] + bonus_point
                result = points_buffer
            clean_buffers()
            return points['x'.join(list(map(lambda x: str(x), sorted(result, reverse=True))))]
        else:
            result_bonus = bonus_point
            clean_buffers()
            if result_bonus > 0:
                if result_bonus == 5:
                    return result_bonus+1
                else:
                    return points[str(result_bonus+1)]
            return 0
    card = hand[0]
    point = hand.count(card)
    if card == 'J':
        bonus_point = point
    else:
        if point > 1:
            points_buffer.append(point)
    return count_points(hand.replace(card, ''))


# [{'TQQJA': 483}, {'T55J5': 684}]
# compare hands in one rank
def compare(hands: list[dict]) -> list[dict]:
    rank_points = {
        'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14
    }

    def custom_key(hand):
        hand = list(hand.keys())[0]
        return [rank_points[card] for card in hand]

    sorted_hands = sorted(hands, key=custom_key)
    return sorted_hands


def create_leaderboard(players_hands):
    ranks = {}
    leaderboard = []
    global points_buffer
    hands = organize(players_hands)
    for hand, bid in hands.items():
        p = count_points(hand)
        if p not in ranks:
            ranks[p] = []
        ranks[p].append({hand: bid})
    for rank in range(7):
        if rank in ranks:
            leaderboard += compare(ranks[rank])
    return leaderboard


def count_total_bid(leaderboard):
    rank = 1
    total = 0
    for hand in leaderboard:
        total += list(hand.values())[0] * rank
        rank += 1
    return total


leaders = create_leaderboard(lines)
total_points = count_total_bid(leaders)
print(total_points)
print(leaders)


# without Jocker
#
# rank_points = {
#         '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
#         '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
#     }

# def count_points(hand):
#     global points_buffer
#     if len(hand) <= 1:
#         if len(points_buffer) > 0:
#             result = points_buffer
#             points_buffer = []
#             return points['x'.join(list(map(lambda x: str(x), sorted(result))))]
#         else:
#             return 0
#     card = hand[0]
#     point = hand.count(card)
#     if point > 1:
#         points_buffer.append(point)
#     return count_points(hand.replace(card, ''))