from DBConnectors import DbType
from DBConnectors import SqliteConnector
from DBConnectors import MysqlConnector

class DbConnectionManager():


    def __init__(self, dbEnumid:int, dbName:str):

        # todo : manejo de error si dbEnumid es distinto a los usados en el enum de DbType
        self.dbType = DbType.DbType(dbEnumid)
        self.connectorObj = None
        self.dbName = dbName
        self.setupConnector()


    def setupConnector(self):

        # Inicializa el objeto segun el tipo de bd a usar

        if(self.dbType.name == "SQLITE"):
            self.connectorObj = SqliteConnector.SqliteCreator(self.dbName)
        elif(self.dbType.name == "MYSQL"):
            self.connectorObj = MysqlConnector.MysqlConnector()
        elif(self.dbType.name == "SQLSERVER"):
            pass



    def writeQuery(self, query:str):

        # Llama al metodo para escribir, usando el connector de la bd elegida

        result = ""

        self.connectorObj.writeQuery(query)

        return result



