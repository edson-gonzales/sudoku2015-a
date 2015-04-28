import os
import logging
import sys
sys.path.append("../utils")
from singleton import Singleton


class LoggerAdmin(object):

    __metaclass__ = Singleton

    def __init__(self,log_file_path, log_file_name="logger.log"):
        """
        Initialize attibutes
        log_file_path -- the path where .log file is stored,
        log_file_name -- the name of .log file by default logger        
        """
        self.log_file_path = log_file_path
        file_handler = self.get_file_handler(log_file_name)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_file_handler(self, log_file_name):
        """
        The method will convert the log_file_name in a absolute path
        log file name -- name of log file
        """
        self.log_file_abs_path = os.path.abspath(self.log_file_path + log_file_name)
        filehandler = logging.FileHandler(self.log_file_abs_path, 'a')
        return filehandler

    def debug(self, message):
        """
        This method will create a log entry into the log file for a debug message
        message -- debug description
        """
        self.logger.debug(message)

    def warning(self, message):
        """
        This method will create a log entry into the log file for a warning message
        message -- warning description
        """
        self.logger.warning(message)

    def critical(self, message):
        """
        This method will create a log entry into the log file for a critical message
        message -- critical description
        """
        self.logger.critical(message)

    def error(self, message):
        """
        This method will create a log entry into the log file for a error message
        message -- error description
        """
        self.logger.error(message)

    def info(self, message):
        """
        This method will create a log entry into the log file for a informational message
        message -- info description
        """
        self.logger.info(message)

    def get_log(self):
        """
        Return the content of the log
        """
        open_file = open(self.log_file_abs_path, 'r')
        read_log = open_file.read()
        open_file.close()
        return str(read_log)
    
    def clear_log(self):
        """
        Clear whole content of the log
        """
        open_file = open(self.log_file_abs_path, 'w')
        open_file.truncate()
        open_file.close()