import logging
import os

from configparser import ConfigParser
from Logger_Converter import LoggerConverter


class Converter:
    parent_directory = os.path.dirname(__file__)
    home_directory = os.path.expanduser("~")
    ULDD_PATH_REQUEST_ID_PATH = "./catalog/catalognaNo"
    CI_RUNBOOK_DESTINATION_PATH = os.path.join(home_directory, "Runbooks")
    CI_TEST_DATA = os.path.join(parent_directory, "TEST_DATA")
    TEMP_XLSX_PATH = os.path.join(parent_directory, "tmp")
    TEMP_XLSX_FILE = "temp.xlsx"
    FILE_SUFIX = "_CI.xlsx"
    CONFIG_LOCATION_AND_NAME = "config/ToscaToCIMapping.ini"
    RQ_IF = "config/RW_IF.ini"
    POSSIBLE_HEADERS = ["ActionType", "__PossibleHeaders_Here"]
    HEADER = "HEADER"
    CREATE_CONFIG = False

    def __init__(self):
        self.__config__ = ConfigParser()
        self.__config__.read(Converter.CONFIG_LOCATION_AND_NAME)
        self.__configSections__ = self.__config__.sections()
        self.__log__ = LoggerConverter.logger(__name__)
        self.__interfaceConfigData__ = ConfigParser()
        self.__interfaceConfigData__.read(Converter.RQ_IF)

    def sectionExist(self, stepType):
        if stepType in self.getSecctions():
            return True
        return False

    def getElementsFromSection(self, section):
        elementsFromSection = []
        try:
            if self.sectionExist(section):
                for key, elements in self.__config__.items(section):
                    elementsFromSection.append(elements)
            else:
                self.__log__.debug(f"Section: {section} not found on config file{Converter.CONFIG_LOCATION_AND_NAME}",
                                   exc_info=True)
        except KeyError:
            raise self.__log__.debug(f"Section: {section} not found on config file{Converter.CONFIG_LOCATION_AND_NAME}",
                                     exc_info=True)
        return elementsFromSection

    def getSecctions(self):
        return self.__configSections__


