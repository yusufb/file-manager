# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ftpConnWidget.ui'
#
# Created: Tue Apr 08 17:14:53 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    
    colors = ["Red", "Blue", "Green", "White", "Black", "Cyan", "Magneta", "Yellow", "Gray"]
    
    def setupUi(self, Form2):
        Form2.setObjectName(_fromUtf8("Form2"))
        Form2.resize(380, 140)
        Form2.setMinimumSize(QtCore.QSize(380,140))
        Form2.setMaximumSize(QtCore.QSize(380,140))
        
        self.name = QtGui.QLineEdit(Form2)
        self.name.setGeometry(QtCore.QRect(80, 20, 280, 20))
        self.name.setObjectName(_fromUtf8("name"))
        
        self.comboBox = QtGui.QComboBox(Form2)
        self.comboBox.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        
        for color in self.colors:
            self.comboBox.addItem(_fromUtf8(color))

        self.label = QtGui.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form2)
        self.label_2.setGeometry(QtCore.QRect(20, 22, 60, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form2)
        self.label_3.setGeometry(QtCore.QRect(20, 52, 60, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        
        self.addButton = QtGui.QPushButton(Form2)
        self.addButton.setGeometry(QtCore.QRect(18, 92, 81, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.cancelButton = QtGui.QPushButton(Form2)
        #self.addButton.clicked.connect(self.connectFTP)
        self.cancelButton.setGeometry(QtCore.QRect(108, 92, 81, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Create Tag", None))
        self.label_2.setText(_translate("Form", "Tag Name :", None))
        self.label_3.setText(_translate("Form", "Color :", None))

        self.addButton.setText(_translate("Form", "Add", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)

    Dialog.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
    Dialog.show()
    Dialog.setFixedHeight(Dialog.height())
    Dialog.setFixedWidth(Dialog.width())
    print "dialog ui is created"
    
    sys.exit(app.exec_())
