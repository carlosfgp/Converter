import os
import xml.etree.ElementTree as ET

from Logger_Converter import LoggerConverter
from configparser import ConfigParser
from Converter import Converter


class ReadXml:

    def __init__(self):
        self.__log__ = LoggerConverter.logger(__name__)
        self.__mapping__ = ConfigParser()
        self.__loadMapping__ = self.__mapping__.read(Converter.RQ_IF)
        self.__mapping__.sections()

        mappingDic = {}
        try:
            for key, elements in self.__mapping__.items("INTERFACEDATA"):
                mappingDic[key] = elements
        except KeyError as exc:
            raise self.__log__.debug(
                f'Sectio not found on config file{Converter.RQ_IF}',
                exc_info=True)
        self.__mappingDic__ = mappingDic

    def readXml(self, row, inputFile):
        elementsToReturn = []
        if os.path.isfile(inputFile):
            tree = ET.parse(inputFile)
            root = tree.getroot()
            neededElements = ['.catalogname', '.UpperCategory1/SubCategoryA/subCategoryName',
                              '.UpperCategory1/SubCategoryA/SubCategoryB/subCategoryName', '.book/description',
                              'catalognaNo']
            try:

                for paths in neededElements:
                    element = root.find(paths).text
                    if element != "" and element is not None:
                        elementsToReturn.append(element.strip(''))

                self.__log__.info(
                    f'Getting requestId for  file {inputFile} in row {row} return value: {elementsToReturn}')
                return elementsToReturn
                # value =  tree.find(Converter.ULDD_PATH_REQUEST_ID_PATH)
                # print(value)
            except AttributeError as exc:
                raise AttributeError(
                    f"Error while getting data from input file {inputFile} in row {row}, either the data needs to be "
                    f"reviewed or the paths to the elements needs to be updated.")

        else:
            self.__log__.critical(f"Error on row {row} file does not exist: {inputFile}.")
        return False
        # if self.__mappingDic__ = interfaceNo:
        #     pass
