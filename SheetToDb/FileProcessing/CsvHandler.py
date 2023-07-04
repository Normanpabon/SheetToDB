import csv
class CsvHanlder:

    #todo : colocar un atributo donde se guarde la informacion ya leida del archivo

    def __init__(self, filePath, filename, encoding):
        self.filePath = filePath
        self.filename = filename
        self.encoding = encoding

    def getFirstLine(self):
        with open(self.filePath+self.filename) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)
            for line in dictLector:
                return line
            
    def returnLines(self, lines):
        with open(self.filePath+self.filename) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)
            itemList = []
            i = lines
            if(lines <= 0):
                return itemList

            #Todo : verificar que hayan lineas para leer

            for line in dictLector:
                if( i == 0):
                    break
                itemList.append(line)
                i -= 1
            return itemList

    def readSelf(self):
        with open(self.filePath+self.filename) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)


            for obj in dictLector:
                print(obj)

            #todo : dejar de leer cuando este vacio

    @staticmethod
    def readCsv(filename, encoding):

        with open(filename, encoding) as ficheroCSV:
            dictLector = csv.DictReader(ficheroCSV)

            for obj in dictLector:
                print(obj)