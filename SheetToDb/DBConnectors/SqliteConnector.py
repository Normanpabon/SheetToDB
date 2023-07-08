import sqlite3
class SqliteCreator:



    def __init__(self, fname):
        # todo : manejo de errores si el archivo existe
        self.filename = fname
        self.connection = sqlite3.connect(self.filename)


    def setupConnection(self):

        self.connection = sqlite3.connect(self.filename)

    def writeQuery(self, query:str):

        cursor = self.connection.cursor()

        cursor.execute(query)



