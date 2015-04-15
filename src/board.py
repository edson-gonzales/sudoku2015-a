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
        if number is 0:
            return '*'
        return str(number)

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

    def print_top_menu(self):

        left_spaces = '          '
        # Top Menu
        top_menu = ''
        top_menu += left_spaces + chr(201)
        for line_vertical in xrange(11):
            top_menu += chr(205)
        top_menu += chr(203)
        for line_vertical in xrange(9):
            top_menu += chr(205)
        top_menu += chr(203)
        for line_vertical in xrange(8):
            top_menu += chr(205)
        top_menu += chr(203)
        for line_vertical in xrange(8):
            top_menu += chr(205)
        top_menu += chr(187) + '\n'
        top_menu += left_spaces + chr(186)+' N:NewGame '+chr(186)+' H:Hints '+chr(186)+' B:Back '+chr(186)+' E:Exit '+chr(186) + '\n'
        top_menu += left_spaces + chr(200)
        for line_vertical in xrange(11):
            top_menu += chr(205)
        top_menu += chr(202)
        for line_vertical in xrange(9):
            top_menu += chr(205)
        top_menu += chr(202)
        for line_vertical in xrange(8):
            top_menu += chr(205)
        top_menu += chr(202)
        for line_vertical in xrange(8):
            top_menu += chr(205)
        top_menu += chr(188) + '\n'
        print top_menu

        characters = ('A','B','C','D','E','F','G','H')
        board_ui = left_spaces + '   ' + '  1 '+'  2 '+'  3 '+'  4 '+'  5 '+'  6 '+'  7 '+'  8 '+'  9 '+'\n'
        board_ui += left_spaces +'   ' + chr(201)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            board_ui += chr(203)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(187) + '\n'
        for y in xrange(8):
            board_ui += left_spaces +' '+characters[y]+' ' + chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186) + '\n'
            board_ui += left_spaces +'   ' + chr(204)
            for n in xrange(8):
                for l in xrange(3):
                    board_ui += chr(205)
                board_ui += chr(206)
            board_ui += chr(205) + chr(205) + chr(205)
            board_ui += chr(185) + '\n'
        board_ui += left_spaces +'   ' + chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186) + '\n'
        board_ui += left_spaces +'   ' + chr(200)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            board_ui += chr(202)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(188) + '\n'
        print board_ui