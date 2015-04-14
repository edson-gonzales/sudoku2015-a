# board.py
# author: Daniel Jauergui
# date: 4-13-2015

import os
from utils.singleton import Singleton


class Board(object):

    #__metaclass__ = Singleton

    def __init__(self, board=None):
        self.board = board

    def print_code(self, number):
        if number is None:
            return '*'
        return str(number + 1)

    def print_board(self):
        out = '-----------------------\n'
        y = 8
        for matrix in xrange(81):
            out += self.print_code(self.board[matrix]) + ' '
            if (matrix % 3) == 2:
                    out += "| "
            if matrix == y:
                    out += '\n'
                    if ((matrix >= 19) and (matrix <= 27)) or ((matrix >= 45) and (matrix <= 54)):
                            out += '------+-------+--------\n'
                    y += 9
        out += '-----------------------\n'
        return out
