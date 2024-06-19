import time
import sqlite3
from register import Ui_Form
from PyQt5.QtWidgets import QWidget


class registerWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        
        self.con = sqlite3.connect("login.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members (name TEXT, surname TEXT, username TEXT, password TEXT, country TEXT)")
        self.con.commit()
        
        self.ui.lineEdit_name.textChanged.connect(self.clickName)
        self.ui.lineEdit_surname.textChanged.connect(self.clickSurname)
        self.ui.lineEdit_username.textChanged.connect(self.clickUsername)
        self.ui.lineEdit_password.textChanged.connect(self.clickPassword)
        
        self.boolsValue = 0
        self.ui.checkBox_confirm.clicked.connect(self.boolValue)
        
        
        self.ui.pushButton_send.clicked.connect(self.click)
        
        
        
    def clickName(self):
        self.ui.label_name.clear()
    
    def clickSurname(self):
        self.ui.label_surname.clear()
        
    def clickUsername(self):
        self.ui.label_username.clear()
        
    def clickPassword(self):
        self.ui.label_password.clear()
        
    def boolValue(self):
        self.boolsValue = 1
        
    def click(self):
        self.register_accept = 0
        
        if self.boolsValue == 0:
            self.ui.label_text.setText("Please confirm!")
            
        else:
            name_input = self.ui.lineEdit_name.text()
            surname_input = self.ui.lineEdit_surname.text()
            username_input = self.ui.lineEdit_username.text()
            password_input = self.ui.lineEdit_password.text()
            country_input = self.ui.comboBox_country.currentText()
            
            self.cursor.execute("SELECT *FROM members WHERE username = ?",(username_input,))
            usernameList = self.cursor.fetchall()
            
            if country_input == "Country":
                self.ui.label_text.setText("Please select a valid country!")
                
            elif name_input == "":
                self.ui.label_text.setText("Please enter name!")
                
            elif surname_input == "":
                self.ui.label_text.setText("Please enter surname!")
                
            elif username_input == "":
                self.ui.label_text.setText("Please enter username!")
                
            elif password_input == "":
                self.ui.label_text.setText("Please enter password!")
            
            elif len(usernameList) == 0:
                self.cursor.execute("INSERT INTO members VALUES(?,?,?,?,?)",(name_input,surname_input,username_input,password_input,country_input))
                self.con.commit()
                
                self.ui.label_text.setText("Registering...")
                time.sleep(1)
                self.ui.label_text.setText("Registration Completed!") 
                self.register_accept = 1
                self.hide()
                
            else:
                self.ui.label_text.setText("The username has already exists!")    
            
            
        
        