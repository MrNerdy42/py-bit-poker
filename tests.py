import unittest
import poker

"""
♣ 2663
♦ 2666
♥ 2665
♠ 2660
"""

FULL_HAND = 0xFFFFFFFFFFFFF
FULL_HAND_STRING = "A♣A♦A♥A♠K♣K♦K♥K♠Q♣Q♦Q♥Q♠J♣J♦J♥J♠X♣X♦X♥X♠9♣9♦9♥9♠8♣8♦8♥8♠7♣7♦7♥7♠6♣6♦6♥6♠5♣5♦5♥5♠4♣4♦4♥4♠3♣3♦3♥3♠2♣2♦2♥2♠"

class DisplayTests(unittest.TestCase):
    def test_get_string_from_hand(self):
        hand_string = poker.get_string_from_hand(FULL_HAND)
        self.assertEqual(hand_string, FULL_HAND_STRING)

    def test_get_hand_from_string(self):
        hand = poker.get_hand_from_string(FULL_HAND_STRING)
        self.assertEqual(hand, FULL_HAND)

class UtilityTests(unittest.TestCase):
    def test_reduce_to_ranks(self):
        ranks = poker.reduce_to_ranks(FULL_HAND)
        self.assertEqual(ranks, 0x1FFF)

class GetNOfKindsTests(unittest.TestCase):
    def test_get_one_pair(self):
        pair = poker.get_hand_from_string("8♣8♠")
        kickers = poker.get_hand_from_string("2♦A♥5♦")
        kicker_ranks = poker.reduce_to_ranks(kickers)
        hand = pair | kickers
        result = poker.get_n_of_kinds(hand)
        self.assertEqual(result, ({4:[], 3:[], 2:[6]}, kicker_ranks))




          

    


