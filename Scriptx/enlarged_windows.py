from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi



class EnlargedWindow(QMainWindow):
    def __init__(self,parent=None,text=None):
        super(EnlargedWindow,self).__init__(parent)
        
        loadUi("enlarged.ui",self)

        self.setWindowTitle("Enlarged View")


        