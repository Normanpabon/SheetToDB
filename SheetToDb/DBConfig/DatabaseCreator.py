from DBConnectors import DbConnectionManager
from DBConfig import DbServer
from DBConfig import TableScheme


class DatabaseCreator:

    def __init__(self, dbName: str):
        self.dbName = dbName
        self.dbHost = None
        self.dbConnector = None
        self.dbTables = []
        self.sqlite = False

    def setSqlite(self, lite: bool):
        self.sqlite = lite

    # Crea una tabla desde zero y la agrega a la lista de tablas del objeto actual
    def addTableFromScratch(self, tableName: str, tableAttrib, tableData):
        tmpObj = TableScheme.TableScheme(tableName, tableAttrib, tableData)
        self.addTable(tmpObj)
    def addTable(self, table: TableScheme.TableScheme):
        self.dbTables.append(table)

    def setDbHost(self, dbServer: DbServer.DbServer):
        self.dbHost = dbServer

    def setDbHostManually(self, dbHost, dbPort, dbType, dbUser, userPassword):
        tmpDbServer = DbServer.DbServer(dbHost, dbPort, dbType, dbUser, userPassword)

        self.dbHost = tmpDbServer
