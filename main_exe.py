import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow
from login_execute import loginWindow
from register_execute import registerWindow
from add_execute import addWindow
from search_execute import searchWindow
from remove_execute import removeWindow
from list_execute import listWindow


class Main(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        self.default_widget = self.ui.centralwidget
        
        self.ui.menuHomepage.setEnabled(True)
        self.ui.menuHomepage.triggered.connect(self.Home)
        
        self.ui.actionLogin.triggered.connect(self.Login)
        self.ui.actionRegister.triggered.connect(self.Register)
        
        self.ui.actionAdd_Product.setEnabled(False)
        self.ui.actionList_Products.setEnabled(False)
        self.ui.actionRemove_Product.setEnabled(False)
        self.ui.actionSearch_Product.setEnabled(False)
        
        self.ui.actionAdd_Product.triggered.connect(self.Add)
        self.ui.actionRemove_Product.triggered.connect(self.Remove)
        self.ui.actionSearch_Product.triggered.connect(self.Search)
        self.ui.actionList_Products.triggered.connect(self.List)
        
        self.ui.actionExit.triggered.connect(self.exit)
        
        
        
        
        self.list = listWindow()
        
         
    def Home(self):
        print("1")
        
        QMainWindow.setCentralWidget(self, self.default_widget)
        
        
    def Login(self):
        
        self.login = loginWindow()
        self.login.show()
        
        self.login.ui.pushButton_send.clicked.connect(self.changeText)
        
    def changeText(self):
        
        if self.login.login_accept == 1:
            self.ui.label_2.setText(self.login.name + " " + self.login.surname)
            self.ui.label_warning.setText("Current Status:")
            self.ui.label_sales.setText(str(self.list.total_type))
            self.ui.label_purchases.setText(str(self.list.total_count))
            
            self.ui.actionAdd_Product.setEnabled(True)
            self.ui.actionList_Products.setEnabled(True)
            self.ui.actionRemove_Product.setEnabled(True)
            self.ui.actionSearch_Product.setEnabled(True)
        
    def Register(self):
        
        self.register = registerWindow()
        self.register.show()
        
        self.register.ui.pushButton_send.clicked.connect(self.registerAccept)
        
    def registerAccept(self):
        
        if self.register.register_accept == 1:
            log = self.Login()
            self.login.ui.label_text.setText("Succesfully Registration Please Log In")
        
    def Add(self):
        
        self.add = addWindow()
        QMainWindow.setCentralWidget(self, self.add)
        
    def Remove(self):
        
        self.remove = removeWindow()
        QMainWindow.setCentralWidget(self, self.remove)
        
    def Search(self):
        
        self.search = searchWindow()
        QMainWindow.setCentralWidget(self, self.search)
        
    def List(self):
        
        self.list = listWindow()
        QMainWindow.setCentralWidget(self, self.list)
   
        
    def exit(self):
        
        app.exit()
    



app = QApplication(sys.argv)

window = Main()

window.show()

sys.exit(app.exec_())
