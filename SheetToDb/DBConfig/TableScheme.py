class TableScheme:

    def __init__(self, tableName, tableAttributes, tableData ):
        self.tableName = tableName
        self.tableAttributes = tableAttributes
        self.tableData = tableData

    def setTableAttributes(self, attributes):
        self.tableAttributes = attributes

    def setTableData(self, data):
        self.tableData = data

    def setTableName(self, name):
        self.tableName = name