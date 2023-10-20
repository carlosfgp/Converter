import configparser
from   configparser import ConfigParser
from Converter import Converter

class StepTypes():


    def __init__(self,configParserArg):
        self.__parser__ =  configparser.ConfigParser()


    def getHeader(self):
        headerValues = []

        for column, value in self.__parser__.items('HEADER'):
            headerValues.append(value)
        return headerValues

    def getSeccion(self,seccion):

        for column, value in self.__parser__.items('HEADER'):
            headerValues.append(value)
        return headerValues


    def File_drop(self,elements):
          = configInfo.getElementsFromSecction(oldKeyCell)