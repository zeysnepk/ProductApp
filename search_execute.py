import sqlite3
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from searchProduct import Ui_Form

class searchWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        self.con = sqlite3.connect("Product.db")
        self.cursor = self.con.cursor()
        
        self.ui.pushButton_search.clicked.connect(self.click)
        
        
    def click(self):
        
        self.code = self.ui.lineEdit_product_code.text()
        
        self.info = " "
        
        self.cursor.execute("SELECT *FROM products WHERE code = ?",(self.code,))
        listInfo = self.cursor.fetchall()
        
        if len(listInfo) == 0:
            self.ui.label_invalid_code.setText("Invalid Code!")
            
        else:
            self.ui.label_invalid_code.setText("")
            
            for i in listInfo[0]:
                self.info += str(i) + " "
              
            self.text = QListWidgetItem(self.info)
            self.ui.listWidget.addItem(self.text)
                

        