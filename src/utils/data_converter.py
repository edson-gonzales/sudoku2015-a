# data_converter.py
# author: Josue Mendoza
# date: 4-22-2015

from singleton import Singleton


class DataConverter(object):
    """
    DataConverter instance object has methods that allow the conversion from
    the game format to csv or txt and vice versa.
    """
    __metaclass__ = Singleton

    def convert_csv_string_to_game_list(self, csv_string, blank_character_code):
        """
        Based on a csv formatted string it will return a list which is the standard
        format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
        If the csv string is not valid it will return None.
        Keyword arguments:
        csv_string -- csv content as a string, it should have 81 items (i.e. 0,0,3,0,...)
        blank_character_code -- is an integer containing the ASCII code of a character to
        be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
        """
        blank_character = chr(int(blank_character_code))
        csv_list = csv_string.split(",")
        for item in csv_list:
            if len(item) != 9:
                return None
        plain_txt_string = ''.join(csv_list)
        plain_txt_string = str.replace(plain_txt_string, blank_character, '0')
        game_list = list(plain_txt_string)
        if self.validate_final_list(game_list):
            return game_list
        else:
            return None

    def convert_txt_string_to_game_list(self, txt_string, blank_character_code):
        """
        Based on a txt formatted string it will return a list which is the standard
        format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
        If the txt string is not valid it will return None.
        Keyword arguments:
        txt_string -- the txt file content as a string, it should have 81 characters separated
        by a new line character every 9 characters (i.e. 200080300\n060070084\n030500209...)
        it can also be in the exported txt format which is a plus :)
        blank_character_code -- is an integer containing the ASCII code of a character to
        be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
        """
        blank_character = chr(int(blank_character_code))

        txt_string = str.replace(txt_string, blank_character, '0')
        txt_string = str.replace(txt_string, ' ', '')
        txt_string = str.replace(txt_string, '|', '')
        txt_string = str.replace(txt_string, '-', '')
        txt_string = str.replace(txt_string, '+', '')
        txt_string = str.replace(txt_string, '\r', '')
        txt_string = str.replace(txt_string, '\n\n', '\n')

        if self.validate_txt_lines(txt_string):
            txt_string = str.replace(txt_string, '\n', '')
            if self.validate_final_list(txt_string):
                return list(txt_string)
            else:
                return None
        else:
            return None

    def validate_txt_lines(self, txt_content):
        """
        Returns True if the lines have the proper format to be handled by the program
        otherwise it returns False
        Keyword arguments:
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

    def convert_input_string_to_game_list(self, input_string, blank_character_code):
        """
        Based on a string retrived using the raw_input method it will return a list which
        is the standard format to be used as a sudoku board game (i.e. ['0', '0', '3', '0',...])
        If the txt string is not valid it will return None.
        Keyword arguments:
        input_string -- the input retrieved as a string, it should have 81 characters (i.e. 2000803...)
        blank_character_code -- is an integer containing the ASCII code of a character to
        be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
        """
        blank_character = chr(int(blank_character_code))

        game_list = list(str.replace(input_string, blank_character, '0'))
        if self.validate_final_list(game_list):
            return game_list
        else:
            return None

    def convert_game_list_to_csv_string(self, game_list_to_export, blank_character_code):
        """
        Returns a csv formatted string containing the game board digits as items.
        Keyword arguments:
        game_list_to_export -- it is a list containing the game board (i.e. 0,0,3,0,...)
        blank_character_code -- is an integer containing the ASCII code of a character to
        be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
        """
        blank_character = chr(int(blank_character_code))
        csv_string = ''.join(game_list_to_export)
        csv_string = str.replace(csv_string, '0', blank_character)
        csv_string = self.add_character_every_x_characters(csv_string, ',', 9)
        return csv_string

    def convert_game_list_to_txt_string(self, game_list_to_export, blank_character_code):
        """
        Returns a sudoku board formatted string based on the arguments.
        Keyword arguments:
        game_list_to_export -- it is a list containing the game board (i.e. 0,0,3,0,...)
        blank_character_code -- is an integer containing the ASCII code of a character to
        be placed in the game as empty spots (i.e. 42 which represents the star sign '*')
        """
        blank_character = chr(int(blank_character_code))
        game_string = ''.join(game_list_to_export)
        game_string = str.replace(game_string, '0', blank_character)

        game_as_csv = self.add_character_every_x_characters(game_string, ',', 9)
        game_lines = game_as_csv.split(',')

        game_formatted = []

        for line in game_lines:
            line = self.add_character_every_x_characters(line, ' ', 1)
            line = line[:6] + '|' + line[6:12] + '|' + line[12:]
            game_formatted.append(line)

        game_formatted = ''.join(game_formatted)

        game_formatted = self.add_character_every_x_characters(game_formatted, '\n', 19)
        game_formatted = self.add_character_every_x_characters(game_formatted, '------+------+-----\n', 60, 0)
        game_formatted = str.replace(game_formatted, '\n', '\r\n')

        return game_formatted

    def add_character_every_x_characters(self, string_to_add_character, character, number_of_characters, trim=1):
        """
        Returns a string resultant from adding a specified character every specified characters.
        Keyword arguments:
        string_to_add_character -- string where the changes will occur (i.e. 'some random text')
        character -- a string containing the character to be added (i.e. '\n')
        number_of_characters -- an integer containing the number of characters between aditions (i.e. 9)
        trim -- the number of characters to be trimmed from the end of the string (default: 1)
        """
        result = ''
        counter = 1
        for cell in string_to_add_character:
            result += cell
            if counter == number_of_characters:
                result += character
                counter = 0
            counter += 1
        if trim > 0:
            result = result[:-trim]
        return result

    def validate_final_list(self, game_list):
        """
        Returns a boolean containing the result of the validation performed which consists in
        validating the list has length of 81, and the list is a list of integers.
        Keyword arguments:
        game_list -- the list containing the sudoku game data (i.e. ['0', '0', '3', '0',...])
        """
        result = True
        if len(game_list) != 81:
            result = False

        for item in game_list:
            try:
                int(item)
            except Exception:
                result = False
        return result