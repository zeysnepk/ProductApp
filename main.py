
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 424)
        MainWindow.setMinimumSize(QtCore.QSize(489, 424))
        MainWindow.setMaximumSize(QtCore.QSize(489, 424))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 181, 71))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 231, 20))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(130, 140, 231, 20))
        self.label_warning.setObjectName("label_warning")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(125, 220, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(125, 260, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_sales = QtWidgets.QLabel(self.centralwidget)
        self.label_sales.setGeometry(QtCore.QRect(260, 220, 81, 16))
        self.label_sales.setText("")
        self.label_sales.setObjectName("label_sales")
        self.label_purchases = QtWidgets.QLabel(self.centralwidget)
        self.label_purchases.setGeometry(QtCore.QRect(260, 260, 81, 16))
        self.label_purchases.setText("")
        self.label_purchases.setObjectName("label_purchases")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(127, 240, 231, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 280, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 42))
        self.menubar.setObjectName("menubar")
        self.menuHomepage = QtWidgets.QMenu(self.menubar)
        self.menuHomepage.setTearOffEnabled(True)
        self.menuHomepage.setToolTipsVisible(True)
        self.menuHomepage.setObjectName("menuHomepage")
        self.menuProducts = QtWidgets.QMenu(self.menubar)
        self.menuProducts.setObjectName("menuProducts")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Product = QtWidgets.QAction(MainWindow)
        self.actionAdd_Product.setObjectName("actionAdd_Product")
        self.actionRemove_Product = QtWidgets.QAction(MainWindow)
        self.actionRemove_Product.setObjectName("actionRemove_Product")
        self.actionList_Products = QtWidgets.QAction(MainWindow)
        self.actionList_Products.setObjectName("actionList_Products")
        self.actionSearch_Product = QtWidgets.QAction(MainWindow)
        self.actionSearch_Product.setObjectName("actionSearch_Product")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.menuProducts.addAction(self.actionAdd_Product)
        self.menuProducts.addAction(self.actionRemove_Product)
        self.menuProducts.addAction(self.actionList_Products)
        self.menuProducts.addAction(self.actionSearch_Product)
        self.menuExit.addAction(self.actionLogin)
        self.menuExit.addAction(self.actionRegister)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuHomepage.menuAction())
        self.menubar.addAction(self.menuProducts.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.label_warning.setText(_translate("MainWindow", "!Please login to see sales informations!"))
        self.label_4.setText(_translate("MainWindow", "Total Product Type:"))
        self.label_5.setText(_translate("MainWindow", "Total Products:"))
        self.menuHomepage.setTitle(_translate("MainWindow", "Homepage"))
        self.menuProducts.setTitle(_translate("MainWindow", "Products"))
        self.menuExit.setTitle(_translate("MainWindow", "Settings"))
        self.actionAdd_Product.setText(_translate("MainWindow", "Add Product"))
        self.actionRemove_Product.setText(_translate("MainWindow", "Remove Product"))
        self.actionList_Products.setText(_translate("MainWindow", "List Products"))
        self.actionSearch_Product.setText(_translate("MainWindow", "Search Product"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
