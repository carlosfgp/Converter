import logging
from Converter import  Converter
from Logger import Logger
import os
import sys
from icecream import ic
from  xlsxwriter.workbook import Workbook
from Transformer import Transformer
import csv
import shutil





class input():

    def __init__(self,inputFile,runbookName='Default'):
        self.__inputFile = inputFile
        self.__log = Logger.logger(__name__,debugLevel=logging.DEBUG)
        new_Stram_Handler = logging.StreamHandler()
        self.__log.addHandler(new_Stram_Handler)
        self.__runbookName = runbookName

        ic.enable()
        if (os.path.isfile(inputFile) & (inputFile).endswith(".csv")):
            message = "Transforming Tosca {} Runbook into CI".format(inputFile)
            ic(message)
            self.__log.info(message)
        else:
            raise FileNotFoundError("Error while reading {}".format(inputFile))



    def _readInput(self):
        if self.__runbookName == 'Default':
            fileName = os.path.join(Converter.TEMP_XLSX_PATH, Converter.TEMP_XLSX_FILE)
            workbook = Workbook(str(fileName), {'strings_to_numbers': True})
        else:
            fileName = os.path.join(Converter.TEMP_XLSX_PATH,self.__runbookName)
            workbook = Workbook(str(fileName), {'strings_to_numbers': True})

        worksheet = workbook.add_worksheet()

        try:
            with open(self.__inputFile, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    self.__log.debug("R - {}  ROW - {}".format(r, row))
                    new_list = [r,row]
                    compute = Transformer(r,row)
                    compute.compute()
                    #worksheet.write(r,c,column)
            #workbook.close()
            ic(fileName)
            self._moveFilesAround(fileName)
        except TypeError as e:
            #workbook.close()
            self.__log.warning("Error while reading input file {e}".format(e))


    def _moveFilesAround(self,actualFile):

        dstnFile = os.path.join(Converter.CI_RUNBOOKS_PATH, os.path.basename(actualFile).replace(".xlsx",Converter.FILE_SUFIX) )
        if os.path.isfile(actualFile):
            shutil.copy(actualFile,dstnFile)
            self.__log.info("File created {}".format(dstnFile))
