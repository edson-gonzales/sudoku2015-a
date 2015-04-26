# game_resources.py
# author: Daniel Jauergui
# date: 4-25-2015

from configuration.configuration import *
from utils.algorithm_solver import *
from file_manager.file_manager import *
from solver.algorithms.norvig_solver import NorvigSolver
# from solver.algorithms.backtraking_solver import Backtraking
# from solver.algorithms.bruteforce_solver import Bruteforce

PATH = os.path.dirname(os.path.abspath(__file__))

CONFIGURATION_FILE_PATH = PATH + '..\\..\\configuration\\xml_config.xml'


def return_result_of_validation(value, board):
    if value is False:
        raw_input("\nOperation cancelled or position does exist. (press any key to continue)...")
        return board
    else:
        if board[value[0]] == 0:
            board[value[0]] = value[1]
        else:
            raw_input("\nPosition contains a number, please select another position. (press any key to continue)...")
        return board


def verify_value_defined(key):
    list_positions = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9",
                      "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9",
                      "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
                      "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
                      "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
                      "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9",
                      "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
                      "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9",
                      "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"]
    current_position = None
    number = None
    for position in xrange(len(list_positions)):
        if list_positions[position] == key.upper():
            current_position = position
    if current_position is not None:
        while number not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            number = raw_input("\nPlease enter a number (1-9): ")
    if number is None or int(number) == 0:
        return False
    else:
        return int(current_position), int(number)


def call_algorithm_to_solve(board):
    algorithm = ""
    code = "algorithm = " + get_algorithm_solver() + "()"
    exec code
    algorithm_to_solve = AlgorithmSolver(algorithm)
    return algorithm_to_solve.solve(board)


def get_level_configuration():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    range_of_level = configuration.level
    range_of_level = range_of_level.split(":")
    try:
        min = range_of_level[1]
        max = range_of_level[2]
    except:
        min = 20
        max = 30
    return min, max


def get_blank_character():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    blank_character = configuration.blank_character
    try:
        blank_character = int(blank_character)
    except:
        blank_character = 42
    return blank_character


def get_algorithm_solver():
    config_file = File(CONFIGURATION_FILE_PATH)
    configuration = Configuration(config_file.read_content())
    return str(configuration.algorithm)