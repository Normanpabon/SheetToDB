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


    def insertIntoTableNoPKQuery(self):
        pass

    def insertIntoTableWithPKQuery(self):
        pass
    def createTableQueryConstructorWithPK(self, dbType: int, tableAttributes:dict, tableName:str, tablePK:str):
        dbType = DbType.DbType(dbType).name
        returnQuery = ""

        if(dbType == "SQLITE"):
            returnQuery = "CREATE TABLE " + tableName + "( "
            # Usarla para agregar los otros atributos
            tmpQuery = ""

            for attribute, dataType in tableAttributes.items():
                if (attribute == tablePK):
                    returnQuery += attribute + " " + dataType + "PRIMARY KEY"
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
            returnQuery = "CREATE TABLE " + tableName + "( id INTEGER PRIMARY KEY"

            for attribute, dataType in tableAttributes.items():
                returnQuery += (", " + attribute + " " + dataType)

            returnQuery += ");"
        elif(dbType == "MYSQL"):
            # TODO: Implementar para Mysql, hace falta implementar el connector correspondiente
            pass


        return returnQuery