# make_sudoku.py
# author: Daniel Jauregui
# date: 4-23-2015

import random
from utils.singleton import Singleton

class Game(object):

    __metaclass__ = Singleton

    def __init__(self, min_threshold=20, max_threshold=30):
        """ Verify the conditions for min_threshold and max_threshold are applied"""
        if min_threshold > max_threshold and 10 >= min_threshold <= 71 and 11 >= max_threshold <= 81:
            self.max_threshold = max_threshold
            self.min_threshold = min_threshold
        else:
            self.min_threshold = 20
            self.max_threshold = 30
        self.hints = []
        self.board = []
        self.grid = None
        self.grid = [[0 for x in range(9)] for x in range(9)]
        self.first_param_in_axis_x = 0
        self.first_param_in_axis_y = 0
        self.second_param_in_axis_x = 0
        self.second_param_in_axis_y = 0

    def generate_game(self):
        """Generate a game that follow the sudoku rules and return a board in array of 81 items,
        where according with level returns some positions with 0

        return -- the game in Array e.g.: [4, 9, 3, 0, 5, ...., 8, 8, 0, 0, 1]
        """
        self.__init__()
        self.write_sudoku_base()
        self.start_shuffle(10)
        self.change_format_grid_to_array()
        self.set_level(self.board)
        return self.board

    def import_game(self, board):
        """import a game that follow the sudoku rules
        """
        self.board = board

    def write_sudoku_base(self):
        """This method fill in global grid variable the base of sudoku game,
        this base is a sudoku solved in order.
        """
        for row in xrange(9):
            for column in xrange(9):
                self.grid[row][column] = (row * 3 + row / 3 + column) % 9 + 1

    def get_shuffle_two_cells(self, first_number, second_number):
        """Get two random numbers in order to shuffle in grid that contains the base of
        sudoku solved.

        Keyword arguments:
        first_number -- Random number between 1 and 9
        second_number -- Random number between 1 and 9
        """
        for row in xrange(0, 8, 3):
            for column in xrange(0, 8, 3):
                self.move_in_block(row, column, first_number, second_number)

    def move_in_block(self, row, column, first_number, second_number):
        """Move for each blocks finding a numbers that will be shuffled into grid

        Keyword arguments:
        first_number -- Random number between 1 and 9
        second_number -- Random number between 1 and 9
        row -- Row position of grid eg: 0, 1, 2 ...
        column -- column position of grid eg: 0, 9, 27 ...
        """
        for row_block in xrange(3):
            self.verify_number_in_column_block(row, column, row_block, first_number, second_number)
        self.grid[self.first_param_in_axis_x][self.first_param_in_axis_y] = second_number
        self.grid[self.second_param_in_axis_x][self.second_param_in_axis_y] = first_number

    def verify_number_in_column_block(self, row, column, row_block, first_number, second_number):
        """Verify if the number is equal than in the grid position, if yes the positions is stored
         and verify the second number is equal in grid position, if yes the position is stored in order
         to get a success swap both numbers in its positions.

        Keyword arguments:
        first_number -- Random number between 1 and 9
        second_number -- Random number between 1 and 9
        row -- Row position of grid eg: 0, 1, 2 ...
        column -- column position of grid eg: 0, 9, 27 ...
        row_block -- Get a row of current block eg: 9, 10, 11 ...
        """
        for column_block in xrange(3):
            if self.grid[row + row_block][column + column_block] == first_number:
                self.first_param_in_axis_x = row + row_block
                self.first_param_in_axis_y = column + column_block
            if self.grid[row + row_block][column + column_block] == second_number:
                self.second_param_in_axis_x = row + row_block
                self.second_param_in_axis_y = column + column_block

    def start_shuffle(self, shuffle_level):
        """Start with shuffle the positions in grid according level that define how many times it will be shuffled

        Keyword arguments:
        shuffle_level -- Random number between 10 and 20
        """
        for repeat in xrange(shuffle_level):
            self.get_shuffle_two_cells(random.randint(1, 9), random.randint(1, 9))

    def change_format_grid_to_array(self):
        """Copy the grid into array to get a standard output of game.
        """
        for row in xrange(9):
            for column in xrange(0, 9):
                self.board.append(self.grid[row][column])

    def set_level(self, board):
        """Define the level of game according threshold defined in configuration file, set 0s to be guess
        and hints array
        """
        level = random.randint(self.min_threshold, self.max_threshold)
        init_level = 0
        while init_level < level:
            position = random.randint(0, 80)
            if board[position] != 0:
                self.hints.append((position, board[position]))
                board[position] = 0
                init_level += 1
        self.board = board