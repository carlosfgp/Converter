#!/user/bin/python3
import argparse
import logging
import os
import sys

from Converter import Converter
from ReadinginputFile import input

def main():
    """
    Main use is to convert csv files into xlsx with custom output base on mapping sourcre -> dictionary - >destiny
    etc etc.
    """

    log = Converter.logger(__name__)
    parseInputArgs = argparse.ArgumentParser(prog="CSV to Xlsx Converter" ,description="Application to convert csv into xlsx files")

    # Removing first argument which is the caller
    parseInputArgs.add_argument("path_to_input_runbook", help="Path to input csv file is mandatory")

    parseInputArgs.add_argument("--output_xlsx_file_name",
                                help="Name of output runbook, default \"temp_name_CI.xlsx\it's \"",
                                default="temp_name_CI", type=str)

    parseInputArgs.add_argument("--is_data_being_copied_over_ci",
                                help="Default to N, only two posible values N/Y", default="N",
                                choices=["N", "Y"])
    args = parseInputArgs.parse_args()
    log.info(f"Input parameters{str(sys.argv)}")

    try:
        if len(sys.argv) < 1:
            raise ValueError(f"Missing input file, Syntaxis: ./caller.py )")
        else:

            path_to_input_runbook = args.path_to_input_runbook
            output_xlsx_file_name = args.output_xlsx_file_name
            is_data_being_copied_over_ci = args.is_data_being_copied_over_ci
            print(str(sys.argv))
            a = input(path_to_input_runbook, output_xlsx_file_name)
            a._readInput()
    except FileNotFoundError as exc:
        raise ValueError(
            f"Missing input file for more info please do ./main --help)")

def wrapper(fnc):
    log = Converter.logger(__name__, debugLevel=logging.INFO)
    log.info("Started...")
    main()
    log.info("Done.1")


if __name__ == "__main__":
    if os.path.exists(Converter.CI_LOGS_FILEPATH):
        os.remove(Converter.CI_LOGS_FILEPATH)

    wrapper(main)
