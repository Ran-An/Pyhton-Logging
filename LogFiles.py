"""
@Author: Ran An
Date: 2019-05-13
"""

import logging
import sys
import config_log as cfg


class LogFiles:
    """
        This module generate log files and store them in the specified folder
            The steps are as follow:
                1.Pass the path into where the log files to be stored
                2.Setup a file handler to write the log files in the specified folder
                3.Setup a logger, then add the handler to the logger
            Methods:
                1. MyLogger: Generate log files and store them in the specified folder
            Input/Attributes:
                s_path: the path where are the log files will be stored
    """

    def __init__(self, s_path):
        self.s_path = s_path
    
    def MyLogger(self, log_name, info_message, formats = cfg.formatter, date_format = cfg.dateformat, D=None):
        """
            Create log files and store them in specified folder
                The steps are as follow:
                    1.Setup a file handler to write the log files in the specified folder
                    2.Create a formatter and add the formatter to handler
                    3.Setup a logger and add handler to logger
                Args:
                    log_name: the name of the log file
                    formats: the format of the formatter
                    date_format: the date format
                    info_message: the message in the log file
                    D: the extra information to be wrote in the log file

                Exception:
                    Errors that happened during processing, and generate a log file in path folder with program name.

                Returns:None
        """
        try:
            step = "1. Setup a file handler to write the log files in the specified folder"
            loghandler = logging.FileHandler(filename=self.s_path + log_name, mode='w')

            step = "1.2. Add formatter to handler"
            FORMAT = logging.Formatter(formats, datefmt=date_format)
            loghandler.setFormatter(FORMAT) 

            step = "2. Setup a logger name and logger level"
            log = logging.getLogger(__name__)
            # log = logging.getLogger(p_file) ------ if use this, a p_file (logger name) parameter need to be added
            log.setLevel(logging.DEBUG)

            step = "3. Add handler to logger"
            log.addHandler(loghandler)

            step = "4. log information into log file"
            log.info(info_message, extra=D)

        except Exception:
            class_method = self.__class__.__name__ + "." + sys._getframe().f_code.co_name
            raise Exception("Class.Method: " + class_method +
                            "\n\tERROR: Step " + str(step) + " \n\tERROR:" + str(sys.exc_info()[0]) +
                            "\n\tERROR:" + str(sys.exc_info()[1]) + "\n\tERROR:" + str(sys.exc_info()[2]))
