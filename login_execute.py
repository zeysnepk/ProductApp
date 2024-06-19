import time
import sqlite3
from PyQt5 import QtWidgets
from login import Ui_Form



class loginWindow(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        self.ui.lineEdit_username.textChanged.connect(self.clickUsername)
        self.ui.lineEdit_password.textChanged.connect(self.clickPassword)
        
        self.ui.pushButton_send.clicked.connect(self.click)
        
    def click(self):
        self.login_accept = 0
        
        username_input = self.ui.lineEdit_username.text()
        password_input = self.ui.lineEdit_password.text()
        
        con = sqlite3.connect("login.db")
        
        cursor = con.cursor()

        cursor.execute("SELECT *FROM members WHERE username = ? and password = ?",(username_input, password_input))    
        list_members = cursor.fetchall() 
        
        for i in list_members:
            self.name = i[0]
            self.surname = i[1]
        
        if len(list_members) == 0:
            self.ui.label_text.setText("Try Again!") 
            
            self.ui.lineEdit_username.clear()
            self.ui.lineEdit_password.clear()   
            
        else:

            self.user_name = self.name
            self.user_surname = self.surname
            self.ui.label_text.setText("Successfully Login!")
            self.login_accept = 1
            time.sleep(2)
            self.hide()
    
    def clickUsername(self):
        self.ui.label_username.clear()
        
    def clickPassword(self):
        self.ui.label_password.clear()
        
            