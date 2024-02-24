import os.path
from configparser import ConfigParser


def generateKeyFeatureConfig():
    config = ConfigParser()
    config.optionxform = str

    config["HEADER"] = {
        "column0": "Feature",
        "column1": "Step",
        "column2": "Param 0 Value",
        "column3": "Param 1 Value",
        "column4": "Param 1 Value",
        "column5": "Param 1 Value",
        "column6": "Param 1 Value",
        "column7": "Param 1 Value",
    }

    config["FolderDrop"] = {
        "column0": "S_FEATURE",
        "column1": "FileDirPath",
        "column2": "PATH",
        "column3": "S_REQUEST_TYPE",
    }
    config["FileDrop"] = {
        "column0": "S_FEATURE",
        "column1": "Drop ULDD",
        "column2": "FilePath",
        "column3": "PATH",
        "column4": "S_REQUEST_TYPE",
    }

    config["LTE"] = {
        "column0": "S_FEATURE",
        "column1": "PublishLTE",
        "column2": "EventName",
        "column3": "PATH",
        "column4": "S_LTE"
    }

    config["LTERange"] = {
        "column0": "S_FEATURE",
        "column1": "Roll Dates",
        "column2": "StartDate",
        "column3": "EndDate"
    }

    config["RunsQL"] = {
        "column0": "S_FEATURE",
        "column1": "Execute SQL Script",
        "column2": "Script",
        "column3": "PATH",
        "column4": "S_MODULE"
    }

    config["Issuer"] = {
        "564654": "FMCC",
        "354684": "FNMA"
    }

    if not os.path.exists(os.path.join(os.path.dirname(__file__), "config")):
        os.makedirs(os.path.join(os.path.dirname(__file__), "config"))

    with open(os.path.join(os.path.dirname(__file__), "config/ToscaToCIMapping.ini"), "w") as f:
        config.write(f)


generateKeyFeatureConfig()
