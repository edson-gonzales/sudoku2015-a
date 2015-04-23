# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015

from utils.menu_config import *
from utils.menu_game import *
from menu import Menu


def display_main_menu():
    """As part of UI this is the first function called and displayed for users,
    define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver')
    menu.text = "Sudoku is a puzzle game designed for\na single player, much like a crossword puzzle."
    menu.clear_items()
    menu.add_item((1, 'Start Game', display_game_menu, display_main_menu))
    menu.add_item((2, 'Game Configuration', display_configuration_menu, display_main_menu))
    menu.add_item((0, 'Exit', None))
    menu.ask()

display_main_menu()