import logging
import os
from configparser import ConfigParser
import xml.etree.ElementTree as ET

from Converter import Converter


class ReadXml:

    def __init__(self):
        self.__log__ = Converter.logger(__name__, debugLevel=logging.DEBUG)
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
        self.__mapinggDic__ = mappingDic

    def readXml(self, row, inputFile):
        elementsToreturn = []
        if os.path.isfile(inputFile):
            tree = ET.parse(inputFile)
            root = tree.getroot()
            neededElements = ['.catalogname' ,'.UpperCategory1/SubCategoryA/subCategoryName', '.UpperCategory1/SubCategoryA/SubCategoryB/subCategoryName','.book/description', 'catalognaNo' ]
            try:
                for paths in neededElements:
                    element = root.find(paths).text
                    if element !="" and element != None:
                        elementsToreturn.append(element.strip(''))

                self.__log__.info(f'Getting requestid for  file {inputFile} in row {row} return value: {elementsToreturn}')
                return  elementsToreturn
                #value =  tree.find(Converter.ULDD_PATH_REQUEST_ID_PATH)
                #print(value)
            except AttributeError as exc:
                raise AttributeError(f'Error while getting data from input file {inputFile} in row {row}, either the data needs to be reviewed or the paths to the elemtns needs to be updated.')

        else:
            self.__log__.critical(f'Error on row {row} file doesn\'t exist: {inputFile}')
        return  False
        # if self.__mapinggDic__ = interfaceNo:
        #     pass


