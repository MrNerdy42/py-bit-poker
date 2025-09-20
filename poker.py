import random

SUITS = ('C','D','H','S')
RANKS = ('A','K','Q','J','10','9','8','7','6','5','4','3','2','1')

"""Actual poker stuff"""

def get_hand():
    hand = 0
    for i in range(5):
        shift = random.randint(0, 51) 
        hand = hand | (1 << shift)
    return hand
    
def get_n_of_kinds(hand):
    kicker_mask = 0
    rank_mask = 0xF << 48
    n_of_kinds = []
    for i in range(13):
        rank = hand & rank_mask
        count = count_set_bits(rank)
        if count > 1:
            n_of_kinds.append((13 - i, count))
            kicker_mask = kicker_mask | rank_mask
        if len(n_of_kinds) == 2 or (len(n_of_kinds) == 1 and n_of_kinds[0][1] == 4):
            break
        rank_mask = rank_mask >> 4
    return (n_of_kinds, kicker_mask)

def get_straight(hand):
    ranks = reduce_to_ranks(hand)
    straight_mask = 0x1F << 8
    for i in range(9):
        if ranks & straight_mask == straight_mask:
            return 13 - i
        straight_mask = straight_mask >> 1
    return 0

def get_flush(hand):
    suit_mask = 0x8888888888888
    for i in range(4):
        suit = hand & suit_mask
        if count_set_bits(suit) >= 5:
            return 4 - i
        suit_mask = suit_mask >> 1
    return 0

def reduce_to_ranks(hand):
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

def print_hand(hand):
    print("{:052b}".format(hand)[:52])


"""Bit twiddling utils"""
        
def count_set_bits(n):
    s = 0
    while(n):
        n &= n-1
        s += 1
    return s

def get_full_bitmask(length):
    return int("1" * length, 2)


"""main"""
# hand = 0x0000030000003
hand = 0x1717110711171
print(get_flush(hand))
