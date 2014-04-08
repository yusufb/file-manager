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
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(189, 172)
        self.hostTxt = QtGui.QLineEdit(Form)
        self.hostTxt.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.hostTxt.setObjectName(_fromUtf8("hostTxt"))
        self.portTxt = QtGui.QLineEdit(Form)
        self.portTxt.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.portTxt.setObjectName(_fromUtf8("portTxt"))
        self.usernameTxt = QtGui.QLineEdit(Form)
        self.usernameTxt.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.usernameTxt.setObjectName(_fromUtf8("usernameTxt"))
        self.passwordTxt = QtGui.QLineEdit(Form)
        self.passwordTxt.setGeometry(QtCore.QRect(60, 100, 113, 20))
        self.passwordTxt.setObjectName(_fromUtf8("passwordTxt"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("hostLabel"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.connectButton = QtGui.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(80, 140, 91, 23))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.cancelButton = QtGui.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(0, 140, 81, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FTP Connection", None))
        self.label.setText(_translate("Form", "Host", None))
        self.label_2.setText(_translate("Form", "Port", None))
        self.label_3.setText(_translate("Form", "Username", None))
        self.label_4.setText(_translate("Form", "Password", None))
        self.connectButton.setText(_translate("Form", "Connect", None))
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
