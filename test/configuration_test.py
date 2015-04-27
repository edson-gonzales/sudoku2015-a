# test_configuration.py
# author: Josue Mendoza
# date: 4-5-2015

import unittest
import os

from configuration import Configuration
from file_manager import File


class ConfigurationTest(unittest.TestCase):
    TEST_FOLDER = os.getcwd() + '\\test_folder'
    TEST_CONFIG_FILE = TEST_FOLDER + '\\test_config_file.xml'

    SAMPLE_LEVEL = 'Custom:10:20'
    SAMPLE_BLANK_CHARACTER = '42'
    SAMPLE_ALGORITHM = 'norvigs'
    SAMPLE_FILE_PATH = 'D:\\'
    SAMPLE_CUSTOM_LEVEL_DEFAULTS = 'Custom:30:50'

<<<<<<< HEAD
    XML_SAMPLE = '<?xml version="1.0" ?><configuration>' \
                 + '<level>' + SAMPLE_LEVEL + '</level>' \
                 + '<blank_character>' + SAMPLE_BLANK_CHARACTER + '</blank_character>' \
                 + '<algorithm>' + SAMPLE_ALGORITHM + '</algorithm>' \
                 + '<file_path_save>' + SAMPLE_FILE_PATH + '</file_path_save>' \
                 + '<file_name_save>' + SAMPLE_FILE_NAME + '</file_name_save>' \
                 + '</configuration>'
=======
    XML_SAMPLE = '<?xml version="1.0" ?><configuration>'\
        + '<level>' + SAMPLE_LEVEL + '</level>' \
        + '<blank_character>' + SAMPLE_BLANK_CHARACTER + '</blank_character>' \
        + '<algorithm>' + SAMPLE_ALGORITHM + '</algorithm>'\
        + '<file_path_save>' + SAMPLE_FILE_PATH + '</file_path_save>'\
        + '<custom_level_defaults>' + SAMPLE_CUSTOM_LEVEL_DEFAULTS + '</custom_level_defaults>'\
        + '</configuration>'
>>>>>>> master

    if not os.path.exists(TEST_FOLDER):
        os.makedirs(TEST_FOLDER)

    def test_just_one_instance_of_configuration_can_be_created(self):
        file_instance = File(self.TEST_CONFIG_FILE)
        file_instance.write_content(self.XML_SAMPLE)
        configuration_instance_a = Configuration(file_instance.read_content())
        configuration_instance_b = Configuration(file_instance.read_content())
        self.assertEqual(configuration_instance_a, configuration_instance_b)
        file_instance.delete()

    def test_configuration_instances_have_correct_values_in_attributes(self):
        file_instance = File(self.TEST_CONFIG_FILE)
        file_instance.write_content(self.XML_SAMPLE)
        configuration_instance = Configuration(file_instance.read_content())
        self.assertEqual(self.SAMPLE_LEVEL, configuration_instance.level)
        self.assertEqual(self.SAMPLE_ALGORITHM, configuration_instance.algorithm)
        self.assertEqual(self.SAMPLE_FILE_PATH, configuration_instance.file_path_save)
        self.assertEqual(self.SAMPLE_CUSTOM_LEVEL_DEFAULTS, configuration_instance.custom_level_defaults)

    def test_configuration_can_be_retrieved_as_xml(self):
        file_instance = File(self.TEST_CONFIG_FILE)
        file_instance.write_content(self.XML_SAMPLE)
        configuration_instance = Configuration(file_instance.read_content())

        raw_xml_sample = self.XML_SAMPLE.strip("\n").strip("\t").replace("\n", "").replace("\t", "")
        raw_retrieved_xml = configuration_instance.get_xml_as_string().strip("\n").strip("\t").replace("\n", "").replace("\t", "")

        self.assertEqual(raw_xml_sample, raw_retrieved_xml)
