# import_export.py
# author: Josue Mendoza
# date: 4-22-2015


def import_game_from_csv_string(csv_string, blank_character_code):
    """
    Based on a csv formatted string it will return a list which is the standard
    format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
    If the csv string is not valid it will return None.
    csv_string -- csv content as a string, it should have 81 items (i.e. 0,0,3,0,...)
    blank_character_code -- is an integer containing the ASCII code of a character to
    be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
    """
    blank_character = chr(int(blank_character_code))
    csv_string = str.replace(csv_string, blank_character, '0')
    if len(csv_content_to_list(csv_string)) == 81:
        return csv_content_to_list(csv_string)
    else:
        return None


def csv_content_to_list(csv_file_content):
    """
    Returns a list containing the comma separated items retrieved from the csv_string
    parameter (i.e. ['0', '0', '3', '0',...])
    csv_file_content -- csv content as a string, it should have 81 items (i.e. 0,0,3,0,...)
    """
    return csv_file_content.split(",")


def import_game_from_txt_string(txt_string, blank_character_code):
    """
    Based on a txt formatted string it will return a list which is the standard
    format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
    If the txt string is not valid it will return None.
    txt_string -- the txt file content as a string, it should have 81 characters separated
    by a new line character every 9 characters (i.e. 200080300\n060070084\n030500209...)
    blank_character_code -- is an integer containing the ASCII code of a character to
    be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
    """
    blank_character = chr(int(blank_character_code))

    txt_string = str.replace(txt_string, blank_character, '0')
    if validate_txt_lines(txt_string):
        txt_string = str.replace(txt_string, '\n', '')
        return list(txt_string)
    else:
        return None


def validate_txt_lines(txt_content):
    """
    Returns True if the lines have the proper format to be handled by the program
    otherwise it returns False
    txt_content -- the txt file content as a string, it should have 81 characters separated
    by a new line character every 9 characters (i.e. 200080300\n060070084\n030500209...)
    """
    result = True
    txt_lines = txt_content.split('\n')

    for line in txt_lines:
        if len(line) != 9:
            result = False
    if len(txt_lines) != 9:
        result = False
    return result


def import_game_from_input_string(input_string, blank_character_code):
    """
    Based on a string retrived using the raw_input method it will return a list which
    is the standard format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
    If the txt string is not valid it will return None.
    input_string -- the input retrieved as a string, it should have 81 characters (i.e. 2000803...)
    blank_character_code -- is an integer containing the ASCII code of a character to
    be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
    """
    blank_character = chr(int(blank_character_code))

    input_string = list(str.replace(input_string, blank_character, '0'))
    if len(input_string) == 81:
        return input_string
    else:
        return None


def export_to_csv_string(game_list_to_export, blank_character_code):
    """
    Returns a csv formatted string containing the game board digits as items
    game_list_to_export -- it is a list containing the game board (i.e. 0,0,3,0,...)
    blank_character_code -- is an integer containing the ASCII code of a character to
    be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
    """
    blank_character = chr(int(blank_character_code))
    csv_string = ','.join(game_list_to_export)
    csv_string = str.replace(csv_string, '0', blank_character)
    return csv_string


def export_to_txt_string(game_list_to_export, blank_character_code):
    """
    Returns a 81 characters string separated by a new line character every 9
    characters (i.e. 200080300\n060070084\n030500209...)
    game_list_to_export -- it is a list containing the game board (i.e. 0,0,3,0,...)
    blank_character_code -- is an integer containing the ASCII code of a character to
    be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
    """
    blank_character = chr(int(blank_character_code))
    cells_string = ''.join(game_list_to_export)
    result = ''
    counter = 1
    for cell in cells_string:
        result += cell
        if counter == 9:
            result += '\n'
            counter = 0
        counter += 1
    result = result[:-1]
    result = str.replace(result, '0', blank_character)
    return result