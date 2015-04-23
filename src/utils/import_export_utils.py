# configuration_manager.py
# author: Josue Mendoza
# date: 4-22-2015

import sys

sys.path.append("..")

from file_manager.file_manager import *
from configuration.configuration import *

CONFIGURATION_FILE_PATH = '..\\configuration\\xml_config.xml'
config_file = File(CONFIGURATION_FILE_PATH)
configuration = Configuration(config_file.read_content())


def import_game_from_csv(file_path):
    game_in_file_format = File(file_path)
    blank_character = chr(int(configuration.blank_character))

    csv_content = game_in_file_format.read_content()
    csv_content = str.replace(csv_content, blank_character, '0')
    if len(csv_content_to_list(csv_content)) == 81:
        print csv_content_to_list(csv_content) #################################################################
        return True
    else:
        return False


def csv_content_to_list(csv_file_content):
    return csv_file_content.split(",")


def import_game_from_txt(file_path):
    game_in_file_format = File(file_path)
    blank_character = chr(int(configuration.blank_character))

    txt_content = game_in_file_format.read_content()
    txt_content = str.replace(txt_content, blank_character, '0')
    if validate_lines(txt_content):
        txt_content = str.replace(txt_content, '\n', '')
        print list(txt_content) ################################################################################
        return True
    else:
        return False


def validate_lines(txt_content):
    result = True
    txt_lines = txt_content.split('\n')

    for line in txt_lines:
        if len(line) != 9:
            result = False
    if len(txt_lines) != 9:
        result = False
    return result


def import_game_from_input():
    blank_character = chr(int(configuration.blank_character))

    input_content = str(raw_input("\nPlease enter game content to be imported: "))
    input_content = list(str.replace(input_content, blank_character, '0'))
    if len(input_content) == 81:
        print input_content ################################################################################
        return True
    else:
        return False


def export_to_csv(game_list, file_path):
    blank_character = chr(int(configuration.blank_character))
    csv_string = ','.join(game_list)
    csv_string = str.replace(csv_string, '0', blank_character)
    exported_game_file = File(file_path)
    exported_game_file.write_content(csv_string)
    print csv_string


def export_to_txt(game_list, file_path):
    blank_character = chr(int(configuration.blank_character))
    cells_string = ''.join(game_list)
    result = ''
    counter = 1
    for cell in cells_string:
        result = result + cell
        if counter == 9:
            result = result + '\n'
            counter = 0
        counter += 1
    result = result[:-1]
    result = str.replace(result, '0', blank_character)
    exported_game_file = File(file_path)
    exported_game_file.write_content(result)
    print result



import_game_from_csv('D:\\test.txt')
import_game_from_txt('D:\\test2.txt')
import_game_from_input()

game_list = ['1', '2', '3', '5', '4', '6', '7', '8', '9', '0', '5', '0', '0', '0', '0', '7', '1', '2', '3', '5', '4', '6', '7', '8', '9', '0', '5', '0', '0', '0', '0', '7', '1', '2', '3', '5', '4', '6', '7', '8', '9', '0', '5', '0', '0', '0', '0', '7', '1', '2', '3', '5', '4', '6', '7', '8', '9', '0', '5', '0', '0', '0', '0', '7', '1', '2', '3', '5', '4', '6', '7', '8', '9', '0', '5', '0', '0', '0', '0', '7', '1']

export_to_csv(game_list, 'D:\\t1.csv')
export_to_txt(game_list, 'D:\\t2.txt')