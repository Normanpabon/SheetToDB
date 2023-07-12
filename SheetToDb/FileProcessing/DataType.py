from dateutil.parser import parse
class DataType:




    @staticmethod
    #Recibe nombre de archivo con extension y revuelve retirando lo que este del ultimo punto en adelante (la extension)
    # usar para obtener el nombre de la tabla a crear, todo: considerar nombres con espacios
    def nameWithoutExtension(name: str):
        i = 0
        lastDot = -1
        while (i < len(name)):
            if (name[i] == "."):
                lastDot = i
            i += 1

        return name[0:lastDot]

    #Metodo para quitar espacios en blanco y cambiarlos por "_"
    @staticmethod
    def removeWhiteSpaces(string:str):
        tmpString = ' '.join(string.split())
        tmpString = tmpString.replace(' ', '_')
        return tmpString

    #Todo: Metodo para estandarizar la fecha a formato ISO 8601. (YYYY-MM-DD)
   #Todo2: Hay que saber desde que formato viene la fecha para poder determinar que numero es el dia y que numero es el mes en caso de que ambos sean < 12.
    @staticmethod
    def dateToISOStandard(date:str,format:str):

        # Verificar formato y traducir a ISO 8601.
        match format:
            case "YYYY-MM-DD":
                return date
            case "DD/MM/YYYY":
                x = date.split("/")
                return x[2]+ "-" + x[1] + "-" + x[0]
            case "MM/DD/YYYY":
                x=date.split("/")
                return x[2] + "-" + x[0]+ "-"+ x[1]
            case "YYYY/MM/DD":
                x=date.split("/")
                return x[0]+"-" +x[1] +"-" +x[2]
            case _:
                print("El formato dado no es correcto.")
                return date
            

    @staticmethod
    # Metodo para separar cadenas de texto separadas por comas, las devuelve en una lista
    def separateStrWithComma(string):
        list = []

        if (len(string) == 0):
            return list

        i = 0
        lastComma = -1
        lastStrEndIndex = -1
        while (i < len(string)):

            # Verificar si ya hay una "," encontrada

            if (string[i] == ","):
                lastComma = i

                # Primer string encontrado
                if (lastStrEndIndex == -1):
                    list.append((string[0:lastComma]).strip())
                    lastStrEndIndex = lastComma + 1
                else:
                    list.append((string[lastStrEndIndex:lastComma]).strip())
                    lastStrEndIndex = i + 1

            i += 1

        if (lastComma == -1):
            list.append(string.strip())
        elif not (lastComma == len(string) - 1):
            list.append((string[lastStrEndIndex:len(string)]).strip())

        return list




    @staticmethod
    # Devuelve verdadero si el diccionario se encuentra con mas espacios vacios que los dados en el threshold
    def isEmptyDict(dic, threshold:int):
        result = True
        nonEmptyValCount = 0

        for val in dic:

            if (len(dic[val]) != 0):
                nonEmptyValCount += 1

        if (nonEmptyValCount > threshold):
            result = False

        return result

    @staticmethod
    # Devuelve verdadero o falso si la ruta de archivo dada concuerda con la extension a evaluar
    def extensionChecker(filePath:str, extension:str):
        aproved = False
        tmpFilename = DataType.extractFilenameFromPath(filePath)
        lastDot = 0
        i = 0
        while(i < len(tmpFilename)):
            if(tmpFilename[i] == "."):
                lastDot = i

            i += 1

        tmpFileExt = tmpFilename[lastDot:len(tmpFilename)].casefold()

        if(tmpFileExt == extension.casefold()):
            aproved = True

        return aproved

    @staticmethod
    # Devuelve el nombre del archivo con su extension respectiva
    # todo : adaptar para revisar tambien en busca de slash normal
    def extractFilenameFromPath( path : str ):

        lastSlash = 0
        i = 0
        while(i < len(path)):

            if(path[i] == "\\" or path[i] == "/" ):
                lastSlash = i
            i+=1

        return ( path[lastSlash+1:(len(path))] )




        pass
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
                atributes[value] = "INTEGER"

            # Verificamos si esta vacio
            elif (obj[value] == ""):
                atributes[value] = "STRING"

            # Verificamos si es una fecha

            # Todo: revisar, aveces toma otros valores como fecha
            elif (DataType.isDate(obj[value])):
                atributes[value] = "DATE"

            # verificar si es bool
            elif (obj[value] == "FALSE" or obj[value] == "TRUE"):
                atributes[value] = "BOOL"

            # Se toma como string
            else:
                atributes[value] = "STRING"

            # atributes[value]= (type(obj[value]))

        return atributes
