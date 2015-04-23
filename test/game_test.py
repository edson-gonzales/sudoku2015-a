# game_test.py
# author: Daniel Jauregui
# date: 4-21-2015

import unittest
from game import Game


class GameTest(unittest.TestCase):

    def test_generate_game_create_and_array_of_81_items(self):
        game = Game()
        self.assertEqual(81, len(game.generate_game()))

    def test_that_the_board_for_each_number_of_the_first_column_is_not_duplicated_in_its_column(self):
        game = Game()
        board = game.generate_game()
        count = 0
        for column in xrange(9):
            column_x = []
            column_x.append(board[column])
            for next_number in xrange(8):
                column_x.append(board[column + 9 * (next_number + 1)])
                if board[column] == board[column + 9 * (next_number + 1)] and board[column] != 0:
                    count += 1
        self.assertEqual(0, count)

    def test_that_the_board_for_each_number_of_the_first_row_is_not_duplicated_in_its_row(self):
        game = Game()
        board = game.generate_game()
        count = 0
        column = 0
        for position in xrange(9):
            for row in xrange(8):
                if board[column] == board[column + 1 + row] and board[column] != 0:
                    count += 1
            column += 9
        self.assertEqual(0, count)

    def test_that_the_board_for_each_number_in_the_block_has_not_duplicate(self):
        game = Game()
        board = game.generate_game()
        blocks = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                  [3, 4, 5, 12, 13, 14, 21, 22, 23],
                  [6, 7, 8, 15, 16, 17, 24, 25, 26],
                  [27, 28, 29, 36, 37, 38, 45, 46, 47],
                  [30, 31, 32, 39, 40, 41, 48, 49, 50],
                  [33, 34, 35, 42, 43, 44, 51, 52, 53],
                  [54, 55, 56, 63, 64, 65, 72, 73, 74],
                  [57, 58, 59, 66, 67, 68, 75, 76, 77],
                  [60, 61, 62, 69, 70, 71, 78, 79, 80]]
        count = 0
        for block in blocks:
            block_list = []
            for position in block:
                if board[position] != 0:
                    block_list.append(board[position])
            unique = list(set(block_list))
            if len(unique) != len(block_list):
                count += 1
        self.assertEqual(0, count)

    def test_the_level_of_game_return_number_of_0s_between_min_and_max_threshold(self):
        game = Game(70, 80)
        board = game.generate_game()
        numbers = board.count(0)
        self.assertTrue(game.min_threshold <= numbers <= game.max_threshold)

    def test_the_min_threshold_cannot_be_major_or_equal_than_max_threshold(self):
        game = Game(50, 50)
        self.assertTrue(game.min_threshold < game.max_threshold)

    def test_the_min_threshold_cannot_be_less_than_10(self):
        game = Game(1, 80)
        self.assertTrue(game.min_threshold >= 10)

    def test_the_min_threshold_cannot_be_major_than_71(self):
        game = Game(80, 81)
        self.assertTrue(game.min_threshold <= 71)

    def test_the_max_threshold_cannot_be_less_than_11(self):
        game = Game(5, 6)
        self.assertTrue(game.max_threshold >= 11)

    def test_the_max_threshold_cannot_be_major_than_81(self):
        game = Game(5, 85)
        self.assertTrue(game.max_threshold <= 81)

    def test_that_two_game_generated_with_the_same_instance_are_not_equal(self):
        game = Game(30, 40)
        board1 = game.generate_game()
        board2 = game.generate_game()
        self.assertTrue(board1 != board2)