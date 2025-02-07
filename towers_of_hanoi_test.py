import unittest
from towers_of_hanoi import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        self.game = None

    def test_initialisation(self):
        self.assertEqual(self.game.get_num_moves(), 0)
        self.assertEqual(self.game.get_min_moves(), 7)
        expected_state = "\nLeft Stack: [3, 2, 1]\nMiddle Stack: []\nRight Stack: []"
        self.assertEqual(self.game.to_String(), expected_state)

    def test_valid_move(self):
        message = self.game.move(0, 2)
        self.assertIsNone(message)
        expected_state = "\nLeft Stack: [3, 2]\nMiddle Stack: []\nRight Stack: [1]"
        self.assertEqual(self.game.to_String(), expected_state)
        self.assertEqual(self.game.get_num_moves(), 1)
        self.assertFalse(self.game.is_over())

    def test_invalid_move(self):
        message = self.game.move(1, 0)
        self.assertIsNotNone(message)
        expected_state = "\nLeft Stack: [3, 2, 1]\nMiddle Stack: []\nRight Stack: []"
        self.assertEqual(self.game.to_String(), expected_state)
        self.assertEqual(self.game.get_num_moves(), 0)
