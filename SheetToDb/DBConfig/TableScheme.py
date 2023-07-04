class TableScheme:

    tableAttributes = {}
    tableData = []

    def __init__(self, tableName):
        self.tableName = tableName

    def setTableAttributes(self, attributes):
        self.tableAttributes = attributes

    def setTableData(self, data):
        self.tableData = data

    def setTableName(self, name):
        self.tableName = name