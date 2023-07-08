from FileProcessing import FilesPipeline
from DBConfig import DbServer
from DBConfig import DatabaseCreator
from FileProcessing import DataType


class SheetToDB:


    def __init__(self):

        self.fileProcess = FilesPipeline.FilesPipeline()
        self.dbSettings = DatabaseCreator.DatabaseCreator("SheetToDB_TEMP")


    def setDbSettings(self, dbName):

        self.dbSettings = DatabaseCreator.DatabaseCreator(dbName)

    def createDb(self):

        self.dbSettings.insertConstructor()


    def addCsvFile(self, path : str):


        self.fileProcess.addCsvFileFromPath(path)

    def loadFiles(self):
        self.fileProcess.readCsvFiles()
        self.fileProcess.readExcFiles()

    def createTablesSchemes(self):
        # todo: verificar que hayan elementos cargados y con datos

        for cvs in self.fileProcess.csvFilesToProcess:
            tmpName = DataType.DataType.nameWithoutExtension(cvs.filename)
            if(cvs.isReaded):
                tmpAttrib = DataType.DataType.getAttributesDataTypes(cvs.getFirstLine())
                tmpData = cvs.readedData
                self.dbSettings.addTableFromScratch(tmpName, tmpAttrib, tmpData)
            else:
                print("ERROR: No se han leido los datos aun")
        #self.dbSettings.addTableFromScratch()