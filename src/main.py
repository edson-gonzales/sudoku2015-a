# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from configuration.configuration import *
from file_manager.file_manager import *
from menu import Menu
from game import *
from board import *


def display_main_menu():
    menu = Menu('Sudoku Solver')
    menu.text = "Sudoku is a puzzle game designed for\na single player, much like a crossword puzzle."
    menu.clear_items()
    menu.add_item((1, 'Start Game', game_menu, 0))
    menu.add_item((2, 'Configuration Game', display_config_menu,0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def display_config_menu():
    menu = Menu('Sudoku Solver - Config Section')
    menu.clear_items()
    menu.add_item((1, 'Select Level', display_config_menu,0))
    menu.add_item((2, 'Select Algorithm', display_config_menu,0))
    menu.add_item((3, 'Print Config File', print_config_file,0))
    menu.add_item((4, 'Print Config Level', print_level_file,0))
    menu.add_item((5, 'Back', display_main_menu,0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def print_config_file():
    os.system('cls')
    print ('Print Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.get_xml_as_string())
    raw_input('\n\nPress any key: ')
    display_config_menu()


def print_level_file():
    os.system('cls')
    print ('Print Level of Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.level)
    raw_input('\n\nPress any key: ')
    display_config_menu()


def game_menu():
    menu = Menu('Sudoku Solver - Game Section')
    menu.clear_items()
    menu.add_item((1, 'Start Game', game,0))
    menu.add_item((2, 'New Game', game,1))
    menu.add_item((3, 'Import Game', game_menu,0))
    menu.add_item((4, 'Export Game', game_menu,0))
    menu.add_item((5, 'Back', display_main_menu,0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def game(mode=0):
    if mode == 1:
        sudoku_game = Game(20, 30)
        sudoku_game.generate_game()
        board = Board(chr(178))
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
    board = Board(chr(178))
    sudoku_game = Game(20, 30)
    if len(board.board) == 81:
        sudoku_game.board = board.board
        sudoku_game.hints = board.hints
    else:
        sudoku_game.generate_game()
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
    option = None
    while option != 'E':
        os.system('cls')
        board.print_ui()
        c = len(board.hints)
        print("Missing numbers: %i \n" % c)
        option = raw_input("Enter coordinates: ")
        if option.upper() == 'N':
            game(1)
            break
        elif option.upper() == 'E':
            break
        elif option.upper() == 'B':
            game_menu()
            break
        elif option.upper() == 'H':
            board.set_hint()
        else:
            raw_input("Implement movement, please press enter to continue...")

display_main_menu()