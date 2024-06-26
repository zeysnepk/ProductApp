
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 424)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 60, 261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_product_name = QtWidgets.QLabel(Form)
        self.label_product_name.setGeometry(QtCore.QRect(30, 100, 91, 21))
        self.label_product_name.setObjectName("label_product_name")
        self.lineEdit_product_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_product_name.setGeometry(QtCore.QRect(140, 100, 113, 21))
        self.lineEdit_product_name.setObjectName("lineEdit_product_name")
        self.label_product_code = QtWidgets.QLabel(Form)
        self.label_product_code.setGeometry(QtCore.QRect(30, 136, 91, 20))
        self.label_product_code.setObjectName("label_product_code")
        self.spinBox_count = QtWidgets.QSpinBox(Form)
        self.spinBox_count.setGeometry(QtCore.QRect(90, 220, 42, 22))
        self.spinBox_count.setProperty("value", 1)
        self.spinBox_count.setObjectName("spinBox_count")
        self.lineEdit_product_code = QtWidgets.QLineEdit(Form)
        self.lineEdit_product_code.setGeometry(QtCore.QRect(140, 140, 113, 21))
        self.lineEdit_product_code.setObjectName("lineEdit_product_code")
        self.label_count = QtWidgets.QLabel(Form)
        self.label_count.setGeometry(QtCore.QRect(30, 220, 58, 16))
        self.label_count.setObjectName("label_count")
        self.comboBox_category = QtWidgets.QComboBox(Form)
        self.comboBox_category.setGeometry(QtCore.QRect(100, 170, 131, 32))
        self.comboBox_category.setObjectName("comboBox_category")
        self.comboBox_category.addItem("")
        self.comboBox_category.setItemText(0, "")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.label_category = QtWidgets.QLabel(Form)
        self.label_category.setGeometry(QtCore.QRect(30, 176, 81, 20))
        self.label_category.setObjectName("label_category")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(80, 260, 100, 32))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_message = QtWidgets.QLabel(Form)
        self.label_message.setGeometry(QtCore.QRect(30, 300, 291, 31))
        self.label_message.setText("")
        self.label_message.setObjectName("label_message")
        self.label_invalid_code = QtWidgets.QLabel(Form)
        self.label_invalid_code.setGeometry(QtCore.QRect(270, 140, 191, 16))
        self.label_invalid_code.setText("")
        self.label_invalid_code.setObjectName("label_invalid_code")
        self.label_invalid_category = QtWidgets.QLabel(Form)
        self.label_invalid_category.setGeometry(QtCore.QRect(240, 180, 221, 16))
        self.label_invalid_category.setText("")
        self.label_invalid_category.setObjectName("label_invalid_category")
        self.label_invalid_name = QtWidgets.QLabel(Form)
        self.label_invalid_name.setGeometry(QtCore.QRect(270, 100, 191, 16))
        self.label_invalid_name.setText("")
        self.label_invalid_name.setObjectName("label_invalid_name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Product Informations:"))
        self.label_product_name.setText(_translate("Form", "Product Name:"))
        self.label_product_code.setText(_translate("Form", "Product Code:"))
        self.label_count.setText(_translate("Form", "Count:"))
        self.comboBox_category.setItemText(1, _translate("Form", "Clothing"))
        self.comboBox_category.setItemText(2, _translate("Form", "Food"))
        self.comboBox_category.setItemText(3, _translate("Form", "Electronics"))
        self.comboBox_category.setItemText(4, _translate("Form", "Care"))
        self.comboBox_category.setItemText(5, _translate("Form", "Health"))
        self.label_category.setText(_translate("Form", "Category:"))
        self.pushButton_add.setText(_translate("Form", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
