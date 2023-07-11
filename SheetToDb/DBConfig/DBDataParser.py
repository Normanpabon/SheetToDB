import json
from DBConnectors import DbType
class DBDataParser:
    # DS = DataStructures


    def __init__(self):
        self.jsonFile = open("/../Jsons/DbDataStructureMapper.json")
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
