from FileProcessing import CsvHandler
from FileProcessing import ExcelSheetHanlder


class FilesPipeline:

    csvFilesToProcess = None
    excFilesToProcess = None

    def __init__(self):

        self.excFilesToProcess = []
        self.csvFilesToProcess = []


    def addCsvFile(self, file: CsvHandler):

        self.csvFilesToProcess.append(file)

    def addExcFile(self, file: ExcelSheetHanlder):

        self.excFilesToProcess.append(file)