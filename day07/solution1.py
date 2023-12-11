from collections import Counter
from functools import cmp_to_key


CARDS = "AKQJT98765432"


def compare(type_hand1: tuple[int, str], type_hand2: tuple[int, str]) -> int:
    type1, hand1 = type_hand1
    type2, hand2 = type_hand2
    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1
    return compare_second_order(hand1, hand2)


def compare_second_order(hand1: str, hand2: str) -> int:
    for c1, c2 in zip(hand1, hand2):
        if CARDS.index(c1) < CARDS.index(c2):
            return -1
        elif CARDS.index(c1) > CARDS.index(c2):
            return 1
    return -1


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

hands_with_bids = {l.split()[0]: int(l.split()[1]) for l in lines}
hands_with_types: list[tuple[int, str]] = []
for hand in hands_with_bids.keys():
    c = Counter(hand)
    counted_cards = [n for _, n in c.most_common()]
    if counted_cards[0] == 5:
        hands_with_types.append((0, hand))  # five of a kind
    elif counted_cards[0] == 4:
        hands_with_types.append((1, hand))  # four of a kind
    elif counted_cards[0] == 3:
        if counted_cards[1] == 2:
            hands_with_types.append((2, hand))  # full house
        else:
            hands_with_types.append((3, hand))  # three of a kind
    elif counted_cards[0] == 2:
        if counted_cards[1] == 2:
            hands_with_types.append((4, hand))  # two pair
        else:
            hands_with_types.append((5, hand))  # one pair
    else:
        hands_with_types.append((6, hand))  # high card

sorted_hands = [h for _, h in sorted(hands_with_types, key=cmp_to_key(compare))]
print(sum(hands_with_bids[h] * (len(lines) - i)
          for i, h in enumerate(sorted_hands)))
