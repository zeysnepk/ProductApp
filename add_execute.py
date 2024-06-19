import sqlite3
from PyQt5.QtWidgets import QWidget
from addProduct import Ui_Form

class addWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        self.con = sqlite3.connect("Product.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, code TEXT, category TEXT, count INT)")
        self.con.commit()
        
        self.ui.pushButton_add.clicked.connect(self.click)
        
        
    def click(self):
        
        self.product_name = self.ui.lineEdit_product_name.text()
        self.product_code = self.ui.lineEdit_product_code.text()
        self.category = self.ui.comboBox_category.currentText()
        self.category_index = self.ui.comboBox_category.currentIndex()
        self.count = self.ui.spinBox_count.value()
        
        if self.product_name == "":
            self.ui.label_invalid_name.setText("Please enter name!")
            
        elif self.product_code == "":
            self.ui.label_invalid_code.setText("Please enter code!")
            
        elif self.category_index == 0:
            self.ui.label_invalid_category.setText("Please select a category!")
            
        else:
            self.cursor.execute("SELECT *FROM products WHERE code = ?",(self.product_code,))
            codeList = self.cursor.fetchall()
            
            if len(codeList) == 0:
                self.ui.label_message.setText("Added product")
                
                self.cursor.execute("INSERT INTO products VALUES(?,?,?,?)",(self.product_name,self.product_code,self.category,self.count))
                self.con.commit()
                
            
            else:
                self.ui.label_message.setText("The product has already exists!")
                
        
    