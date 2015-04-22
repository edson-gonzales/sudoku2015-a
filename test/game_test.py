# game_test.py
# author: Daniel Jauregui
# date: 4-21-2015

import unittest
from game import Game


class GameTest(unittest.TestCase):

    def test_generate_game_create_and_array_of_81_items(self):
        game = Game()
        self.assertEqual(81, len(game.generate_game()))
