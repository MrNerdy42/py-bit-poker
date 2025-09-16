import random

"""Actual poker stuff"""

def get_hand():
    hand = 0
    for i in range(0, 5):
        shift = random.randint(0, 51) 
        hand = hand | (1 << shift)
    return hand
    
def get_n_of_kinds(hand):
    rank_mask = 0xF << 48
    n_of_kinds = []
    for i in range(13):
        rank = hand & rank_mask
        count = count_set_bits(rank)
        if count > 1:
            n_of_kinds.append((13 - i, count))
        if len(n_of_kinds) == 2 or (len(n_of_kinds) == 1 and n_of_kinds[0][1] == 4):
            break
        rank_mask = rotate_mask_right(rank_mask, 4, 52)
    return n_of_kinds

def get_strait(hand):
    pass


def reduce_to_ranks(hand):
    rank_mask = 0xF << 48
    ranks = 0
    for i in range(13):
        rank = (hand & rank_mask) >> (i*4)
        if rank > 1:
            ranks = ranks & (1 << i)

        

"""Bit twiddling utils"""
        
def count_set_bits(n):
    s = 0
    while(n):
        n &= n-1
        s += 1
    return s
    
def rotate_mask_right(n, shift, wrap_length):
    little_end = n & get_full_bitmask(shift)
    little_end = little_end << (wrap_length - shift)
    n = n >> shift
    n = n | little_end
    return n

def get_full_bitmask(length):
    return int("1" * length, 2)

def print_hand(hand):
    print("{:052b}".format(hand))

"""main"""
hand = 0xF000000000000

print(get_n_of_kinds(hand))
