# menu_config.py
# author: Josue Mendoza
# date: 4-23-2015

from configuration.configuration import CONFIGURATION_FILE_PATH
from configuration.configuration import Configuration
from file_manager.file_manager import *
from menu import Menu
from utils.singleton import Singleton


class MenuConfig(object):

    __metaclass__ = Singleton

    def display_configuration_menu(self, display_main_menu):
        """
        Sub menu of Main menu, this function provides the user options to manage
        the configuration of the application.
        In order to support changes and persistent configuration.
        Define a menu object that is provided with Title, Description and
        items. It calls an ask function in order to get an option selected by user.
        display_main_menu -- is the main menu object that will be eventually called.
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = self.get_formatted_configuration()
        menu.clear_items()
        menu.add_item((1, 'Modify Level', self.modify_level_menu, display_main_menu))
        menu.add_item((2, 'Modify Blank Character', self.modify_blank_character_menu, display_main_menu))
        menu.add_item((3, 'Modify Algorithm', self.modify_algorithm_menu, display_main_menu))
        menu.add_item((4, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()


    def get_formatted_configuration(self):
        """
        Returns a string containing the configuration data formatted
        so it has the indentation the menu has.
        """
        config_file = File(CONFIGURATION_FILE_PATH)
        configuration = Configuration(config_file.read_content())
        level_list = configuration.level.split(':')
        config_txt = '    Configuration:\n    ==============\n' + \
                     '    Level: ' + level_list[0] + \
                     '    (Min: ' + level_list[1] + \
                     '    Max: ' + level_list[2] + ')\n' + \
                     '    Blank Character: ' + chr(int(configuration.blank_character)) + '\n' + \
                     '    Algorithm: ' + configuration.algorithm
        return config_txt


    def modify_level_menu(self, display_main_menu):
        """
        Displays the corresponding menu for modifying the level in the
        configuration.
        display_main_menu -- is the main menu object that will be eventually called
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new level for the game:'
        menu.clear_items()
        menu.add_item((1, 'Easy', self.modify_configuration, ('level', 'Easy:10:20', display_main_menu)))
        menu.add_item((2, 'Medium', self.modify_configuration, ('level', 'Medium:30:40', display_main_menu)))
        menu.add_item((3, 'Hard', self.modify_configuration, ('level', 'Hard:40:50', display_main_menu)))
        menu.add_item((4, 'Custom', self.modify_custom_level_menu, display_main_menu))
        menu.add_item((5, 'Back', self.display_configuration_menu, display_main_menu))
        menu.add_item((0, 'Exit', None))
        menu.ask()


    def modify_custom_level_menu(self, display_main_menu):
        """
        Displays the corresponding menu for modifying the custom level in the
        configuration.
        display_main_menu -- is the main menu object that will be eventually called
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new level for the game:'
        menu.clear_items()

        config_file = File(CONFIGURATION_FILE_PATH)
        configuration = Configuration(config_file.read_content())
        custom_level_list = configuration.custom_level_defaults.split(':')
        default_min = custom_level_list[1]
        default_max = custom_level_list[2]

        try:
            min_val = int(input("Please enter the minimum number of blank spaces "
                                "(Current: " + default_min + "): "))
            max_val = int(input("Please enter the maximum number of blank spaces "
                                "(Current: " + default_max + "): "))
            if (min_val < max_val) and (min_val >= 10) and (max_val <= 81):
                custom_level_string = 'Custom:' + str(min_val) + ':' + str(max_val)
                self.modify_configuration(('level', custom_level_string, display_main_menu))
        except Exception:
            print "Invalid values entered"
        self.display_configuration_menu(display_main_menu)


    def modify_blank_character_menu(self, display_main_menu):
        """
        Displays the corresponding menu for modifying the custom blank character in the
        configuration.
        display_main_menu -- is the main menu object that will be eventually called
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new level for the game:'
        menu.clear_items()
        blank_char = str(raw_input('Enter an ASCII character that will be used as separator: '))
        if self.validate_blank_char(blank_char):
            try:
                char_code = str(ord(blank_char))
                self.modify_configuration(('blank_character', char_code, display_main_menu))
            except Exception:
                print "Invalid character"
        self.display_configuration_menu(display_main_menu)


    def validate_blank_char(self, blank_char):
        """
        Returns True if the blank character is entered as parameter is not a forbidden one.
        blank_char -- a string containing the custom blank character to be saved by another method.
        """
        result = True
        not_allowed_chars = [',', '<', '>', '"', '\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for char in not_allowed_chars:
            if char == blank_char:
                result = False
        try:
            if ord(blank_char) > 128:
                result = False
        except:
            print "Invalid character"
        return result


    def modify_algorithm_menu(self, display_main_menu):
        """
        Displays the corresponding menu for modifying the algorithm in the configuration.
        display_main_menu -- is the main menu object that will be eventually called
        """
        menu = Menu('Sudoku Solver - Configuration')
        menu.text = 'Select the new algorithm for the game:'
        menu.clear_items()
        menu.add_item((1, 'NorvigSolver', self.modify_configuration, ('algorithm', 'Norvig', display_main_menu)))
        menu.add_item((2, 'BackTracking', self.modify_configuration, ('algorithm', 'BackTrack', display_main_menu)))
        menu.add_item((3, 'BruteForce', self.modify_configuration, ('algorithm', 'BruteForce', display_main_menu)))
        menu.add_item((4, 'Back', self.display_configuration_menu, display_main_menu))
        menu.add_item((0, 'Exit', None))
        menu.ask()


    def modify_configuration(self, config_data):
        """
        Modifies the configuration based on a tuple retrieved as an argument.
        Modifications are persisted in the configuration xml file.
        Keyword Arguments:
        config_data -- a tuple containing strings in the positions 0 and 1, these strings contain the
        setting name and the new value; the position 2 contains the display_main_menu object which is
        the main menu object that will be eventually called.
        """
        config_file = self.File(CONFIGURATION_FILE_PATH)
        setting = config_data[0]
        new_value = config_data[1]
        display_main_menu = config_data[2]
        configuration = Configuration(config_file.read_content())
        setattr(configuration, setting, new_value)
        if 'Custom:' in new_value:
            setattr(configuration, 'custom_level_defaults', new_value)
        config_file.write_content(configuration.get_xml_as_string())
        self.display_configuration_menu(display_main_menu)