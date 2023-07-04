from DBConnectors import DbConnectionManager
from DBConfig import DbServer
from DBConfig import TableScheme

class DatabaseCreator:

    dbTables = []

    dbConnector = None

    def __init__(self, dbName: str, dbHost: DbServer.DbServer):

        self.dbName = dbName
        self.dbHost = dbHost
        self.dbTables = []



    def addTable(self, table : TableScheme.TableScheme):

        self.dbTables.append(table)

    def setDbHost(self, dbServer : TableScheme.TableScheme):

        self.dbHost = dbServer
