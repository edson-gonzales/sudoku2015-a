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
    print ('\n                         Sudoku Game')
    print ('                         """""" """"\n')
    sudoku_game = Game("easy")
    board = Board(sudoku_game.generate_game())
    print board.print_top_menu()
    # print board.print_board()
    c = 0
    for x in board.board:
        if x:
            c += 1
    c = 81 - c
    print("Missing numbers: %i" % c)
    raw_input('\n\nPress any key: ')
    game_menu()

main_menu()