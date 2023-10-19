from Logger import  Logger
from configparser import ConfigParser
from Converter import  Converter
from icecream import ic



class Transformer():
    def __init__(self,n_row,row):
        ic.enable()
        self.__n_row__ = n_row
        self.__row__ = row

    def compute(self):
        config = ConfigParser()
        config.read(Converter.CONFIG_LOCATION_AND_NAME)
        config_data = config["DEFAULT"]

        ic(str(self.__row__[0]).lower())
        oldCell = str(self.__row__[0]).lower()
        if oldCell in config_data.keys():
            newCell = config_data[oldCell]
            ic(newCell)







