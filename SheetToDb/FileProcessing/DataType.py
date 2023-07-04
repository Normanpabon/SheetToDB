from dateutil.parser import parse
class DataType:

    @staticmethod
    def isDate( string, fuzzy=False):
        try:
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False


    @staticmethod
    def isFloat(string):
        # iterar buscando el .

        flag = False
        dCount = 0

        for char in string:

            if (char == '@'):
                break

            if (char == '.'):
                dCount += 1

        if dCount == 1:
            flag = True

        return flag


    @staticmethod
    # devuelve diccionario con "llave dada del dic original" : tipo dato segun Mysql
    def getAttributesDataTypes(obj):

        atributes = {}
        for value in obj:
            # print(obj[value])

            # Todo: revisar cada valor y asignar el correspondiente

            # Verifica si es numerico

            if (DataType.isFloat(obj[value])):
                atributes[value] = "DOUBLE"
            elif (obj[value].isnumeric()):
                atributes[value] = "INT"

            # Verificamos si esta vacio
            elif (obj[value] == ""):
                atributes[value] = "VARCHAR"

            # Verificamos si es una fecha

            # Todo: revisar, aveces toma otros valores como fecha
            elif (DataType.isDate(obj[value])):
                atributes[value] = "DATE"

            # verificar si es bool
            elif (obj[value] == "FALSE" or obj[value] == "TRUE"):
                atributes[value] = "BOOL"

            # Se toma como varchar
            else:
                atributes[value] = "VARCHAR"

            # atributes[value]= (type(obj[value]))

        return atributes
