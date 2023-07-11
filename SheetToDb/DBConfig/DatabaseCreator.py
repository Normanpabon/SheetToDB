from DBConnectors import DbConnectorManager
from DBConfig import DbServer
from DBConfig import TableScheme
from DBConfig import DBDataParser


class DatabaseCreator:

    def __init__(self, dbName: str):
        self.dbName = dbName
        self.dbHost = None
        self.dbConnector = None
        self.dbTables = []
        self.dbDataParser = DBDataParser.DBDataParser()
        self.dbType = None

    def initialiceConnectionManager(self, dbType:int):
        # Metodo : inicializa el tipo de connector a usar en la BD ( 0. Sqlite, 1.Mysql, 2.SqlServer)
        self.dbType = dbType
        self.dbConnector = DbConnectorManager.DbConnectionManager(dbType, self.dbName)

    def convertTablesDataTypes(self):
        # Iterar sobre lista dbTables
        for tableScheme in self.dbTables:
            # llamar metodo dbDataParser.DataTypeMapper y pasarle los respectivos dicts con los tipos de datos de la tabla a crear
            #todo : quizas migrar tambien el tipo de db a crear aca
            tmpTable = tableScheme.tableAttributes
            newTable = self.dbDataParser.dataTypeMapper(self.dbType,tmpTable)

            tableScheme.setTableAttributes(newTable)



    # Todo : Terminar llamados. Este metodo se encarga de crear la respectiva BD y llamar los querys para la creacion de tablas e ingreso de datos

    def createDatabase(self):

        for table in self.dbTables:
            tmpTableQuery = ""
            #verificamos si se detecto un PK en la tabla y llamamos al metodo acorde
            tmpTablePk = table.tablePKKey
            if(tmpTablePk == None):
                tmpTableQuery = self.dbDataParser.createTableQueryConstructorNoPK(self.dbType, table.tableAttributes,
                                                                                  table.tableName)
            else:
                tmpTableQuery = self.dbDataParser.createTableQueryConstructorWithPK(self.dbType, table.tableAttributes,table.tableName, tmpTablePk)
            # Pedimos query para crear las tablas con sus campos


            #Enviamos el query a la bd
            self.sendQueryToDb(tmpTableQuery)

            # todo: Crear queries para insertar los datos de la tabla




    # Todo DEPRECATED
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



    def sendQueryToDb(self, query:str):
        #Llama al dbconnector y envia la peticion
        # todo: mostrar el resultado cuando se haga la gui
        result = self.dbConnector.writeQuery(query)

        #todo: borrar
        print(result)

    def addTableFromScratch(self, tableName: str, tableAttrib, tableData):
        # Crea una tabla desde zero y la agrega a la lista de tablas del objeto actual
        tmpObj = TableScheme.TableScheme(tableName, tableAttrib, tableData)
        tmpObj.checkForPk()
        self.addTable(tmpObj)
    def addTable(self, table: TableScheme.TableScheme):
        # Agrega una tabla a la lista del objeto actual
        table.checkForPk()
        self.dbTables.append(table)

    def setDbHost(self, dbServer: DbServer.DbServer):
        self.dbHost = dbServer

    def setDbHostManually(self, dbHost, dbPort, dbType, dbUser, userPassword):
        # Configurar datos de conexion al servidor
        tmpDbServer = DbServer.DbServer(dbHost, dbPort, dbType, dbUser, userPassword)

        self.dbHost = tmpDbServer
