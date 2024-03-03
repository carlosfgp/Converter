
from Logger_Converter import LoggerConverter
from Converter import Converter
from ReadXml import ReadXml


class StepTypes:
    def __init__(self):
        self.__log__ = LoggerConverter.logger(__name__)
        self.__config__ = Converter()

    def FileDrop(self, n_row, sectionName, oldRowData):
        # OD = OLD_DATA
        global newRowValues
        OD_FILE_DROP = 0
        OD_INTERFACE_NO = 1
        OD_ISSUER_ID = 2
        OD_PATH = 3
        OD_1A = 4
        OD_1E = 5
        OD_1C = 6

        NEW_FEATURE = 0
        NEW_DROP_ULDD = 1
        NEW_FILE_PATH = 2
        NEW_PATH = 3
        NEW_REQUEST_TYP = 4
        NEW_RT = 5

        ciElements = self.__config__.getElementsFromSection(sectionName)
        fileinfo = ReadXml()
        valuesFromXml = fileinfo.readXml(n_row, oldRowData[3])
        if valuesFromXml:
            newRowValues = []

            interfaceNo = self.getInterfaceValue(valuesFromXml[NEW_REQUEST_TYP])

            # Feature
            newRowValues.append(valuesFromXml[NEW_FEATURE])
            # Step
            newRowValues.append(ciElements[NEW_DROP_ULDD])
            # Param 0
            newRowValues.append(ciElements[NEW_FILE_PATH])
            # Param 1
            newRowValues.append(oldRowData[NEW_PATH])
            # Param 2
            newRowValues.append(ciElements[NEW_REQUEST_TYP])
            # Param 3

            newRowValues.append(interfaceNo)
            # 1E element is the second to last on drop uldd for Tosca users

            if int(oldRowData[-2]) >= 1:
                # Leaving an empty space between other arguments
                newRowValues.append("")
                newRowValues.append('Expect1E')
                newRowValues.append('1')
            newRowValues.append(oldRowData[OD_ISSUER_ID])
        return newRowValues

    def getInterfaceValue(self, interfaceName):
        try:
            if self.__config__.__interfaceConfigData__['INTERFACEDATA'][interfaceName] != "":
                return self.__config__.__interfaceConfigData__['INTERFACEDATA'][interfaceName]
        except Exception as e:
            self.__log__.warning(
                f'Element{interfaceName} not found on config file{Converter.RQ_IF} interfaces value will be empty')
        return 'NotFound'

    def LTE(self, n_row, section, oldRowData):
        temp = ['Not Ready yet']
        return temp

    def findMethod(self, n_row, section, oldRowData):
        if self.__config__.sectionExist(section):
            funcCall = getattr(self, section)
            return funcCall(n_row, section, oldRowData)

    def FolderDrop(self, n_row, sectionName, oldRowData):
        elements = self.__config__.getElementsFromSection(sectionName)
        # interfaceName = ReadXml.ReadXml(elements[3])
        # featureName =
        # feature = getFeatureBaseOnInterface(elements[3])
        return elements
