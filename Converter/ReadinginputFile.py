import csv
import logging
import os

import xlsxwriter.exceptions
from Converter import Converter
from Transformer import Transformer
from WriteNewXlsx import WriteNewXlsx
from xlsxwriter.workbook import Workbook


class input(Converter):

    def __init__(self, inputFile, runbookName):
        self.__inputFile = inputFile
        self.__log__ = Converter.logger(__name__, debugLevel=logging.INFO)
        self.__runbookName__ = runbookName
        new_Stram_Handler = logging.StreamHandler()
        self.__log__.addHandler(new_Stram_Handler)
        if (os.path.isfile(inputFile) & (inputFile).endswith(".csv")):
            message = f"Transforming Tosca *{inputFile}* Runbook into CI."
            self.__log__.info(message)
        else:
            raise FileNotFoundError(f"Error while reading input file: *{inputFile}*")

    # Reads csv file and writes new xlsx at the same time
    def _readInput(self):
        compute = Transformer()
        linesWrote = 0  # Row counter for new file
        moveFiles = WriteNewXlsx()

        if self.__runbookName__ == 'Default':
            fileName = os.path.join(Converter.TEMP_XLSX_PATH, Converter.TEMP_XLSX_FILE)
            workbook = Workbook(str(fileName), {"strings_to_numbers": True})
        else:
            fileName = os.path.join(Converter.TEMP_XLSX_PATH, self.__runbookName__)
            workbook = Workbook(str(fileName), {"strings_to_numbers": True})

        worksheet = workbook.add_worksheet()

        try:
            with open(self.__inputFile, "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                # Number of destiny row might not be the same as the origin, tracking it using linsWrote
                for walkingRowNumber, dataInRow in enumerate(reader):
                    self.__log__.debug(f"Origin - R - {walkingRowNumber}  ROW - {dataInRow}")
                    self.__log__.debug(f"Destiny - R - {linesWrote}  ROW - {dataInRow}")

                    newRowValuesLst = compute.compute(linesWrote, dataInRow)
                    if False == newRowValuesLst:
                        # Empty value is already handled on compute() method
                        continue
                    else:
                        self.__log__.debug(f"Origin - R - {walkingRowNumber}  ROW - {dataInRow}")
                        self.__log__.debug(f"Destiny - R - {linesWrote}  ROW - {newRowValuesLst}")

                        for colNoNewFile, element in enumerate(newRowValuesLst):
                            worksheet.write(linesWrote, colNoNewFile, element)
                            self.__log__.debug(f"Row number: {linesWrote} Column: {colNoNewFile} CELL - {element}")
                        linesWrote += 1
            workbook.close()
            moveFiles.moveFilesAround(fileName)
        except TypeError as exc:
            self.__log__.warning(f"Error while reading input file {exc}", exc_info=True)
        except xlsxwriter.exceptions.FileCreateError as exc:
            self.__log__.critical(f"File is open {exc}")
