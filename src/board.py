# board.py
# author: Daniel Jauergui
# date: 4-13-2015


class Board(object):

    def __init__(self, board, code='*'):
        self.board = board
        self.code = code

    def print_ui(self):
        """ Print the title, Menus and Board
        """
        self.print_title()
        self.print_top_menu()
        self.print_board()

    def print_title(self):
        """ Print the title
        """
        spaces = '      '
        title = '\n' + spaces
        title += chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(187)+chr(219)+chr(219)+chr(187)
        title += chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(187)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)
        title += chr(219)+chr(187)+chr(32)+chr(32)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(187)
        title += chr(32)+chr(219)+chr(219)+chr(187)+chr(32)+chr(32)+chr(219)+chr(219)+chr(187)+chr(219)+chr(219)
        title += chr(187)+chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(187)+'\n'
        title += spaces
        title += chr(219)+chr(219)+chr(201)+chr(205)+chr(205)+chr(205)+chr(205)+chr(188)+chr(219)+chr(219)+chr(186)
        title += chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+chr(219)+chr(219)+chr(201)+chr(205)+chr(205)
        title += chr(219)+chr(219)+chr(187)+chr(219)+chr(219)+chr(201)+chr(205)+chr(205)+chr(205)+chr(219)+chr(219)
        title += chr(187)+chr(219)+chr(219)+chr(186)+chr(32)+chr(219)+chr(219)+chr(201)+chr(188)+chr(219)+chr(219)
        title += chr(186)+chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+'\n'
        title += spaces
        title += chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(187)+chr(219)+chr(219)+chr(186)
        title += chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+chr(219)+chr(219)+chr(186)+chr(32)+chr(32)
        title += chr(219)+chr(219)+chr(186)+chr(219)+chr(219)+chr(186)+chr(32)+chr(32)+chr(32)+chr(219)+chr(219)
        title += chr(186)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(201)+chr(188)+chr(32)+chr(219)+chr(219)
        title += chr(186)+chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+'\n'
        title += spaces
        title += chr(200)+chr(205)+chr(205)+chr(205)+chr(205)+chr(219)+chr(219)+chr(186)+chr(219)+chr(219)+chr(186)
        title += chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+chr(219)+chr(219)+chr(186)+chr(32)+chr(32)+chr(219)
        title += chr(219)+chr(186)+chr(219)+chr(219)+chr(186)+chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)
        title += chr(219)+chr(219)+chr(201)+chr(205)+chr(219)+chr(219)+chr(187)+chr(32)+chr(219)+chr(219)+chr(186)
        title += chr(32)+chr(32)+chr(32)+chr(219)+chr(219)+chr(186)+'\n'
        title += spaces
        title += chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(186)+chr(200)+chr(219)+chr(219)
        title += chr(219)+chr(219)+chr(219)+chr(219)+chr(201)+chr(188)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)
        title += chr(219)+chr(201)+chr(188)+chr(200)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(201)
        title += chr(188)+chr(219)+chr(219)+chr(186)+chr(32)+chr(32)+chr(219)+chr(219)+chr(187)+chr(200)+chr(219)
        title += chr(219)+chr(219)+chr(219)+chr(219)+chr(219)+chr(201)+chr(188)+'\n'
        title += spaces
        title += chr(200)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(188)+chr(32)+chr(200)+chr(205)
        title += chr(205)+chr(205)+chr(205)+chr(205)+chr(188)+chr(32)+chr(200)+chr(205)+chr(205)+chr(205)+chr(205)
        title += chr(205)+chr(188)+chr(32)+chr(32)+chr(200)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(188)
        title += chr(32)+chr(200)+chr(205)+chr(188)+chr(32)+chr(32)+chr(200)+chr(205)+chr(188)+chr(32)+chr(200)
        title += chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(188)+chr(32)+'\n'
        print title

    def print_top_menu(self):
        """ Print the top menu
        """
        left_spaces = '           '
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
        top_menu += left_spaces + chr(186) + ' N:NewGame ' + chr(186) + ' H:Hints '
        top_menu += chr(186)+' B:Back ' + chr(186) + ' E:Exit ' + chr(186) + '\n'
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

    def print_board(self):
        """ Print the Board
        """
        for x in xrange(81):
            if self.board[x] == 0:
                self.board[x] = self.code
        left_spaces = '          '
        characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        board_ui = left_spaces + '   ' + '  1 '+'  2 '+'  3 '+'  4 '+'  5 '+'  6 '+'  7 '+'  8 '+'  9 '+'\n'
        board_ui += left_spaces + '   ' + chr(201)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            if n == 2 or n == 5:
                board_ui += chr(203)
            else:
                board_ui += chr(205)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(187) + '\n'
        position = 0
        for y in xrange(8):
            board_ui += left_spaces + ' ' + characters[y]+' ' + chr(186)+' ' + str(self.board[position])
            board_ui += ' '+chr(179)
            board_ui += ' ' + str(self.board[position+1]) + ' '+chr(179)+' ' + str(self.board[position+2])
            board_ui += ' ' + chr(186)
            board_ui += ' ' + str(self.board[position+3]) + ' '+chr(179)+' ' + str(self.board[position+4])
            board_ui += ' ' + chr(179)
            board_ui += ' ' + str(self.board[position+5]) + ' '+chr(186)+' ' + str(self.board[position+6])
            board_ui += ' ' + chr(179)
            board_ui += ' ' + str(self.board[position+7]) + ' '+chr(179)+' ' + str(self.board[position+8])
            board_ui += ' ' + chr(186) + '\n'
            board_ui += left_spaces + '   ' + chr(204)
            position += 9
            if y == 2 or y == 5:
                for n in xrange(8):
                    for l in xrange(3):
                        board_ui += chr(205)
                    if n == 2 or n == 5:
                        board_ui += chr(206)
                    else:
                        board_ui += chr(205)
                board_ui += chr(205) + chr(205) + chr(205)
                board_ui += chr(185) + '\n'
            else:
                for n in xrange(8):
                    for l in xrange(3):
                        board_ui += chr(196)
                    if n == 2 or n == 5:
                        board_ui += chr(206)
                    else:
                        board_ui += chr(197)
                board_ui += chr(196) + chr(196) + chr(196)
                board_ui += chr(185) + '\n'

        board_ui += left_spaces + ' I ' + chr(186) + ' ' + str(self.board[position]) + ' ' + chr(179) + ' '
        board_ui += str(self.board[position+1]) + ' ' + chr(179) + ' ' + str(self.board[position+2]) + ' ' + chr(186)
        board_ui += ' ' + str(self.board[position+3]) + ' ' + chr(179) + ' ' + str(self.board[position+4]) + ' '
        board_ui += chr(179) + ' ' + str(self.board[position+5]) + ' ' + chr(186) + ' ' + str(self.board[position+6])
        board_ui += ' '+chr(179)+' ' + str(self.board[position+7]) + ' ' + chr(179) + ' ' + str(self.board[position+8])
        board_ui += ' ' + chr(186) + '\n'
        board_ui += left_spaces + '   ' + chr(200)
        for n in xrange(8):
            for l in xrange(3):
                board_ui += chr(205)
            if n == 2 or n == 5:
                board_ui += chr(202)
            else:
                board_ui += chr(205)
        board_ui += chr(205) + chr(205) + chr(205)
        board_ui += chr(188) + '\n'
        print board_ui