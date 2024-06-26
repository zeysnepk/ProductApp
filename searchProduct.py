
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 423)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 80, 261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_product_code = QtWidgets.QLineEdit(Form)
        self.lineEdit_product_code.setGeometry(QtCore.QRect(50, 150, 191, 21))
        self.lineEdit_product_code.setObjectName("lineEdit_product_code")
        self.label_product_code = QtWidgets.QLabel(Form)
        self.label_product_code.setGeometry(QtCore.QRect(120, 120, 41, 20))
        self.label_product_code.setObjectName("label_product_code")
        self.pushButton_search = QtWidgets.QPushButton(Form)
        self.pushButton_search.setGeometry(QtCore.QRect(90, 190, 100, 32))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_invalid_code = QtWidgets.QLabel(Form)
        self.label_invalid_code.setGeometry(QtCore.QRect(250, 150, 211, 16))
        self.label_invalid_code.setText("")
        self.label_invalid_code.setObjectName("label_invalid_code")
        self.label_message = QtWidgets.QLabel(Form)
        self.label_message.setGeometry(QtCore.QRect(30, 240, 361, 31))
        self.label_message.setText("")
        self.label_message.setObjectName("label_message")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 250, 401, 141))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Search Product:"))
        self.label_product_code.setText(_translate("Form", "Code:"))
        self.pushButton_search.setText(_translate("Form", "SEARCH"))

