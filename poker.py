import random

"""
Ranks
high card
one pair
two pair
three of a kind,
straight
flush
full-house (three)
four of a kind
straight flush
"""

PAIR_OFFSET = 13
TWO_PAIR_OFFSET = 17
THREE_OF_KIND_OFFSET = 21
STRAIGHT_OFFSET = 25
FLUSH_OFFSET = 29
FULL_HOUSE_THREE_OFFSET = 46
FOUR_OF_KIND_OFFSET = 50
STRAIGHT_FLUSH_OFFSET = 41

SUITS = ('♣','♦','♥','♠')
RANKS = ('A','K','Q','J','10','9','8','7','6','5','4','3','2')

def get_hand():
    hand = 0
    for _ in range(5):
        shift = random.randint(0, 51) 
        hand = hand | (1 << shift)
    return hand
    
def get_n_of_kinds(hand: int):
    kicker_ranks = 0
    rank_mask = 0xF << 48
    n_of_kinds: dict[int, list[int]] = {4:[], 3:[], 2:[]}
    found = 0
    for i in range(13):
        rank = hand & rank_mask
        count = rank.bit_count()
        if count > 1:
            n_of_kinds[count].append(13 - i)
            kicker_ranks = kicker_ranks | rank_mask
            found += 1
            if count == 4 or found == 2:
                break
        rank_mask = rank_mask >> 4
    return (n_of_kinds, kicker_ranks)

def get_straight(hand: int):
    ranks = reduce_to_ranks(hand)
    straight_mask = 0x1F << 8
    for i in range(9):
        if ranks & straight_mask == straight_mask:
            return 13 - i
        straight_mask = straight_mask >> 1
    return 0

def get_flush(hand: int):
    suit_mask = 0x8888888888888
    for _ in range(4):
        suit = hand & suit_mask
        if suit.bit_count() >= 5:
            return reduce_to_ranks(hand)
        suit_mask = suit_mask >> 1
    return 0

def get_high_card(hand: int):
    ranks = reduce_to_ranks(hand)
    return ranks.bit_length()-1

def reduce_to_ranks(hand: int):
    rank_mask = 0xF << 48
    ranks = 0
    for i in range(13):
        rank = hand & rank_mask
        if rank:
            ranks = ranks | 1
        if i < 12:
            ranks = ranks << 1
        rank_mask = rank_mask >> 4
    return ranks


def rank_n_of_kinds(hand: int):
    n_of_kinds, kicker_ranks = get_n_of_kinds(hand)
    rank = kicker_ranks

    if n_of_kinds[4]:
        rank |= (n_of_kinds[4][0] << FOUR_OF_KIND_OFFSET)
    elif n_of_kinds[3] and n_of_kinds[2]:
        rank |= (n_of_kinds[3][0] << FULL_HOUSE_THREE_OFFSET)
        rank |= (n_of_kinds[2][0] << PAIR_OFFSET)
    elif len(n_of_kinds[2]) == 2:
        rank |= (n_of_kinds[2][0] << TWO_PAIR_OFFSET)
        rank |= (n_of_kinds[2][1] << PAIR_OFFSET)
    else:
        rank |= (n_of_kinds[2][0] << PAIR_OFFSET)


def get_full_bitmask(length: int):
    return int("1" * length, 2)

def get_string_from_hand(hand: int):
    hand_string = ""
    mask = 1 << 51
    for i in range(52):
        if hand & mask:
            hand_string += RANKS[i//4] + SUITS[i%4]
        mask >>= 1
    return hand_string

def get_hand_from_string(string: str):
    hand = 0
    card_strings = pair_off(string)
    for c in card_strings:
        rank = RANKS.index(c[0])
        suit = RANKS.index(c[1])
        hand |= suit << rank

def pair_off(string: str) -> list[str]:
    if len(string) == 0:
        return []
    pairs: list[str] = []
    for i in range(len(string)):
        if i % 2 == 0:
            pairs.append("")
        pairs[len(pairs)-1] += string[i]
    return pairs
