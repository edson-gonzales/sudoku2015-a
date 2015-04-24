# test_configuration.py
# author: Josue Mendoza
# date: 4-5-2015

import unittest
import os

from import_export import *


class ImportExportTest(unittest.TestCase):
    TEST_FOLDER = os.getcwd() + '\\test_folder'
    TEST_CONFIG_FILE = TEST_FOLDER + '\\test_config_file.xml'

    BLANK_CHARACTER_CODE_SAMPLE = '42' # 42 is the code for the star sign: '*'
    BLANK_CHAR_SAMPLE = chr(int(BLANK_CHARACTER_CODE_SAMPLE))


    GAME_1_CSV_STRING = '0,0,3,0,2,0,6,0,0,9,0,0,3,0,5,0,0,1,0,0,1,8,0,6,4,0,0,0,0,' \
                        '8,1,0,2,9,0,0,7,0,0,0,0,0,0,0,8,0,0,6,7,0,8,2,0,0,0,0,2,6,' \
                        '0,9,5,0,0,8,0,0,2,0,3,0,0,9,0,0,5,0,1,0,3,0,0'
    GAME_1_CSV_CUSTOM_BLANK_CHAR = str.replace(GAME_1_CSV_STRING, '0', BLANK_CHAR_SAMPLE)

    GAME_1_STRING = '0030206009003050010018064000081029007000000080067082000026095' \
                    '00800203009005010300'
    GAME_1_LIST = list(GAME_1_STRING)

    GAME_2_TXT_STRING = '200080300\n060070084\n030500209\n000105408\n000000000\n' \
                        '402706000\n301007040\n720040060\n004010003'
    GAME_2_TXT_CUSTOM_BLANK_CHAR = str.replace(GAME_2_TXT_STRING, '0', BLANK_CHAR_SAMPLE)

    GAME_2_STRING = '2000803000600700840305002090001054080000000004027060003010070' \
                    '40720040060004010003'
    GAME_2_LIST = list(GAME_2_STRING)

    GAME_3_INPUT_STRING = '0000009070004201800007050261009040000500000400005070099' \
                          '20108000034059000507000000'
    GAME_3_INPUT_CUSTOM_BLANK_CHAR = str.replace(GAME_3_INPUT_STRING, '0', BLANK_CHAR_SAMPLE)

    GAME_3_LIST = list(GAME_3_INPUT_STRING)


    GAME_1_CSV_STRING_1_ITEM_LESS = GAME_1_CSV_STRING[:-2]

    GAME_2_TXT_STRING_1_ITEM_LESS = GAME_2_TXT_STRING[:-1]

    GAME_3_INPUT_STRING_1_ITEM_LESS = GAME_3_INPUT_STRING[:-1]



    if not os.path.exists(TEST_FOLDER):
        os.makedirs(TEST_FOLDER)

    def test_import_from_csv_string_can_import_a_game_from_a_csv_string(self):
        imported_game = import_game_from_csv_string(self.GAME_1_CSV_STRING,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_1_LIST)

    def test_import_from_txt_string_can_import_a_game_from_a_txt_string(self):
        imported_game = import_game_from_txt_string(self.GAME_2_TXT_STRING,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_2_LIST)

    def test_import_from_input_string_can_import_a_game_from_an_input_string(self):
        imported_game = import_game_from_input_string(self.GAME_3_INPUT_STRING,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_3_LIST)


    def test_import_from_csv_string_returns_None_when_the_game_cannot_be_imported(self):
        imported_game = import_game_from_txt_string(self.GAME_1_CSV_STRING_1_ITEM_LESS,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertIsNone(imported_game)

    def test_import_from_txt_string_returns_None_when_the_game_cannot_be_imported(self):
        imported_game = import_game_from_txt_string(self.GAME_2_TXT_STRING_1_ITEM_LESS,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertIsNone(imported_game)

    def test_import_from_input_returns_None_when_the_game_cannot_be_imported(self):
        imported_game = import_game_from_input_string(self.GAME_3_INPUT_STRING_1_ITEM_LESS,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertIsNone(imported_game)


    def test_import_from_csv_string_can_import_a_game_from_a_csv_string_with_custom_blank_character(self):
        imported_game = import_game_from_csv_string(self.GAME_1_CSV_CUSTOM_BLANK_CHAR,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_1_LIST)

    def test_import_from_txt_string_can_import_a_game_from_a_txt_string_with_custom_blank_character(self):
        imported_game = import_game_from_txt_string(self.GAME_2_TXT_CUSTOM_BLANK_CHAR,
                                                    self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_2_LIST)

    def test_import_from_input_string_can_import_a_game_from_an_input_string_with_custom_blank_character(self):
        imported_game = import_game_from_input_string(self.GAME_3_INPUT_CUSTOM_BLANK_CHAR,
                                                      self.BLANK_CHARACTER_CODE_SAMPLE)
        self.assertEqual(imported_game, self.GAME_3_LIST)


    def test_export_to_csv_string_can_export_a_game_to_a_csv_string(self):
        blank_character = chr(int(self.BLANK_CHARACTER_CODE_SAMPLE))
        exported_game = export_to_csv_string(self.GAME_1_LIST, self.BLANK_CHARACTER_CODE_SAMPLE)
        expected_csv_string = str.replace(self.GAME_1_CSV_STRING, '0', blank_character)
        self.assertEqual(exported_game, expected_csv_string)

    def test_export_to_txt_string_can_export_a_game_to_a_csv_string(self):
        blank_character = chr(int(self.BLANK_CHARACTER_CODE_SAMPLE))
        exported_game = export_to_txt_string(self.GAME_2_LIST, self.BLANK_CHARACTER_CODE_SAMPLE)
        expected_txt_string = str.replace(self.GAME_2_TXT_STRING, '0', blank_character)
        self.assertEqual(exported_game, expected_txt_string)
