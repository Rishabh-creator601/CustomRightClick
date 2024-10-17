from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from enlarged_windows import EnlargedWindow
import sys ,os,pyperclip,time
from files_tools import show_files,path_scripts,read_file,write_file

os.chdir(r"C:\codes\GUIs") 













class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi("Scripts.ui",self)
        
        ## DEFAULT SETTINGS 
        self.setWindowTitle("--Scripts")
        self.content.setAcceptRichText(False)
        self.content.setFontFamily("sans-serif")
        self.tabs.setCurrentIndex(0)


        
        
        ## TAB 1 : FILES 
        self.filesList.addItems(show_files())
        self.filesHeader.setText(f"FILE SOURCE : {path_scripts}")
        self.showInfo(len(show_files()))
        self.filesList.itemSelectionChanged.connect(self.render_file)
        self.itemsCheck.stateChanged.connect(self.show_items)
        self.renderBtn.clicked.connect(self.render_items)
        
        
        
        ## TAB 2 : TEXT
        self.copy_cont.clicked.connect(self.copy_) 
        self.save_file.clicked.connect(self.save_cont)
        self.clear_btn.clicked.connect(self.clear_area)
        
        ## New window
        self.show_enlarged.clicked.connect(self.show_data)
        
        self.enlarged_view = EnlargedWindow(self)
        
    
    
    def show_items(self):
        if self.itemsCheck.isChecked():
            self.filesList.clear()
            items = sorted(show_files(all=True),key=len)
            self.filesList.addItems(items)
            self.showInfo(len(items))
            
        if self.itemsCheck.isChecked() == False:
            self.filesList.clear()
            items = show_files()
            self.filesList.addItems(items)
            self.showInfo(len(items))
    
    
    def showInfo(self,length_items):
        self.itemsInfo.setText(f"TOTAL ITEMS : {length_items}")
    
    def render_file(self):
        self.renderBtn.setEnabled(True) if len(self.filesList.selectedItems()) > 0  else self.renderBtn.setEnabled(False)
        
        
    
    def render_items(self):
       file_name  = [i.text() for  i in self.filesList.selectedItems()][0]
       file_path = f"{path_scripts}/{file_name}"
       data = read_file(file_path)
       self.tabs.setCurrentIndex(1)
       self.front_file_name.setText(file_name)
       self.content.setText(data)
       self.save_file.setEnabled(True)
       self.copy_cont.setEnabled(True)
    
    
    def copy_(self):
        pyperclip.copy(self.content.toPlainText())
        QMessageBox.information(self ,"Info","COPIED !")
    
    
    def save_cont(self):
        file_name = self.front_file_name.text()
        cont = self.content.toPlainText()
        if file_name != "" and cont != "":
            write_file(f"{path_scripts}/{file_name}",cont)
            QMessageBox.information(self ,"Info",f"File {file_name} Saved !")
        
        else:
            QMessageBox.information(self ,"Info","Either Filename or content is empty")
    def show_data(self):
        self.enlarged_view.data.setFontPointSize(10.0)
        self.enlarged_view.data.setText(self.content.toPlainText())
        self.enlarged_view.show()
    
    def clear_area(self):
        self.front_file_name.setText("")
        self.content.setText("")
        
        
    

            
        
            
        
        
        
        
        
        
        
        
        
        
app = QApplication(sys.argv)
ui = Main()

ui.show()
app.exec_()