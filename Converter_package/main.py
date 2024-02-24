#!/user/bin/python3
import argparse
import logging

import sys

import setupConverter
from ReadinginputFile import Input
from Converter import Converter


def main():
    """
    Main use is to convert csv files into xlsx with custom output base on mapping source -> dictionary - >destiny
    Note:Step 1 and 2 are only need to be run first time or when there is updates to the configuration files.
        1. Set up the needed directories using setupConverter.py.
        2. Create the needed configuration files using requestName_interfaceNumber_config_creator.py
        3. Make sure to call the main program with at least the input.csv file
    """

    parseinputargs = argparse.ArgumentParser(prog="CSV to Xlsx Converter\n",
                                             description="Application to convert csv into xlsx files")

    # Removing first argument which is the caller
    parseinputargs.add_argument("path_to_input_runbook", help="Path to input csv file is mandatory")

    parseinputargs.add_argument("--output_xlsx_file_name",
                                help="Name of output runbook, default \"temp_name_CI.xlsx it's \"",
                                default="Default", type=str)

    parseinputargs.add_argument("--is_data_being_copied_over_ci",
                                help="Default to N, only two possible values N/Y", default="N",
                                choices=["N", "Y"])
    args = parseinputargs.parse_args()

    try:
        if len(sys.argv) < 1:
            raise ValueError(f"Missing input file, Syntax's: ./caller.py )")
        else:

            path_to_input_runbook = args.path_to_input_runbook
            output_xlsx_file_name = args.output_xlsx_file_name
            is_data_being_copied_over_ci = args.is_data_being_copied_over_ci
            print(str(sys.argv))
            a = Input(path_to_input_runbook, output_xlsx_file_name)
            a._readInput()
    except FileNotFoundError as exc:
        raise ValueError(
            f"Missing input file for more info please do ./main --help),{exc}")


def wrapper(fnc):
    if setupConverter.setupDirectories():
        print("Setup already completed, skipping folder creation.")
    else:
        print("Initial folder setup completed.")
    log = Converter.logger(__name__, debugLevel=logging.DEBUG)
    log.info("Started...")
    main()
    log.info("Done")

if __name__ == "__main__":
    wrapper(main)
