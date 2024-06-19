import sqlite3
from PyQt5.QtWidgets import QWidget
from removeProduct import Ui_Form



class removeWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        self.con = sqlite3.connect("Product.db")
        self.cursor = self.con.cursor()
        
        self.ui.lineEdit_code.editingFinished.connect(self.clickCode)
        
        self.ui.pushButton_remove.clicked.connect(self.click)
        
    def clickCode(self):
        
        self.product_code = self.ui.lineEdit_code.text()
        
        
        self.cursor.execute("SELECT *FROM products WHERE code = ?",(self.product_code,))
        self.listData = self.cursor.fetchall()
        
        if len(self.listData) == 0:
            self.ui.label_product_information.setText(" ")
            self.ui.label_message.setText("Product not found!")
        
        else:
            for i in self.listData:
                self.product_code_to_remove = i[1]
                self.count_to_remove = i[3]
                self.ui.label_product_information.setText("Product Name:   " + str(i[0]) + "\nProduct Category:   " + str(i[2]) + "\nProduct Count:   " + str(i[3]))
                    
        
    def click(self):
        
        self.productCode = self.ui.lineEdit_code.text()
        
        self.count = self.ui.spinBox_count.value()
        
        try:
            if self.count > self.count_to_remove:
                self.ui.label_message.setText("The count of " + self.productCode + " coded product is " + str(self.count_to_remove) + "!")
            
            elif self.count == self.count_to_remove:
                self.cursor.execute("DELETE FROM products WHERE code = ?",(self.productCode,))
                self.con.commit()
                
                self.ui.label_message.setText("The " + self.productCode + " coded product is deleted.") 
                
            else:
                self.new_count = self.count_to_remove - self.count
                
                self.cursor.execute("UPDATE products SET count = ? WHERE code = ?",(self.new_count,self.productCode))
                self.con.commit()
                
                self.ui.label_message.setText("The " + self.productCode + " coded product is decreased.") 
                
        except AttributeError:
                self.ui.label_message.setText("Please enter invalid code!")
                
        