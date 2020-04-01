"""
@Author: Ran An
Date: 2019-05-13
"""

import logging
import time
import LogFiles as lg
import config_log as cfg
import sys

if __name__ == "__main__":

    step = "1. Define parameters in LogFiles.MyLogger method"
    curr_time = time.strftime('%Y-%m-%d-%H%M', time.localtime(time.time()))
    logger_name = 'logging ' + curr_time + '.log'
    messages = 'This is an info message'

    try:
        step = "2. Instantiate LogFiles class to identify the path"
        a_log = lg.LogFiles(cfg.file_store_path)

        step = "3. Pass the parameters into the MyLogger method"
        Gene_log = a_log.MyLogger(logger_name, messages)
        
        Message = "Successful: Run Complete " + __file__

    except:
        Message = "Failed: Running " + __file__
        logging.basicConfig(filename=cfg.file_store_path + logger_name, level=logging.DEBUG)
        logging.exception("ERROR: " + __file__ + "\n    ERROR: Step " + str(step) +
                          " \n    ERROR:" + str(sys.exc_info()[0]) + "\n\tERROR:" + str(sys.exc_info()[1]) +
                          "\n\tERROR:" + str(sys.exc_info()[2]) + "\n" + Message, exc_info=False)

        
        print("ERROR: " + __file__ + "\n    ERROR: Step " + str(step) +
              "\n    ERROR:" + str(sys.exc_info()[0]) + "\n\tERROR:" + str(sys.exc_info()[1]) +
              "\n\tERROR:" + str(sys.exc_info()[2]))
    
    finally:
        print(Message)
        sys.exit()
