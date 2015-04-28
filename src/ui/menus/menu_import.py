# menu_import.py
# author: Josue Mendoza
# date: 4-25-2015

from configuration.configuration import CONFIGURATION_FILE_PATH
from configuration.configuration import Configuration
from file_manager.file_manager import File
from utils.data_converter import DataConverter
from utils.singleton import Singleton
from menu import Menu
from game import Game
from board import Board
from ui.menus.menu_game import MenuGame

import Tkinter
import tkFileDialog
import os


class MenuImport(object):

    __metaclass__ = Singleton

    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    blank_character = configuration.blank_character
    converter = DataConverter()

    def display_import_menu(self, display_main_menu):
        """Sub menu of Main,this function provide to user options to manage the configuration of application
        in order to support changes and persistent configuration.
        Define a menu object that is provided with Title, Description and
        items, it calls an ask function in order to get an option selected by user.
        display_main_menu -- is the main menu object that will be eventually called.
        """
        game = Game()
        board = Board()
        submenu = MenuGame()
        menu = Menu('Sudoku Solver - Import Game')
        menu.clear_items()
        menu.add_item((1, 'Import from CSV File', self.import_from_csv_file, (display_main_menu, game, board, submenu)))
        menu.add_item((2, 'Import from TXT File', self.import_from_txt_file, (display_main_menu, game, board, submenu)))
        menu.add_item((3, 'Import from Input', self.import_from_input, display_main_menu))
        menu.add_item((4, 'Back', display_main_menu, 0))
        menu.add_item((0, 'Exit', None))
        menu.ask()

    def import_from_csv_file(self, param):
        """
        Imports a game from a file in csv format (i.e. 123456789,123456789,123...)
        display_main_menu -- is the main menu object that will be eventually called.
        """
        file_types = [('CSV files', '*.csv'), ('All files', '*')]
        file_to_be_imported = self.file_browser_dialog(file_types)
        if file_to_be_imported.file_exists():
            self.store_last_used_folder(file_to_be_imported.file_path)
            file_content = file_to_be_imported.read_content()
            imported_game = self.converter.convert_csv_string_to_game_list(file_content, self.blank_character)
            imported_game = [int(numeric_string) for numeric_string in imported_game]
            param[1].import_game(imported_game)
            param[2].board = param[1].board
            param[3].play_game((2, param[0]))
        else:
            self.display_import_menu(param[0])

    def import_from_txt_file(self, param):
        """
        Imports a game from a file in txt format.
        display_main_menu -- is the main menu object that will be eventually called.
        """
        file_types = [('Text files', '*.txt'), ('All files', '*')]
        file_to_be_imported = self.file_browser_dialog(file_types)
        if file_to_be_imported.file_exists():
            self.store_last_used_folder(file_to_be_imported.file_path)
            file_content = file_to_be_imported.read_content()
            imported_game = self.converter.convert_txt_string_to_game_list(file_content, self.blank_character)
            imported_game = [int(numeric_string) for numeric_string in imported_game]
            param[1].import_game(imported_game)
            param[2].board = param[1].board
            param[3].play_game((2, param[0]))
        else:
            self.display_import_menu(param[0])

    def import_from_input(self, display_main_menu):
        """
        Imports a game from a the console input (i.e. 1234567879986343...)
        display_main_menu -- is the main menu object that will be eventually called.
        """
        input_content = raw_input('Enter the game to be imported: ')
        if len(input_content) == 81:
            imported_game = self.converter.convert_input_string_to_game_list(input_content, self.blank_character)
            print imported_game
        else:
            self.display_import_menu(display_main_menu)

    def file_browser_dialog(self, file_types):
        """
        Uses Tkinter to launch an File Browser that will select a specific file.
        It returns the file selected in a File object.
        file_types -- An array of tuples containing the files allowed by the file
        browser (i.e. [('Text files', '*.txt'), ('All files', '*')])
        """
        root = Tkinter.Tk()
        root.withdraw()
        folder = self.configuration.file_path_save

        file_path = tkFileDialog.askopenfilename(initialdir=folder, filetypes=file_types, multiple=False)
        file_to_be_imported = File(file_path)
        return file_to_be_imported

    def store_last_used_folder(self, last_used_file_path):
        """
        Stores the folder container for the last successfully file selected by the file_browser_dialog
        method in the configuration file.
        Returns True if the folder path was stored successfully in the configuration, otherwise False.
        last_used_file_path -- a string containing the folder path to be validated and stored.
        """
        folder_path = os.path.dirname(os.path.abspath(last_used_file_path))
        if os.path.exists(folder_path):
            self.configuration.file_path_save = folder_path
            self.config_file.write_content(self.configuration.get_xml_as_string())
            return True
        else:
            return False