import json
from DBConnectors import DbType
class DBDataParser:
    # DS = DataStructures


    def __init__(self):
        self.jsonFile = open("Jsons/DbDataStructureMapper.json")
        self.jsonDSData = json.load(self.jsonFile)

    def dataTypeMapper(self, dbType: int, tableAttributes: dict):
        newDic = {}

        dbType = DbType.DbType(dbType).name

        print(dbType)
        for attribName, dataType in tableAttributes.items():

            # Iterar sobre json
            for typeData in self.jsonDSData['DataSt']:
                # Buscar entre tipos de datos el STRING
                for details in typeData[dataType]:
                    for db, syntax in details.items():
                        if (db == dbType):
                            newDic[attribName] = (syntax)

        return newDic

    # todo: pensar en optimizacion a futuro, pasandole directamente el listado de elementos a insertar
    def insertIntoTableQuery(self, dbType:int, tableData:dict, tableName:str):
        #Inserta datos cuando la tabla tiene una pk definida
        returnQuery = ""
        dbType = DbType.DbType(dbType).name
        #tableData = DBDataParser.removeEmptyAttributes(tableData)
        if (dbType == "SQLITE"):
            returnQuery = "INSERT INTO " + tableName + "("
            tmpQuery = "VALUES( "
            first = 0
            for attribute, value in tableData.items():
                if(first > 0):
                    returnQuery += ", "
                    tmpQuery += ", "

                first = 1
                returnQuery += attribute
                tmpQuery += value

            # quitar ',' del final
            tmpQuery = tmpQuery + " );"
            returnQuery = returnQuery+ ") " + tmpQuery

        elif(dbType == "MYSQL"):
            pass


        return returnQuery
    @staticmethod
    def removeEmptyAttributes(tableAttributes:dict):
        # Devuelve diccionario, retirando los elementos que tengan una llave pero no valor asociado o vacio
        returnDict = {}
        for key, val in tableAttributes.items():
            if(len(val) > 0 and val != None):
                returnDict[key] = val

        return returnDict

    @staticmethod
    def putQuotationMarksRequiredDataTypes(tableAttributes:dict, tableData:dict):
        returnDict = {}
        #dbType = DbType.DbType(dbType).name
        tableData = DBDataParser.removeEmptyAttributes(tableData)

        for key, val in tableData.items():
            if(tableAttributes[key]=="STRING"):
                returnDict[key] = '"' + val + '"'
            else:
                returnDict[key] = val

        return returnDict

    def createTableQueryConstructorWithPK(self, dbType: int, tableAttributes:dict, tableName:str, tablePK:str):
        dbType = DbType.DbType(dbType).name
        returnQuery = ""

        if(dbType == "SQLITE"):
            returnQuery = "CREATE TABLE " + tableName + "( "
            # Usarla para agregar los otros atributos
            tmpQuery = ""

            for attribute, dataType in tableAttributes.items():
                if (attribute == tablePK):
                    returnQuery += attribute + " " + dataType + " PRIMARY KEY"
                else:
                    tmpQuery += (", " + attribute + " " + dataType)

            returnQuery += tmpQuery + ");"
        elif(dbType == "MYSQL"):

            # TODO: Implementar para Mysql, hace falta implementar el connector correspondiente
            pass



        return returnQuery

    def createTableQueryConstructorNoPK(self, dbType: int, tableAttributes:dict, tableName:str):
        dbType = DbType.DbType(dbType).name
        returnQuery = ""

        if(dbType == "SQLITE"):
            returnQuery = "CREATE TABLE " + tableName + "( id INTEGER PRIMARY KEY AUTOINCREMENT"

            for attribute, dataType in tableAttributes.items():
                returnQuery += (", " + attribute + " " + dataType)

            returnQuery += ");"
        elif(dbType == "MYSQL"):
            # TODO: Implementar para Mysql, hace falta implementar el connector correspondiente
            pass


        return returnQuery