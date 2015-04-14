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
    def display(self):
        slicers=[0,9] #slice points
        row_counter=0 #counts row to know when to place double line
        for i in range(9): #for all the rows
            RP=self.board[slicers[0]:slicers[1]] #sliced board
            if row_counter in (3,6):
                print("---------------------------------------")
                print("---------------------------------------")
            else:
                print("---------------------------------------")
            print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(RP[0],RP[1],RP[2],RP[3],RP[4],RP[5],RP[6],RP[7],RP[8]))
            row_counter+=1 #update counter
            slicers[0]+=9 #update slicers
            slicers[1]+=9 #update slicers
        print("---------------------------------------")

    def print_top_menu(self):

        # Top Menu
        top_menu = ''
        top_menu += chr(201)
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
        top_menu += chr(186)+' N:NewGame '+chr(186)+' H:Hints '+chr(186)+' M:Home '+chr(186)+' E:Exit '+chr(186) + '\n'
        top_menu += chr(200)
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

        board_ui =  '  ' + chr(186)+' 1 '+chr(186)+' 2 '+chr(186)+' 3 '+chr(186)+' 4 '+chr(186)+' 5 '+chr(186)+' 6 '+chr(186)+' 7 '+chr(186)+' 8 '+chr(186)+' 9 '+chr(186) + '\n'
        board_ui += '  ' + chr(201)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            board_ui += chr(203)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(187) + '\n'
        for y in xrange(8):
            board_ui += '  ' + chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186) + '\n'
            board_ui += '  ' + chr(204)
            for n in xrange(8):
                for l in xrange(3):
                    board_ui += chr(205)
                board_ui += chr(206)
            board_ui += chr(205) + chr(205) + chr(205)
            board_ui += chr(185) + '\n'
        board_ui +=  '  ' + chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186)+'   '+chr(186) + '\n'
        board_ui += '  ' + chr(200)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            board_ui += chr(202)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(188) + '\n'
        print board_ui