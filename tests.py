import unittest
import poker

FULL_HAND = 0xFFFFFFFFFFFFF
FULL_HAND_STRING = "A♣A♦A♥A♠K♣K♦K♥K♠Q♣Q♦Q♥Q♠J♣J♦J♥J♠X♣X♦X♥X♠9♣9♦9♥9♠8♣8♦8♥8♠7♣7♦7♥7♠6♣6♦6♥6♠5♣5♦5♥5♠4♣4♦4♥4♠3♣3♦3♥3♠2♣2♦2♥2♠"

class DisplayTests(unittest.TestCase):
    def test_get_string_from_hand(self):
        hand_string = poker.get_string_from_hand(FULL_HAND)
        print()
        print(f"{FULL_HAND:0X} -> {hand_string}")
        self.assertEqual(hand_string, FULL_HAND_STRING)

    def test_get_hand_from_string(self):
        hand = poker.get_hand_from_string(FULL_HAND_STRING)
        print()
        print(f"{FULL_HAND_STRING} -> {hand:0X}")
        self.assertEqual(hand, FULL_HAND)


class GetPairTests(unittest.TestCase):
    def test_get_pairs(self):
        pass



            
          

    


