import random
def get_hand():
    hand = 0
    for i in range(0, 5):
        shift = random.randint(0, 51) 
        hand = hand | (1 << shift)
    return hand
    
def has_n_of_a_kind(hand):
    rank_mask = 0xF0000000000000
    for i in range(14, 0, -1):
        rank = hand & rank_mask
        count = count_set_bits(rank)
        if count > 1:
            return i, count
        rank_mask = rotate_mask_right(rank_mask, 4, 52)
        
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

hand = 0b0110000001000000000010000000000000000100000000000000
print_hand(hand)
print(has_n_of_a_kind(hand))