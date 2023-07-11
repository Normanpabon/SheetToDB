import tkinter as tk
from FileProcessing import CsvHandler
from FileProcessing import DataType
import SheetToDB


def main():

    # Objeto principal

    sheetToDb = SheetToDB.SheetToDB()

    # CLI

    userInput = ""

    while(userInput != "-1"):

        print("\n\n\n\nSheetToDB \t\t- Version A0.1")
        print("-------------------------------------------------------------------------------------\n")
        print("\nBienvenido, el proceso de conversion de sus archivos CSV a una Base de datos iniciara en breve")
        print("---------------------------------------------------------------------------------------------------\n")
        # Pruebas de secuencia de ejecucion

        # 1. El usuario ingresa el o los archivos a procesar
        filesToProccess = input("Ingrese las rutas de los archivos a procesar seguidos de ',' entre ellos\n: ")

        # 2. El listado de PATHS se procesa y se deja la o las rutas de los archivos en una lista
        filesToProccessList = DataType.DataType.separateStrWithComma(filesToProccess)

        # 3. Se recorre la lista de rutas, inicializando los csv en la lista de objetos de tipo cvsHandler contenida en FilesPipeline
        for file in filesToProccessList:
            sheetToDb.addCsvFile(file)

        # 4. Se carga la info de los csv a memoria, guardandose en el atributo readedData de cada objeto csvHandler
        sheetToDb.loadFiles()

        '''
         Nota : Aca ya tendriamos inicializado completamente el obj FilePipeline de la clase SheetToDB (proceso principal)
         Ahora necesitamos inicializar el DatabaseCreator, el constructor de este objeto solo requiere el nombre de la BD a crear
         sin embargo, necesita inicializar otros objetos (atributos internos) antes de seguir (DbServer, TableScheme, DbConnectionManager) 
        '''

        # 5. Se pide al usuario el nombre de la BD a crear y se asigna
        tmpName = input("\nIngrese el nombre de la BD a crear: ")
        sheetToDb.setDbSettings(tmpName)

        # n. Pedir los datos de conexion a la bd y hacer las pruebas de que funcionen #todo implementar


        # 6. Agregar esquemas de tablas al DatabaseCreator
        # Nota: usar el atributo del obj csvHanlder "isReaded" para saber si ya se cargo en memoria el mismo
        sheetToDb.createTablesSchemes()


        # 7. Seleccion de tipo de BD a migrar (todo : implementar, probar solo con sqlite (opc 1) por ahora)
        tmpInput = int(input("\nTipo de bd a crear. \n0.Sqlite\n1.Mysql\n2.SqlServer\nIngrese una opcion:"))
        if(tmpInput == 0):
            # SQLITE
            # Llamar inicializador de la conexion
            # Todo: crear metodo para llamado, por buenas practicas
            sheetToDb.dbSettings.initialiceConnectionManager(tmpInput)

            # Llama la etapa de proceso de las tablas a la bd
            sheetToDb.createDb()
        elif(tmpInput ==1):
            pass
        elif(tmpInput==2):
            pass

        print(sheetToDb)
       # finPruebas






if __name__ == '__main__':
    main()


