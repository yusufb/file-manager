# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat Jun 07 15:55:57 2014
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
        Form.resize(556, 433)
        Form.setA
        self.baslikLabel = QtGui.QLabel(Form)
        self.baslikLabel.setGeometry(QtCore.QRect(230, 10, 46, 13))
        self.baslikLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.baslikLabel.setObjectName(_fromUtf8("baslikLabel"))
        self.baslikLabel.setText("")
        
        '''
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(130, 90, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))'''
        
        self.pic = QtGui.QLabel(Form)
        self.pic.setGeometry(10, 10, 400, 600)
        self.pic.setPixmap(QtGui.QPixmap('../resources/img/buffalo-fm.png'))
        
        self.infoLabel = QtGui.QLabel(Form)
        self.infoLabel.setGeometry(QtCore.QRect(230, 290, 46, 13))
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.nameLabel = QtGui.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(230, 320, 46, 13))
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "About Buffalo File Manager", None))
        self.baslikLabel.setText(_translate("Form", "baslik", None))
        self.infoLabel.setText(_translate("Form", "info", None))
        self.nameLabel.setText(_translate("Form", "names", None))


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