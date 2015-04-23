# make_sudoku.py
# author: Daniel Jauregui
# date: 4-23-2015

import random


class Game(object):

    def __init__(self, min_threshold=20, max_threshold=30):
        if min_threshold > max_threshold and 10 >= min_threshold <= 71 and 11 >= max_threshold <= 81:
            self.max_threshold = max_threshold
            self.min_threshold = min_threshold
        else:
            self.min_threshold = 20
            self.max_threshold = 30
        self.hints = []
        self.board = []
        self.grid = [[0 for x in range(9)] for x in range(9)]
        self.first_param_in_axis_x = 0
        self.first_param_in_axis_y = 0
        self.second_param_in_axis_x = 0
        self.second_param_in_axis_y = 0

    def generate_game(self):
        """Call to make_puzzle with a empty board to generate game
        with level defined and it will return a array e.g.:
        Array: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        Where the position are from 0 to 80

        return -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        # self.write_number_in_board([None] * 81)
        self.board = []
        self.write_sudoku_base()
        self.start_shuffle(10)
        self.change_format_grid_to_array()
        self.set_level(self.board)
        return self.board

    def write_sudoku_base(self):
        for row in xrange(9):
            for column in xrange(9):
                self.grid[row][column] = (row * 3 + row / 3 + column) % 9 + 1

    def get_shuffle_two_cells(self, first_number, second_number):
        for row in xrange(0, 8, 3):
            for column in xrange(0, 8, 3):
                self.move_in_block(row, column, first_number, second_number)

    def move_in_block(self, row, column, first_number, second_number):
        for row_block in xrange(3):
            self.verify_number_in_column_block(row, column, row_block, first_number, second_number)
        self.grid[self.first_param_in_axis_x][self.first_param_in_axis_y] = second_number
        self.grid[self.second_param_in_axis_x][self.second_param_in_axis_y] = first_number

    def verify_number_in_column_block(self, row, column, row_block, first_number, second_number):
        for column_block in xrange(3):
            if self.grid[row + row_block][column + column_block] == first_number:
                self.first_param_in_axis_x = row + row_block
                self.first_param_in_axis_y = column + column_block
            if self.grid[row + row_block][column + column_block] == second_number:
                self.second_param_in_axis_x = row + row_block
                self.second_param_in_axis_y = column + column_block

    def start_shuffle(self, shuffle_level):
        for repeat in xrange(shuffle_level):
            self.get_shuffle_two_cells(random.randint(1, 9), random.randint(1, 9))

    def change_format_grid_to_array(self):
        for row in xrange(9):
            for column in xrange(0, 9):
                self.board.append(self.grid[row][column])

    def set_level(self, board):
        level = random.randint(self.min_threshold, self.max_threshold)
        init_level = 0
        while init_level < level:
            position = random.randint(0, 80)
            if board[position] != 0:
                self.hints.append((position, board[position]))
                board[position] = 0
                init_level += 1
        self.board = board
