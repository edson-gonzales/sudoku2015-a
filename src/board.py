# board.py
# author: Daniel Jauergui
# date: 4-13-2015

import os
from utils.singleton import Singleton


class Board(object):

    __metaclass__ = Singleton

    def __init__(self, code='*', board=[], hints=[]):
        self.board = board
        self.code = code
        self.hints = hints
        self.resolved = []

    def set_hint(self):
        """Set hints into board
        """
        for x in self.hints:
            if self.board[x[0]] == 0:
                self.board[x[0]] = x[1]
                break

    def get_resolved_game(self):
        """Using a board of this object is generated a resolved game in 'resolved' variable
        to compare with user game.
        """
        self.resolved = []
        for x in xrange(81):
            self.resolved.append(self.board[x])
        for x in self.hints:
            if self.resolved[x[0]] == 0:
                self.resolved[x[0]] = x[1]

    def print_ui(self):
        """ Print the title, Menus and Board
        """
        os.system('cls')
        self.print_title()
        self.print_top_menu()
        self.print_board(self.board)

    def concat_character_list(self, character_list):
        """Concat for each character from parameter into string variable
        Keyword arguments:
        character_list -- Get an array of number, eg: [219, 219, ..., 32, 32]
        return -- an string with all character joined
        """
        title = ''
        for character in character_list:
            title += chr(character)
        return title

    def print_title(self):
        """ Print the title
        """
        spaces = '      '
        title = '\n' + spaces
        list_character = [219, 219, 219, 219, 219, 219, 219, 187, 219, 219, 187, 32, 32, 32, 219, 219, 187, 219,
                          219, 219, 219, 219, 219, 187, 32, 32, 219, 219, 219, 219, 219, 219, 187, 32, 219, 219,
                          187, 32, 32, 219, 219, 187, 219, 219, 187, 32, 32, 32, 219, 219, 187]
        title += self.concat_character_list(list_character) + '\n' + spaces
        list_character = [219, 219, 201, 205, 205, 205, 205, 188, 219, 219, 186, 32, 32, 32, 219, 219, 186, 219,
                          219, 201, 205, 205, 219, 219, 187, 219, 219, 201, 205, 205, 205, 219, 219, 187, 219, 219,
                          186, 32, 219, 219, 201, 188, 219, 219, 186, 32, 32, 32, 219, 219, 186]
        title += self.concat_character_list(list_character) + '\n' + spaces
        list_character = [219, 219, 219, 219, 219, 219, 219, 187, 219,219, 186, 32, 32, 32, 219, 219, 186, 219,
                          219, 186, 32, 32, 219, 219, 186, 219, 219, 186, 32, 32, 32, 219, 219, 186, 219, 219,
                          219, 219, 219, 201, 188, 32, 219, 219, 186, 32, 32, 32, 219, 219, 186]
        title += self.concat_character_list(list_character) + '\n' + spaces
        list_character = [200, 205, 205, 205, 205, 219, 219, 186, 219, 219, 186, 32, 32, 32, 219, 219, 186, 219,
                          219, 186, 32, 32, 219, 219, 186, 219, 219, 186, 32, 32, 32, 219, 219, 186, 219, 219,
                          201, 205, 219, 219, 187, 32, 219, 219, 186, 32, 32, 32, 219, 219, 186]
        title += self.concat_character_list(list_character) + '\n' + spaces
        list_character = [219, 219, 219, 219, 219, 219, 219, 186, 200, 219, 219, 219, 219, 219, 219, 201, 188, 219,
                          219, 219, 219, 219, 219, 201, 188, 200, 219, 219, 219, 219, 219, 219, 201, 188, 219, 219,
                          186, 32, 32, 219, 219, 187, 200, 219, 219, 219, 219, 219, 219, 201, 188]
        title += self.concat_character_list(list_character) + '\n' + spaces
        list_character = [200, 205, 205, 205, 205, 205, 205, 188, 32, 200, 205, 205, 205, 205, 205, 188, 32, 200,
                          205, 205, 205, 205, 205, 188, 32, 32, 200, 205, 205, 205, 205, 205, 188, 32, 200, 205,
                          188, 32, 32, 200, 205, 188, 32, 200, 205, 205, 205, 205, 205, 188, 32]
        title += self.concat_character_list(list_character) + '\n'
        print title

    def print_top_menu(self):
        """ Print the top menu
        """
        left_spaces = '     '
        top_menu = left_spaces + chr(201)
        top_menu += self.add_chr_to_string(chr(205), 11) + chr(203) + self.add_chr_to_string(chr(205), 9) + chr(203)
        top_menu += self.add_chr_to_string(chr(205), 11) + chr(203)
        top_menu += self.add_chr_to_string(chr(205), 8) + chr(203) + self.add_chr_to_string(chr(205), 8)
        top_menu += chr(187) + '\n' + left_spaces + chr(186) + ' N:NewGame ' + chr(186) + ' H:Hints '
        top_menu += chr(186) + ' R:Resolve ' + chr(186)+' B:Back ' + chr(186) + ' E:Exit ' + chr(186) + '\n'
        top_menu += left_spaces + chr(200) + self.add_chr_to_string(chr(205), 11) + chr(202)
        top_menu += self.add_chr_to_string(chr(205), 9) + chr(202)
        top_menu += self.add_chr_to_string(chr(205), 11) + chr(202) + self.add_chr_to_string(chr(205), 8) + chr(202)
        top_menu += self.add_chr_to_string(chr(205), 8) + chr(188) + '\n'
        print top_menu

    def add_chr_to_string(self, character, size):
        """ Concat the characters according cells and block of sudoku board
        """
        menu = ''
        for x in xrange(size):
            menu += character
        return menu

    def add_chr_each_block(self, character1, character2, character3, size):
        """ Concat the characters according blocks of sudoku board
        """
        menu = ''
        for n in xrange(size):
            menu += self.add_chr_to_string(character1, 3)
            if n == 2 or n == 5:
                menu += character2
            else:
                menu += character3
        return menu

    def add_chr_each_row(self, size, board):
        """ Concat the characters according blocks of sudoku board
        """
        menu = ''
        position = 0
        characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        left_spaces = '          '
        for y in xrange(size):
            menu += left_spaces + ' ' + characters[y]+' ' + chr(186)+' ' + str(board[position]) + ' ' + chr(179)
            menu += ' ' + str(board[position+1]) + ' '+chr(179)+' ' + str(board[position+2]) + ' ' + chr(186)
            menu += ' ' + str(board[position+3]) + ' '+chr(179)+' ' + str(board[position+4]) + ' ' + chr(179)
            menu += ' ' + str(board[position+5]) + ' '+chr(186)+' ' + str(board[position+6]) + ' ' + chr(179)
            menu += ' ' + str(board[position+7]) + ' '+chr(179)+' ' + str(board[position+8]) + ' ' + chr(186) + '\n'
            menu += left_spaces + '   ' + chr(204)
            position += 9
            if y == 2 or y == 5:
                menu += self.add_chr_each_block(chr(205), chr(206), chr(205), 8) + chr(205) + chr(205) + chr(205)
                menu += chr(185) + '\n'
            else:
                menu += self.add_chr_each_block(chr(196), chr(206), chr(197),8) + chr(196) + chr(196) + chr(196)
                menu += chr(185) + '\n'
        return menu

    def print_board(self, board):
        """ Print the Board
        """
        left_spaces = '          '
        board_ui = left_spaces + '   ' + '  1 '+'  2 '+'  3 '+'  4 '+'  5 '+'  6 '+'  7 '+'  8 '+'  9 '+'\n'
        board_ui += left_spaces + '   ' + chr(201) + self.add_chr_each_block(chr(205), chr(203), chr(205), 8)
        board_ui += chr(205) + chr(205) + chr(205) + chr(187) + '\n'
        board_ui += self.add_chr_each_row(8, board)
        board_ui += left_spaces + ' I ' + chr(186) + ' ' + str(board[72]) + ' ' + chr(179) + ' '
        board_ui += str(board[73]) + ' ' + chr(179) + ' ' + str(board[74]) + ' ' + chr(186)
        board_ui += ' ' + str(board[75]) + ' ' + chr(179) + ' ' + str(board[76]) + ' '
        board_ui += chr(179) + ' ' + str(board[77]) + ' ' + chr(186) + ' ' + str(board[78])
        board_ui += ' '+chr(179)+' ' + str(board[79]) + ' ' + chr(179) + ' ' + str(board[80])
        board_ui += ' ' + chr(186) + '\n'
        board_ui += left_spaces + '   ' + chr(200)
        board_ui += self.add_chr_each_block(chr(205), chr(202), chr(205), 8)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(188) + '\n'
        print board_ui.replace("0", self.code)