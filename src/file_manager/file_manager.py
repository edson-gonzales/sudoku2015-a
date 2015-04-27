# file_manager.py
# author: Josue Mendoza
# date: 4-2-2015

import os

class File(object):
    """File instance objects have as the only attribute the file path of a file.

    Attributes are:
    file_path: a string containing the full path of the file related to the File
    instance. (i.e. C:\sudoku\files\file_1.txt)
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_content(self):
        """Uses native python implementations to read files,
        it also handles IOError related exceptions.

        It uses the file_path attribute (absolute file path) of the given
        File instance

        It returns a string containing the content read
        """
        file_content = ''

        try:
            fo = open(self.file_path)
            file_content = fo.read()
        except IOError:
            raise IOError('cannot read file')
        finally:
            fo.close()

        return file_content

    def write_content(self, file_content):
        """Uses native python implementations to write content to files,
        it also handles IOError related exceptions.

        It uses the file_path attribute (absolute file path) of the given
        File instance

        Keyword arguments:
        file_content -- the string that contains the content to be written
        """
        result = True

        try:
            fo = open(self.file_path, "wb")
            fo.write(file_content)
        except IOError:
            raise IOError('cannot write content to file')
            result = False
        finally:
            fo.close()

        return result

    def delete(self):
        """Uses native python implementations to delete the file related
        to the File instance.

        It uses the file_path attribute (absolute file path) of the given
        File instance
        """
        os.remove(self.file_path)
        return not os.path.exists(self.file_path)

    def file_exists(self):
        """Uses native python implementations to identify the file related
        to the File instance exists or not.

        It uses the file_path attribute (absolute file path) of the given
        File instance

        It returns a boolean stating wether the file exists or not
        """
        return os.path.exists(self.file_path)