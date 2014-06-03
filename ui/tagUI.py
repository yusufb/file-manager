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
        Form2.resize(450, 200)
        self.path = QtGui.QLineEdit(Form2)
        self.path.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.path.setObjectName(_fromUtf8("path"))
        
        self.comboBox = QtGui.QComboBox(Form2)
        self.comboBox.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        
        '''for color in self.colors:
            self.comboBox.addItem(_fromUtf8(color))
        '''
        self.label_2 = QtGui.QLabel(Form2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.addButton = QtGui.QPushButton(Form2)
        self.addButton.setGeometry(QtCore.QRect(80, 140, 91, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.cancelButton = QtGui.QPushButton(Form2)
        #self.addButton.clicked.connect(self.connectFTP)
        self.cancelButton.setGeometry(QtCore.QRect(0, 140, 81, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Add to Tags", None))
        self.label_2.setText(_translate("Form", "Path", None))
        self.label_3.setText(_translate("Form", "Tags", None))

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
