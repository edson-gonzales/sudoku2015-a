# menu_game.py
# author: Daniel Jauergui
# date: 4-23-2015

from main import display_main_menu
from menu import Menu
from game import *
from board import *


def game_menu():
    """Sub Menu of Main menu that provide option for user in order to manage the geme.
    It will call display_config_menu function after press any key.
    Define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver - Game Section')
    menu.clear_items()
    menu.add_item((1, 'Start/Continue Game', play_game, 0))
    menu.add_item((2, 'New Game', play_game, 1))
    menu.add_item((3, 'Import Game', game_menu, 0))
    menu.add_item((4, 'Export Game', game_menu, 0))
    menu.add_item((5, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def play_game(mode=0):
    """This function provide to the user a game interface with menus, board and input request.

    Keyword arguments:
    mode -- Define if game should be generated again or continue with previous status, values (0=ContinueGame,1=NewGame)
    """
    if mode == 1:
        sudoku_game = Game(20, 30)
        sudoku_game.generate_game()
        board = Board('*')
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
        board.get_resolved_game()
    board = Board('*')
    sudoku_game = Game(20, 30)

    if len(board.board) == 81:
        sudoku_game.board = board.board
        sudoku_game.hints = board.hints
    else:
        sudoku_game.generate_game()
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
        board.get_resolved_game()
    option = None
    while option != 'E':
        os.system('cls')
        board.print_ui()
        missing_numbers = len(board.hints)
        print("Missing numbers: %i \n" % missing_numbers)
        if board.board == board.resolved:
            print("Congratulations! you did it. Sudoku solved successfully\n")
        elif board.board.count(0) == 0:
            print("The solution is not correct, pleas see below in solved game an compare:\n")
            board.print_board(board.resolved)
        option = raw_input("Enter coordinates: ")
        if option.upper() == 'N':
            play_game(1)
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