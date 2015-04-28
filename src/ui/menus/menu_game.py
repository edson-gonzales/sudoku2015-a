# menu_game.py
# author: Daniel Jauergui
# date: 4-23-2015

from game import *
from board import *
from menu import Menu
from ui.menus.menu_import import *
from configuration import *
from utils.game_resources import *
import Tkinter
import tkFileDialog
import os


class MenuGame(object):

    __metaclass__ = Singleton

    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    blank_character = configuration.blank_character

    def display_game_menu(self, display_main_menu):
        """Sub Menu of Main menu that provide option for user in order to manage the geme.
        It will call display_config_menu function after press any key.
        Define a menu object that is provided with Title, Description and
        items, it calls an ask function in order to get an option selected by user.

        Keyword arguments:
        display_main_menu -- Get a address of father menu used in back option.
        """
        menu = Menu('Sudoku Solver - Game Section')
        menu.clear_items()
        menu.add_item((1, 'Start/Continue Game', self.play_game, (0, display_main_menu)))
        menu.add_item((2, 'New Game', self.play_game, (1, display_main_menu)))
        menu.add_item((3, 'Export Game (txt)', self.export_game_in_txt_format, display_main_menu))
        menu.add_item((4, 'Export Game (csv)', self.display_game_menu, display_main_menu))
        menu.add_item((9, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()

    def export_game_in_txt_format(self, display_main_menu):
        default_type = 'txt'
        file_to_export = self.save_file_dialog(default_type)
        data_converter = DataConverter()
        board = Board()
        c = [str(numeric_string) for numeric_string in board.board]
        game_formatted_as_string = data_converter.convert_game_list_to_txt_string(c, self.blank_character)
        file_to_export.write_content(game_formatted_as_string)
        self.display_game_menu(display_main_menu)

    def save_file_dialog(self, default_type):
        """
        Uses Tkinter to launch an File Browser that will select a specific file.
        It returns the file selected in a File object.
        file_types -- An array of tuples containing the files allowed by the file
        browser (i.e. [('Text files', '*.txt'), ('All files', '*')])
        """
        root = Tkinter.Tk()
        root.withdraw()
        folder = self.configuration.file_path_save
        file_path = tkFileDialog.asksaveasfilename(initialdir=folder, defaultextension=default_type)
        file_to_export = File(file_path)
        return file_to_export

    def play_game(self, mode):
        """This function provide to the user a game interface with menus, board and input request.

        Keyword arguments:
        mode -- Define if game should be generated again or continue with previous status,
        values (0=ContinueGame,1=NewGame)
        """
        self.verify_import_board(mode[0])
        game_resources = GameResources()
        sudoku_game = Game(game_resources.get_level_configuration())
        board = Board(chr(game_resources.get_blank_character()))
        if mode[0] == 1 or len(board.board) < 81:
            sudoku_game.generate_game()
            board.board = sudoku_game.board
            board.hints = sudoku_game.hints
            board.get_resolved_game()
        option = None
        while option != 'E':
            board.print_ui()
            result = self.verify_selected_option(board, game_resources)
            try:
                if result[1] == 'object':
                    board.board = result[0]
                else:
                    exec result[0]
                if result[1] == 'break':
                    break
            except:
                break

    def verify_import_board(self, mode):
        """Verify if boar was imported, if yes it resolve game using the algorithm and set hints.

        Keyword arguments:
        mode -- Get int number, if it is 2 game will be imported.
        return -- boolean if it was imported return true.
        """
        if mode != 2:
            return False
        sudoku_game = Game()
        board = Board()
        game_resources = GameResources()
        board.hints = []
        solved_board = game_resources.call_algorithm_to_solve(board)
        if solved_board.count(0) > 0:
            board.hints.append((0, 0))
            board.resolved = []
            return False
        for position in xrange(len(solved_board)):
            if board.board[position] == 0:
                board.hints.append((position, solved_board[position]))
        if len(board.hints) > 0:
            sudoku_game.hints = board.hints
        board.get_resolved_game()
        return True

    def verify_selected_option(self, board, game_resources):
        """This function verify the option introduced by user in order to executed an specific
        command.

        Keyword arguments:
        board -- Get board of game, Array of int eg:[8,6,2,0,...,9]
        return -- Return a tuple of command to execute or board result and flag
        """
        print("Missing numbers: %i" % board.board.count(0))
        option = raw_input("\nEnter menu option or board position (eg: D7): ")
        if board.board == board.resolved and option.upper() not in ['E', 'B', 'R', 'N']:
            return 'raw_input("\\nCongratulations! you did it. Sudoku solved successfully")', 'not_break'
        elif board.board.count(0) == 0 and option.upper() not in ['E', 'B', 'R', 'N']:
            print("\nThe solution is not correct, ")
            if len(board.resolved) == 81:
                print("please see below in solved game and compare:\n")
                board.print_board(board.resolved)
            return 'raw_input("\\n...(please press any key to continue)")', 'not_break'
        else:
            if option.upper() == 'N':
                return 'self.play_game((1, mode[1]))', 'break'
            elif option.upper() == 'E':
                return 'break', 'break'
            elif option.upper() == 'B':
                return 'self.display_game_menu(mode[1])', 'break'
            elif option.upper() == 'R':
                return 'board.board = game_resources.call_algorithm_to_solve(board)', 'not_break'
            elif option.upper() == 'H':
                return 'board.set_hint()', 'not_break'
            else:
                return game_resources.return_result_of_validation(game_resources.verify_value_defined(option),
                                                                  board.board), 'object'