import unittest
from run import parse_card_input
from run import sort_by_rank

class TestStringMethods(unittest.TestCase):
    def test_parse_card_input(self):
        self.assertEqual(parse_card_input('Jack of Hearts'), ('J', 'H'))
        self.assertEqual(parse_card_input('jh'), ('J', 'H'))
        self.assertEqual(parse_card_input('two of club'), ('2', 'C'))
        self.assertEqual(parse_card_input('2 c'), ('2', 'C'))

    def test_sort_by_rank(self):
        deck = [('K', 'S'), ('3', 'D'), ('5', 'S'), ('Q', 'H'), ('A', 'C'), ('A', 'S')]
        sort_by_rank(deck)
        self.assertEqual(deck, [('A', 'C'), ('A', 'S'), ('3', 'D'), ('5', 'S'), ('Q', 'H'), ('K', 'S')])

if __name__ == '__main__':
    unittest.main()
