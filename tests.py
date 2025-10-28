import unittest
import poker

PAIRS = (0b1100, 0b1010, 0b1001, 0b0101 , 0b0011)
FULL_HAND_STRING = "A♣A♦A♥A♠K♣K♦K♥K♠Q♣Q♦Q♥Q♠J♣J♦J♥J♠10♣10♦10♥10♠9♣9♦9♥9♠8♣8♦8♥8♠7♣7♦7♥7♠6♣6♦6♥6♠5♣5♦5♥5♠4♣4♦4♥4♠3♣3♦3♥3♠2♣2♦2♥2♠"

class DisplayTests(unittest.TestCase):
    def test_get_hand_string(self):
        hand = 0xFFFFFFFFFFFFF
        self.assertEqual(poker.get_hand_string(hand), FULL_HAND_STRING)


class GetPairTests(unittest.TestCase):
    def setUp(self):
        self.all_pair_hands = []
        for p in PAIRS:
            for i in range(13):
                self.all_pair_hands.append(p << i)


def get_permutations(l: list):
    def loop(k: int, l: list):
        if k <= 1:
            print(l)
            return

        loop(k-1, l)
        for i in range(k-1):
            swap_index = i if k % 2 == 0 else 0
            l[swap_index], l[k-1] = l[k-1], l[swap_index] # swap swap_index and k-1
            loop(k-1, l)

    
    loop(len(l), l)
    
    

            
          

    


