import logging

from Converter import Converter


class StepTypes():

    def __init__(self):
        self.__log__ = Converter.logger(__name__, debugLevel=logging.INFO)
        self.__config__ = Converter()

    def getHeader(self):
        headerValues = []

        for column, value in self.__parser__.items('HEADER'):
            headerValues.append(value)
        return headerValues

    def FileDrop(self, sectionName):
        elements = self.__config__.getElementsFromSecction(sectionName)
        return elements

    def LTE(self, section):
        temp = ['Not Ready yet']
        return temp

    def findMethod(self, section):
        if self.__config__.secctionExist(section):
            funcCall = getattr(self, section)
            return funcCall(section)
