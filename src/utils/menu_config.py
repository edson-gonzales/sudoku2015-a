# menu_config.py
# author: Daniel Jauergui
# date: 4-23-2015

from main import display_main_menu
from menu import Menu
from configuration.configuration import *
from file_manager.file_manager import *

CONFIGURATION_FILE_PATH = 'configuration\\xml_config.xml'

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