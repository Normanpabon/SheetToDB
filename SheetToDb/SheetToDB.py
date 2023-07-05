from FileProcessing import FilesPipeline
from DBConfig import DbServer
from DBConfig import DatabaseCreator



class SheetToDB:


    def __init__(self):

        self.fileProcess = FilesPipeline.FilesPipeline()
        self.dbSettings = None


    def setDbSettings(self, dbName):

        self.dbSettings = DatabaseCreator.DatabaseCreator(dbName)


    def addCsvFile(self, path : str):


        self.fileProcess.addCsvFileFromPath(path)

    def loadFiles(self):
        self.fileProcess.readCsvFiles()
        self.fileProcess.readExcFiles()