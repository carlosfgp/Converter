import logging

from configparser import ConfigParser


class Converter():
    
    ULDD_PATH_REQUEST_ID_PATH ="./catalog/catalognaNo"
    CI_RUNBOOKS_PATH = r"C:\Users\carlo\Runbooks"
    CI_LOGS_FILEPATH = r"C:\Users\carlo\projects\Python\Converter\Converter\Logs\converter.log"
    CI_TEST_DATA = r"C:\Users\carlo\TEST_DATA"
    TEMP_XLSX_PATH = r"C:\Users\carlo\projects\Python\Converter\Converter\tmp"
    TEMP_XLSX_FILE = r"temp.xlsx"
    ROOT_CI_DATA_FOLDER = r"C:\Users\carlo\TEST_DATA"
    FILE_SUFIX = "_CI.xlsx"
    CONFIG_LOCATION_AND_NAME = "config/ToscaToCIMapping.ini"
    RQ_IF = "config/RW_IF.ini"
    POSSIBLE_HEADERS = ["ActionType","__PosibleHeaders_Here"]
    HEADER = "HEADER"
    CREATE_CONFIG = False

    def __init__(self):
        self.__config__ = ConfigParser()
        self.__config__.read(Converter.CONFIG_LOCATION_AND_NAME)
        self.__configSections__ = self.__config__.sections()
        self.__log__ = Converter.logger(__name__, debugLevel=logging.DEBUG)
        self.__interfaceConfigData__ = ConfigParser()
        self.__interfaceConfigData__.read(Converter.RQ_IF)

    def secctionExist(self, stepType):
        if stepType in self.getSecctions():
            return True
        return False

    def getElementsFromSecction(self, section):
        elementsFromSeccion = []
        try:
            if self.secctionExist(section):
                for key, elements in self.__config__.items(section):
                    elementsFromSeccion.append(elements)
            else:
                self.__log__.debug(f"Section: {section} not found on config file{Converter.CONFIG_LOCATION_AND_NAME}",
                                   exc_info=True)
        except KeyError as exc:
            raise self.__log__.debug(f"Section: {section} not found on config file{Converter.CONFIG_LOCATION_AND_NAME}",
                                     exc_info=True)
        return elementsFromSeccion

    def getSecctions(self):
        return self.__configSections__

    def logger(moduleName, fileName=CI_LOGS_FILEPATH, formatter="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
               debugLevel=logging.INFO):
        log = logging.getLogger(moduleName)

        log.setLevel(debugLevel)
        formatter = logging.Formatter(formatter)
        file_handler = logging.FileHandler(fileName)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
        return log
