import os.path
from configparser import ConfigParser

from Converter import Converter


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
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "config")):
        os.makedirs(os.path.join(os.path.dirname(__file__), "config"))
    with open(Converter.RQ_IF, "w") as f:
        config.write(f)


generateIFConfig()
