#!/usr/bin/python3
from Converter import Converter
import os
from Logger import Logger
import sys
from icecream import ic
from ReadinginputFile import input

ic.enabled
path = r"C:\Users\carlo\projects\Python\inputfile.csv"
runbookname = 'Runbook1.xlsx'

sys.argv.pop()
sys.argv.append(path)
sys.argv.append(runbookname)


def main():
    log = Logger.logger(__name__)

    if len(sys.argv) < 0:
        raise ValueError(f'Missing input file, Syntaxis: ./caller.py Runbook_To_Converted_Path Optional=RunbookName)'.format())

    else:
        fileName = sys.argv[0]
        runboook = sys.argv[1]
        ic("Started...")
        log.info("Started...")
        a = input(fileName,runboook)
        a.readInput()
        ic("Done.")
        log.info("Done.")

if __name__ == "__main__":
    ic(os.path.exists(Converter.CI_LOGS_FILEPATH))
    if os.path.exists(Converter.CI_LOGS_FILEPATH):
        os.remove(Converter.CI_LOGS_FILEPATH)
    main()