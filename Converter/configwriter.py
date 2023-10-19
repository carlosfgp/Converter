from configparser import  ConfigParser
from Converter import Converter

config = ConfigParser()

config["DEFAULT"] = {
    "HEADER" : ["Feature","Step","Param 0"],
    "ActionType" : "Feature",
    "Paraml" : "Step",
    "Param2" : "Param 0 Value",
    "Param3" : "Param 1 Value",
    "Paran4" : "Param 2 Value",
    "Param5" : "Param 3 Value",
    "Paran6" : "Param 4 Value",
    "Paran7" : "Param 5 Value",
    "Paran8" : "Param 6 Value",
    "Paran9" : "Param 7 Value",
    "Paran10" : "Param 8 Value",
    "FolderDrop" : ["S_FEATURE","Drop ULDD","FileDirPath","PATH","S_REQUEST_TYPE"],
    "FileDrop" : ["S_FEATURE","Drop ULDD","FilePath:PATH","PATH","S_REQUEST_TYPE"],
    "LTE" : ["S_FEATURE","PublishLTE","EventName","S_LTE"],
    "LTERange" : ["S_FEATURE","Roll Dates","StartDate","EndDate"],
    "RunsQL" : ["S_FEATURE","Execute SQL Script","Script","PATH","S_MODULE:MODULE"],
    "564654" : ["FMCC"],
    "354684" : ["FNMA"]
}

with open(Converter.CONFIG_LOCATION_AND_NAME, "w") as f:
    config.write(f)