from DBConnectors import DbConnectorManager
from DBConfig import DbServer
from DBConfig import TableScheme


class DatabaseCreator:

    def __init__(self, dbName: str):
        self.dbName = dbName
        self.dbHost = None
        self.dbConnector = None
        self.dbTables = []

    def initialiceConnectionManager(self, dbType:int):
        # Metodo : inicializa el tipo de connector a usar en la BD ( 0. Sqlite, 1.Mysql, 2.SqlServer)
        self.dbConnector = DbConnectorManager.DbConnectionManager(dbType, self.dbName)


    def insertConstructor(self):

        # todo: debe adaptarse la sintaxis segun la bd a la que se vaya a pasar la info
        # ref para sqlite : https://www.sqlite.org/datatype3.html

        # Metodo: se encarga de generar el insert a enviar a la bd para cada tabla
        tmpInsert = ""

        for table in self.dbTables:
            # Crear tabla si no existe con los tipos de datos de tableAttributes
            tmpInsert = "CREATE TABLE [IF NOT EXISTS] " + table.tableName + "("

            # iterar sobre los atributos de la tabla
            for vals in table.tableAttributes:
                print(vals) # Key
                print(table.tableAttributes[vals]) #Value



            # iterar sobre los obj de tableData e insertarlos


    def sqlDatatypeChanger(self):
        # Metodo para cambiar los tipos de datos acorde al tipo de sql a utilizar
        pass

    def sendQueryToDb(self, query:str):
        #Llama al dbconnector y envia la peticion
        # todo: mostrar el resultado cuando se haga la gui
        result = self.dbConnector.writeQuery(query)

        #todo: borrar
        print(result)


    def addTableFromScratch(self, tableName: str, tableAttrib, tableData):
        # Crea una tabla desde zero y la agrega a la lista de tablas del objeto actual
        tmpObj = TableScheme.TableScheme(tableName, tableAttrib, tableData)
        self.addTable(tmpObj)
    def addTable(self, table: TableScheme.TableScheme):
        # Agrega una tabla a la lista del objeto actual
        self.dbTables.append(table)

    def setDbHost(self, dbServer: DbServer.DbServer):
        self.dbHost = dbServer

    def setDbHostManually(self, dbHost, dbPort, dbType, dbUser, userPassword):
        # Configurar datos de conexion al servidor
        tmpDbServer = DbServer.DbServer(dbHost, dbPort, dbType, dbUser, userPassword)

        self.dbHost = tmpDbServer
