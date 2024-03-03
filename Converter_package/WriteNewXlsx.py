import logging
import os
import shutil

from Logger_Converter import LoggerConverter
from Converter import Converter


class WriteNewXlsx:

    def __init__(self):
        self.__log__ = LoggerConverter.logger(__name__)

    def moveFilesAround(self, actualFile):
        dstnFile = os.path.join(Converter.CI_RUNBOOK_DESTINATION_PATH,
                                str(os.path.basename(actualFile)).replace(".xlsx", Converter.FILE_SUFIX))
        if os.path.isfile(actualFile):
            shutil.copy(actualFile, dstnFile)
            self.__log__.info(f"File created *{dstnFile}*")

    # def MoveInputFiles
    # Will probably read paths and move files around
