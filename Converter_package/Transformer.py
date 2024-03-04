
from Logger_Converter import LoggerConverter
from Converter import Converter
from StepTypes import StepTypes


class Transformer():
    def __init__(self):
        self.__log__ = LoggerConverter.logger(__name__)

    def compute(self, n_row, oldRowData):
        configInfo = Converter()
        dataFromConfigFile = Converter()
        oldKeyCell = str(oldRowData[0])
        stepType = StepTypes()

        if oldKeyCell in Converter.POSSIBLE_HEADERS:
            self.__log__.info("Extracting Headers from config file")
            return dataFromConfigFile.getElementsFromSection(Converter.HEADER)
        elif configInfo.sectionExist(oldKeyCell):
            return stepType.findMethod(n_row, oldKeyCell, oldRowData)
        else:
            self.__log__.info(
                f"Skipping like... Key: *{oldKeyCell}* not found on config file: *{Converter.CONFIG_LOCATION_AND_NAME}*")
            return False
