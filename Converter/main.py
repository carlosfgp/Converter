#!/usr/bin/python3
import os
import sys

from Converter import Converter
from ReadinginputFile import input

path = r"C:\Users\carlo\projects\Python\inputfile.csv"
runbookname = 'Runbook1.xlsx'

sys.argv.pop()
sys.argv.append(path)
sys.argv.append(runbookname)


def main():
    log = Converter.logger(__name__)

    if len(sys.argv) < 0:
        raise ValueError(
            f'Missing input file, Syntaxis: ./caller.py Runbook_To_Converted_Path Optional=RunbookName)'.format())

    else:
        fileName = sys.argv[0]
        runboook = sys.argv[1]

        log.info("Started...")
        a = input(fileName, runboook)
        a._readInput()
        log.info("Done.")


if __name__ == "__main__":
    if os.path.exists(Converter.CI_LOGS_FILEPATH):
        os.remove(Converter.CI_LOGS_FILEPATH)
    main()