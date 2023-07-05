from FileProcessing import CsvHandler
from FileProcessing import ExcelSheetHanlder
from FileProcessing import DataType


class FilesPipeline:

    csvFilesToProcess = None
    excFilesToProcess = None

    def __init__(self):

        self.excFilesToProcess = []
        self.csvFilesToProcess = []


    def addCsvFile(self, file: CsvHandler):

        self.csvFilesToProcess.append(file)

    def addCsvFileFromPath(self, path):

        # Arroja error si es invalido el archivo
        try:

            if not (DataType.DataType.extensionChecker(path, ".csv")):
                raise AttributeError
            else:
                tmpFilename = DataType.DataType.extractFilenameFromPath(path)
                tmpCsvhandlerObj = CsvHandler.CsvHanlder(path, tmpFilename, 'UTF-8')
                self.csvFilesToProcess.append(tmpCsvhandlerObj)
        except AttributeError:
            print("ERROR : El path dado no corresponde a ningun archivo .CSV")




    def addExcFile(self, file: ExcelSheetHanlder):

        self.excFilesToProcess.append(file)

    def readCsvFiles(self):

        for csvFiles in self.csvFilesToProcess:
            csvFiles.readSelf()

    def readExcFiles(self):
        pass