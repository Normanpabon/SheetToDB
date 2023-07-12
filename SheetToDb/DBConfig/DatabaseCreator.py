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

            #Enviamos el query a la bd
            self.sendQueryToDb(tmpTableQuery)

            # todo: Crear queries para insertar los datos de la tabla
            for data in table.tableData:
                tmpProccesedData = DBDataParser.DBDataParser.putQuotationMarksRequiredDataTypes(table.tableAttributes, data)
                tmpDataInsertQuery = self.dbDataParser.insertIntoTableQuery(self.dbType, tmpProccesedData, table.tableName)

                #Enviar query a la BD
                try:
                    self.sendQueryToDb(tmpDataInsertQuery)
                except Exception as error:
                    print(error)
                    print("Query que causo el error:")
                    print(tmpDataInsertQuery)

            #todo : llamar commit para bd
            self.callForCommit()
            print("Datos creados correctamente ! \n\n\n")

    def callForCommit(self):
        self.dbConnector.callCommit()
    def sendQueryToDb(self, query:str):
        #Llama al dbconnector y envia la peticion
        # todo: mostrar el resultado cuando se haga la gui
        result = self.dbConnector.writeQuery(query)


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
