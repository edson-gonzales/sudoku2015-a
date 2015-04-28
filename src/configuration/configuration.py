# configuration_manager.py
# author: Josue Mendoza
# date: 4-2-2015

from xml.dom.minidom import *
from utils.singleton import Singleton
import os

CONFIGURATION_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '..\\..\\configuration\\xml_config.xml'

class Configuration(object):
    """Configuration instance object has attributes containing the
    configuration values and the raw xml as string.
    Attributes are:
    __raw_xml_configuration: a string containing the complete configuration xml
    level: a string containing the level of the game. (i.e. easy)
    algorithm: a string containing the algorithm to be used to solve the game if
    applicable. (i.e. peter_norvig)
    file_path_save: a string containing the default file path where games will
    be saved. (i.e. C:\sudoku\files\)
    custom_level_defaults: a string containing the default value for the default
    custom level. (i.e. 'Custom:15:40')
    """
    __metaclass__ = Singleton

    CONFIGURATION_NAME = 'configuration'
    LEVEL_NAME = 'level'
    BLANK_CHARACTER_NAME = 'blank_character'
    ALGORITHM_NAME = 'algorithm'
    FILE_PATH_SAVE_NAME = 'file_path_save'
    CUSTOM_LEVEL_DEFAULTS_NAME = 'custom_level_defaults'

    def __init__(self, xml_content=None):
        self.__raw_xml_configuration = xml_content
        self.level = self.get_value_from_raw_xml(self.LEVEL_NAME)
        self.blank_character = self.get_value_from_raw_xml(self.BLANK_CHARACTER_NAME)
        self.algorithm = self.get_value_from_raw_xml(self.ALGORITHM_NAME)
        self.file_path_save = self.get_value_from_raw_xml(self.FILE_PATH_SAVE_NAME)
        self.custom_level_defaults = self.get_value_from_raw_xml(self.CUSTOM_LEVEL_DEFAULTS_NAME)

    def get_value_from_raw_xml(self, xml_key):
        """Returns a value from a XML string based on the key sent as argument.
        Keyword arguments:
        xml_key -- the string that contains the xml data.
        """
        dom = parseString(self.__raw_xml_configuration)

        try:
            return dom.getElementsByTagName(xml_key)[0].childNodes[0].data
        except IndexError:
            raise IndexError("invalid configuration file, elements not found")

    def get_xml_as_string(self):
        """Retrieves all the attributes from a configuration instance, with the    data
        gathered it builds an XML and stores it into a string which is returned as result
        """
        doc = Document()
        config = doc.createElement(self.CONFIGURATION_NAME)
        level = doc.createElement(self.LEVEL_NAME)
        blank_character = doc.createElement(self.BLANK_CHARACTER_NAME)
        algorithm = doc.createElement(self.ALGORITHM_NAME)
        file_path_save = doc.createElement(self.FILE_PATH_SAVE_NAME)
        custom_level_defaults = doc.createElement(self.CUSTOM_LEVEL_DEFAULTS_NAME)

        level.appendChild(doc.createTextNode(self.level))
        blank_character.appendChild(doc.createTextNode(self.blank_character))
        algorithm.appendChild(doc.createTextNode(self.algorithm))
        file_path_save.appendChild(doc.createTextNode(self.file_path_save))
        custom_level_defaults.appendChild(doc.createTextNode(self.custom_level_defaults))

        doc.appendChild(config)
        config.appendChild(level)
        config.appendChild(blank_character)
        config.appendChild(algorithm)
        config.appendChild(file_path_save)
        config.appendChild(custom_level_defaults)

        return doc.toprettyxml()