import csv
from FileProcessing.DataType import DataType


class CsvHanlder:

    # todo : colocar un atributo donde se guarde la informacion ya leida del archivo

    def __init__(self, filePath, filename, encoding):
        self.filePath = filePath
        self.filename = filename
        self.encoding = encoding
        # Guardar diccionarios leidos del archvio CSV
        self.readedData = []
        # Confirma si ya se ha cargado los datos a la lista
        self.isReaded = False


    def getFirstLine(self):
        if(self.isReaded):
            for line in self.readedData:
                if(len(line) > 0):
                    return line
        else:
            self.readSelf()
            print("Err: El archivo no se ha leido o se encuentra vacio")
            return None

    '''
    def getFirstLine(self):
        with open(self.filePath + self.filename) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)
            for line in dictLector:
                return line
    '''

    def returnLines(self, lines):
        with open(self.filePath) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)
            itemList = []
            i = lines
            if (lines <= 0):
                return itemList

            # Todo : verificar que hayan lineas para leer

            for line in dictLector:
                if (i == 0):
                    break
                itemList.append(line)
                i -= 1
            return itemList

    # Lee el csv y lo guarda en la variable de clase: readedData
    def readSelf(self):
        with open(self.filePath) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)

            for obj in dictLector:

                if not (DataType.isEmptyDict(obj, 1)):
                    self.readedData.append(obj)
        self.isReaded = True

    @staticmethod
    def readCsv(filename, encoding):

        with open(filename, encoding) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)

            #todo: dejar el metodo tal que devuelva la lista de diccionarios contenidos en el csv

            for obj in dictLector:
                print(obj)