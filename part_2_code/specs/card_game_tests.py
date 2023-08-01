import unittest
from src.card import Card
from src.card_game import CardGame

# I've written the dynamic tests

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()

    def test_check_for_ace_true(self):
        card = Card("clubs", 1)
        self.assertTrue(self.card_game.check_for_ace(card))

    def test_check_for_ace_false(self):
        card = Card("hearts", 7)
        self.assertFalse(self.card_game.check_for_ace(card))

    def test_highest_card_card1_higher(self):
        card1 = Card("diamonds", 10)
        card2 = Card("hearts", 5)
        result = self.card_game.highest_card(card1, card2)
        self.assertEqual(result, card1)

    def test_highest_card_card2_higher(self):
        card1 = Card("hearts", 3)
        card2 = Card("clubs", 8)
        result = self.card_game.highest_card(card1, card2)
        self.assertEqual(result, card2)

    def test_cards_total(self):
        cards = [Card("diamonds", 5), Card("hearts", 2), Card("spaces", 9)]
        result = self.card_game.cards_total(cards)
        self.assertEqual(result, "you have a total of 16 I think")
