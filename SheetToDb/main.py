import tkinter as tk
from FileProcessing import CsvHandler
from FileProcessing import DataType


def main():

    # Pruebas
    CsvObj1 = CsvHandler.CsvHanlder("", "students.csv", 'UTF-8')
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
    #root.mainloop()


if __name__ == '__main__':
    main()


