import os.path

from Converter import Converter
from configparser import ConfigParser
from Logger_Converter import LoggerConverter

log = LoggerConverter.logger(__name__)


def generateIFConfig():
    config = ConfigParser()
    config.optionxform = str

    config["INTERFACEDATA"] = {
        "IFederico": "99_8_8",
        "ICarlos": "13_1_3",
        "column2": "Param 0 Value",
        "column3": "Param 1 Value",
        "column4": "Param 1 Value",
        "column5": "Param 1 Value",
        "column6": "Param 1 Value",
        "column7": "Param 1 Value",
    }

    file = os.path.join(os.path.dirname(__file__), Converter.RQ_IF)

    with open(file, "w") as f:
        config.write(f)

    log.info(f"Configuration file created: {file}")