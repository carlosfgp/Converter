import logging

from Converter import Converter
from StepTypes import StepTypes


class Transformer():
    def __init__(self):
        self.__log__ = Converter.logger(__name__, debugLevel=logging.INFO)

    def compute(self, n_row, row):
        configInfo = Converter()
        dataFromConfigFile = Converter()
        oldKeyCell = str(row[0])
        stepType = StepTypes()

        if oldKeyCell in Converter.POSSIBLE_HEADERS:
            self.__log__.info("Extracting Headers from config file")
            return dataFromConfigFile.getElementsFromSecction(Converter.HEADER)
        elif configInfo.secctionExist(oldKeyCell):
            return stepType.findMethod(oldKeyCell)
        else:
            self.__log__.debug(
                f"Skipping like... Key: *{oldKeyCell}* not found on config file: *{Converter.CONFIG_LOCATION_AND_NAME}*")
            return False
        self.__log__.info(f"Not sure what to do for this key: *{oldKeyCell}*")
        return False
