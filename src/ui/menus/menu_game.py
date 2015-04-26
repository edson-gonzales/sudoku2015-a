# menu_game.py
# author: Daniel Jauergui
# date: 4-23-2015

from game import *
from board import *
from menu import Menu
from utils.game_resources import *


def display_game_menu(display_main_menu):
    """Sub Menu of Main menu that provide option for user in order to manage the geme.
    It will call display_config_menu function after press any key.
    Define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver - Game Section')
    menu.clear_items()
    menu.add_item((1, 'Start/Continue Game', play_game, (0, display_main_menu)))
    menu.add_item((2, 'New Game', play_game, (1, display_main_menu)))
    menu.add_item((3, 'Import Game', display_game_menu, display_main_menu))
    menu.add_item((4, 'Export Game', display_game_menu, display_main_menu))
    menu.add_item((9, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def play_game(mode):
    """This function provide to the user a game interface with menus, board and input request.

    Keyword arguments:
    mode -- Define if game should be generated again or continue with previous status, values (0=ContinueGame,1=NewGame)
    """
    sudoku_game = Game(get_level_configuration())
    board = Board(chr(get_blank_character()))
    if mode[0] == 1 or len(board.board) < 81:
        sudoku_game.generate_game()
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
        board.get_resolved_game()
    option = None
    while option != 'E':
        os.system('cls')
        board.print_ui()
        missing_numbers = len(board.hints)
        print("Missing numbers: %i" % missing_numbers)
        if board.board == board.resolved:
            print("\nCongratulations! you did it. Sudoku solved successfully")
        elif board.board.count(0) == 0:
            print("\nThe solution is not correct, please see below in solved game and compare:\n")
            board.print_board(board.resolved)
        option = raw_input("\nEnter menu option or board position (eg: D7): ")
        if option.upper() == 'N':
            play_game((1, mode[1]))
            break
        elif option.upper() == 'E':
            break
        elif option.upper() == 'B':
            display_game_menu(mode[1])
            break
        elif option.upper() == 'R':
            board.board = call_algorithm_to_solve(board)
        elif option.upper() == 'H':
            board.set_hint()
        else:
            board.board = return_result_of_validation(verify_value_defined(option), board.board)