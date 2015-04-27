# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from ui.menus.menu_config import *
<<<<<<< HEAD
=======
from ui.menus.menu_import import *
>>>>>>> master
from ui.menus.menu_game import *
from menu import Menu


def display_main_menu():
    """As part of UI this is the first function called and displayed for users,
    define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu_game = MenuGame()
    menu_config = MenuConfig()
    menu_import = MenuImport()
    menu = Menu('Sudoku Solver')
    menu.text = "Sudoku is a puzzle game designed for\na single player, much like a crossword puzzle."
    menu.clear_items()
<<<<<<< HEAD
    menu.add_item((1, 'New Game', menu_game.display_game_menu, display_main_menu))
    menu.add_item((2, 'Import game', menu_import.display_import_menu, display_main_menu))
    menu.add_item((3, 'Game Configuration', menu_config.display_configuration_menu, display_main_menu))
=======
    menu.add_item((1, 'New Game', display_game_menu, display_main_menu))
    menu.add_item((2, 'Import game', display_import_menu, display_main_menu))
    menu.add_item((3, 'Game Configuration', display_configuration_menu, display_main_menu))
>>>>>>> master
    menu.add_item((0, 'Exit', None))
    menu.ask()

display_main_menu()