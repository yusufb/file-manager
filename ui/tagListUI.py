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
        self.tags = QtGui.QTableWidget(Form)
        self.tags.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.tags.verticalHeader().setVisible(False)
        self.tags.SelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tags.EditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tags.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.removeButton = QtGui.QPushButton(Form)
        self.removeButton.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        
        self.deleteThisTag = QtGui.QPushButton(Form)
        self.deleteThisTag.setGeometry(QtCore.QRect(290, 270, 100, 23))
        self.deleteThisTag.setObjectName(_fromUtf8("deleteThisTag"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Tag", None))
        self.removeButton.setText(_translate("Form", "Remove", None))
        self.deleteThisTag.setText(_translate("Form", "Delete This Tag", None))
        
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


