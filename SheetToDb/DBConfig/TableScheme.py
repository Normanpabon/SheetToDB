class TableScheme:

    def __init__(self, tableName, tableAttributes, tableData ):

        self.tableName = "".join(tableName.split())
        self.tableAttributes = tableAttributes
        self.tableData = tableData
        self.tablePKKey = None

    def setTableAttributes(self, attributes):
        self.tableAttributes = attributes

    def setTableData(self, data):
        self.tableData = data

    def setTableName(self, name):
        self.tableName = name