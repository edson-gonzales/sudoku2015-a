# sudoku_solver.py
# author: Daniel Jauergui
# date: 3-31-2015


from configuration.configuration import *
from file_manager.file_manager import *
from menu import Menu
#from game import *
#from board import *

CONFIGURATION_FILE_PATH = 'configuration\\xml_config.xml'


def display_main_menu():
    """As part of UI this is the first function called and displayed for users,
    define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver')
    menu.text = "Sudoku is a puzzle game designed for\na single player, much like a crossword puzzle."
    menu.clear_items()
    menu.add_item((1, 'Start Game', game_menu, 0))
    menu.add_item((2, 'Game Configuration', display_configuration_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def display_configuration_menu():
    """Sub menu of Main,this function provide to user options to manage the configuration of application
    in order to support changes and persistent configuration.
    Define a menu object that is provided with Title, Description and
    items, it calls an ask function in order to get an option selected by user.
    """
    menu = Menu('Sudoku Solver - Configuration')
    menu.text = get_formatted_configuration()
    menu.clear_items()
    menu.add_item((1, 'Modify Level', modify_level_menu, 0))
    menu.add_item((2, 'Modify Algorithm', modify_algorithm_menu, 0))
    menu.add_item((3, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def get_formatted_configuration():
    """Returns a string containing the configuration data formatted
    so it has the indentation the menu has.
    """
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    config_txt = '    Configuration:\n    ==============\n' + \
                 '    Level: ' + configuration.level + '\n' + \
                 '    Algorithm: ' + configuration.algorithm
    return config_txt


def modify_level_menu():
    """Displays the corresponding menu for modifying the level in the
    configuration.
    """
    menu = Menu('Sudoku Solver - Configuration')
    menu.text = 'Select the new level for the game:'
    menu.clear_items()
    menu.add_item((1, 'Easy', modify_configuration, ('level', 'Easy')))
    menu.add_item((2, 'Medium', modify_configuration, ('level', 'Medium')))
    menu.add_item((3, 'Hard', modify_configuration, ('level', 'Hard')))
    menu.add_item((4, 'Custom', modify_configuration, ('level', 'Custom')))
    menu.add_item((5, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def modify_algorithm_menu():
    """Displays the corresponding menu for modifying the algorithm in the
    configuration.
    """
    menu = Menu('Sudoku Solver - Configuration')
    menu.text = 'Select the new algorithm for the game:'
    menu.clear_items()
    menu.add_item((1, 'Norvig', modify_configuration, ('algorithm', 'Norvig')))
    menu.add_item((2, 'BackTrack', modify_configuration, ('algorithm', 'BackTrack')))
    menu.add_item((3, 'BruteForce', modify_configuration, ('algorithm', 'BruteForce')))
    menu.add_item((4, 'Back', display_main_menu, 0))
    menu.add_item((0, 'Exit', None))
    menu.ask()


def modify_configuration(config_data):
    """Modifies the configuration based on a tuple retrieved as an argument.
    Modifications are persisted in the configuration xml file.
    Keyword Arguments:
    config_data -- a tuple of strings containing the setting name and the new value
    """
    config_file = File(CONFIGURATION_FILE_PATH)
    setting = config_data[0]
    new_value = config_data[1]
    configuration = Configuration(config_file.read_content())
    setattr(configuration, setting, new_value)
    config_file.write_content(configuration.get_xml_as_string())
    display_configuration_menu()


def print_config_file():
    """This function displays the XML information about current configuration.
    It will call display_config_menu function after press any key.
    """
    os.system('cls')
    print ('Print Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.get_xml_as_string())
    raw_input('\n\nPress any key: ')
    display_configuration_menu()


def print_level_file():
    """This function displays the value of level game that is getting from XML configuration.
    It will call display_config_menu function after press any key.
    """
    os.system('cls')
    print ('Print Level of Configuration file\n\n')
    file_obj = File('configuration/xml_config.xml')
    config = Configuration(file_obj.read_content())
    print (config.level)
    raw_input('\n\nPress any key: ')
    display_configuration_menu()


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
        board = Board(chr(178))
        board.board = sudoku_game.board
        board.hints = sudoku_game.hints
        board.get_resolved_game()
    board = Board(chr(178))
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
            print("Congratulations! you did it. Sudoku solved successfully")
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

display_main_menu()