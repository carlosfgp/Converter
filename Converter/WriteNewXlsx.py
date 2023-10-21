import logging
import os
import shutil

from Converter import Converter


class WriteNewXlsx:

    def __init__(self, runbookName='Default'):
        self.__log__ = Converter.logger(__name__, debugLevel=logging.INFO)

    def moveFilesAround(self, actualFile):
        dstnFile = os.path.join(Converter.CI_RUNBOOKS_PATH,
                                os.path.basename(actualFile).replace(".xlsx", Converter.FILE_SUFIX))
        if os.path.isfile(actualFile):
            shutil.copy(actualFile, dstnFile)
            self.__log__.info(f"File created *{dstnFile}*")

    # def MoveInputFiles
    # Will probably read paths and move files around
