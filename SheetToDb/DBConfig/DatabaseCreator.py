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

    def addTable(self, table: TableScheme.TableScheme):
        self.dbTables.append(table)

    def setDbHost(self, dbServer: DbServer.DbServer):
        self.dbHost = dbServer

    def setDbHostManually(self, dbHost, dbPort, dbType, dbUser, userPassword):
        tmpDbServer = DbServer.DbServer(dbHost, dbPort, dbType, dbUser, userPassword)

        self.dbHost = tmpDbServer
