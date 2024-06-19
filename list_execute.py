import sqlite3
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from listProducts import Ui_Form


class listWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        con = sqlite3.connect("Product.db")
        cursor = con.cursor()
        
        cursor.execute("SELECT *FROM products")
        listProducts = cursor.fetchall()
        
        self.total_count = 0
        self.total_type = 0
        
        for i in listProducts:
            self.total_count += i[3]
            self.total_type += 1
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(i[0]))
            self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(i[2]))
            self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(str(i[3])))
    
        
