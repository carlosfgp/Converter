from Converter import Converter
import logging

class Logger():

    def logger(moduleName,fileName=Converter.CI_LOGS_FILEPATH,formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s',debugLevel=logging.INFO):
        log = logging.getLogger(moduleName)

        log.setLevel(debugLevel)
        formatter = logging.Formatter(formatter)
        file_handler = logging.FileHandler(fileName)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
        return log
