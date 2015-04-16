# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from configuration.configuration import *
from file_manager.file_manager import *
from menu import Menu
from game import *
from board import *


def main_menu():
    menu = Menu('Sudoku Solver')
    menu.text = "Sudoku is a puzzle game designed for\na single player, much like a crossword puzzle."
    menu.clear_items()
    menu.add_item((1, 'Configuration Game', config_menu))
    menu.add_item((2, 'Start Game', game_menu))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def config_menu():
    menu = Menu('Sudoku Solver - Config Section')
    menu.clear_items()
    menu.add_item((1, 'Select Level', config_menu ))
    menu.add_item((2, 'Select Algorithm', config_menu ))
    menu.add_item((3, 'Print Config File', print_config_file ))
    menu.add_item((4, 'Print Config Level', print_level_file))
    menu.add_item((5, 'Back', main_menu ))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def print_config_file():
    os.system('cls')
    print ('Print Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.get_xml_as_string())
    raw_input('\n\nPress any key: ')
    config_menu()


def print_level_file():
    os.system('cls')
    print ('Print Level of Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.level)
    raw_input('\n\nPress any key: ')
    config_menu()


def game_menu():
    menu = Menu('Sudoku Solver - Game Section')
    menu.clear_items()
    menu.add_item((1, 'Start New Game', game))
    menu.add_item((2, 'Import Game', game_menu))
    menu.add_item((3, 'Back', main_menu))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def game():
    os.system('cls')
    sudoku_game = Game(20, 30)
    sudoku_game.generate_game()
    board = Board(sudoku_game.board, chr(178))
    board.print_ui()
    c = len(sudoku_game.hints)
    print("Missing numbers: %i \n" % c)
    for x in sudoku_game.hints:
        sudoku_game.board[x[0]] = x[1]
    board.print_board()
    raw_input('\n\nPress any key: ')
    game_menu()

main_menu()