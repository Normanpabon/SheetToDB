class TableScheme:

    def __init__(self, tableName, tableAttributes, tableData ):

        self.tableName = "".join(tableName.split())
        self.tableAttributes = tableAttributes
        self.tableData = tableData
        self.tablePKKey = None
        self.checkForPk()

    def setTableAttributes(self, attributes):
        self.tableAttributes = attributes

    def setTableData(self, data):
        self.tableData = data

    def setTableName(self, name):
        self.tableName = name

    def checkForPk(self):
        # revisa si hay algun atributo llamado id o uid

        #todo: quizas deba implementarse un metodo que verifique que todos los datos tengan id en el campo encontrado, como prevencion de errores

        for atrib, dType in self.tableAttributes.items():
            if(atrib.casefold() == "id".casefold() or atrib.casefold() == "uid".casefold() ):
                if(dType == "INTEGER"):
                    self.tablePKKey = atrib
                    return True
        return False

    def setPkKey(self, pkName:str):

        self.tablePKKey = pkName
