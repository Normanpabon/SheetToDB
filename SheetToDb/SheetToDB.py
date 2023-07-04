from FileProcessing import FilesPipeline
from DBConfig import  DbServer
from DBConfig import DatabaseCreator

class SheetToDB:


    def __init__(self):

        self.fileProcess = FilesPipeline.FilesPipeline()
        self.dbSettings = None


    def setDbSettings(self, dbName, dbServer: DbServer):

        self.dbSettings = DatabaseCreator.DatabaseCreator(dbName, dbServer)

