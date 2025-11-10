import unittest
import poker


FULL_HAND_STRING = "A♣A♦A♥A♠K♣K♦K♥K♠Q♣Q♦Q♥Q♠J♣J♦J♥J♠10♣10♦10♥10♠9♣9♦9♥9♠8♣8♦8♥8♠7♣7♦7♥7♠6♣6♦6♥6♠5♣5♦5♥5♠4♣4♦4♥4♠3♣3♦3♥3♠2♣2♦2♥2♠"

class DisplayTests(unittest.TestCase):
    def test_get_hand_string(self):
        hand = 0xFFFFFFFFFFFFF
        self.assertEqual(poker.get_string_from_hand(hand), FULL_HAND_STRING)


class GetPairTests(unittest.TestCase):
    def test_get_pairs(self):

        



            
          

    


