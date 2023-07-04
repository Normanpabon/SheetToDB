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

        print("\n\n\n\nBienvenido a SheetToDB ")
        print("\n1.Convertir archivo csv a una base de datos\n2.TEST \n-1 . para salir")
        userInput = input("Ingrese una opcion:")
        if(userInput == "1"):
            print("Ingrese las rutas de los archivos separadas por comas")
        elif(userInput == "2"):
            # Pruebas

            CsvObj1 = CsvHandler.CsvHanlder("Data/", "students.csv", 'UTF-8')
            CsvObj2 = CsvHandler.CsvHanlder("", "studentsV2.csv", 'UTF-8')

            firstLineObj1 = CsvObj1.getFirstLine()

            print(firstLineObj1)

            atributes = DataType.DataType.getAttributesDataTypes(firstLineObj1)

            print(atributes)
            # finPruebas

            # Tk display
            root = tk.Tk()
            c = tk.Canvas(root, width=1080, height=720, bg='black')
            c.pack()
            # root.mainloop()






if __name__ == '__main__':
    main()


