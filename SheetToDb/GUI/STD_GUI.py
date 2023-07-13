import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
#from PyQt5 import QtWidgets, uic

class MainGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        loadUi('SheetToDb_main.ui', self)
        self.btnContinuar1.clicked.connect(self.nextScreen)


    def nextScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
class GUI2(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI2, self).__init__()
        loadUi('SheetToDb_main.ui', self)



class main():
    app = QApplication.QStackedWidget()
    mainGUI=MainGUI()
    screen2 = GUI2()
    widget.addWidget(mainGUI)
    widget.addWidget(GUI2)
    widget.show()




main()