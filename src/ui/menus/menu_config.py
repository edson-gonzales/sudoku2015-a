# menu_config.py
# author: Daniel Jauergui
# date: 4-23-2015

from configuration.configuration import *
from file_manager.file_manager import *
from menu import Menu

CONFIGURATION_FILE_PATH = 'configuration\\xml_config.xml'


class MenuConfig(object):

    __metaclass__ = Singleton

    def display_configuration_menu(self, display_main_menu):
        """Sub menu of Main,this function provide to user options to manage the configuration of application
        in order to support changes and persistent configuration.
        Define a menu object that is provided with Title, Description and
        items, it calls an ask function in order to get an option selected by user.
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = self.get_formatted_configuration()
        menu.clear_items()
        menu.add_item((1, 'Modify Level', self.modify_level_menu, display_main_menu))
        menu.add_item((2, 'Modify Algorithm', self.modify_algorithm_menu, display_main_menu))
        menu.add_item((9, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()

    def get_formatted_configuration(self):
        """Returns a string containing the configuration data formatted
        so it has the indentation the menu has.
        """
        config_file = File(CONFIGURATION_FILE_PATH)
        configuration = Configuration(config_file.read_content())
        config_txt = '    Configuration:\n    ==============\n' + \
                     '    Level: ' + configuration.level + '\n' + \
                     '    Algorithm: ' + configuration.algorithm
        return config_txt

    def modify_level_menu(self, display_main_menu):
        """Displays the corresponding menu for modifying the level in the
        configuration.
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new level for the game:'
        menu.clear_items()
        menu.add_item((1, 'Easy', self.modify_configuration, ('level', 'Easy', display_main_menu)))
        menu.add_item((2, 'Medium', self.modify_configuration, ('level', 'Medium', display_main_menu)))
        menu.add_item((3, 'Hard', self.modify_configuration, ('level', 'Hard', display_main_menu)))
        menu.add_item((4, 'Custom', self.modify_configuration, ('level', 'Custom', display_main_menu)))
        menu.add_item((9, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()

    def modify_algorithm_menu(self, display_main_menu):
        """Displays the corresponding menu for modifying the algorithm in the
        configuration.
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new algorithm for the game:'
        menu.clear_items()
        menu.add_item((1, 'Norvig', self.modify_configuration, ('algorithm', 'Norvig',display_main_menu)))
        menu.add_item((2, 'BackTrack', self.modify_configuration, ('algorithm', 'BackTrack', display_main_menu)))
        menu.add_item((3, 'BruteForce', self.modify_configuration, ('algorithm', 'BruteForce',display_main_menu)))
        menu.add_item((9, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()

    def modify_configuration(self, config_data):
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
        self.display_configuration_menu(config_data[2])