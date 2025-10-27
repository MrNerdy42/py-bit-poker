import unittest
import poker

PAIRS = (0b1100, 0b1010, 0b1001, 0b0101 , 0b0011)

class GetPairTests(unittest.TestCase):
    def setUp(self):
        self.all_pair_hands = []
        for p in PAIRS:
            for i in range(13):
                self.all_pair_hands.append(p << i)


def perm(l):
    if len(l) == 1:
        return l
    
    perm(l)