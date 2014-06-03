# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookmarkListUI.ui'
#
# Created: Sun May 25 15:06:30 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qt
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
        Form.resize(400, 300)
        self.searchList = QtGui.QTableWidget(Form)
        self.searchList.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.searchList.setObjectName(_fromUtf8("searchList"))
        self.searchList.verticalHeader().setVisible(False)
        self.searchList.SelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.searchList.EditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.searchList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.openButton = QtGui.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.openButton.setObjectName(_fromUtf8("openButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Search results", None))
        self.openButton.setText(_translate("Form", "Open", None))
        
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


