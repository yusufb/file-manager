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
        Form.resize(550, 430)
        self.baslikLabel = QtGui.QLabel(Form)
        self.baslikLabel.setGeometry(QtCore.QRect(155, 10, 250, 30))
        self.baslikLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.baslikLabel.setObjectName(_fromUtf8("baslikLabel"))
        self.baslikLabel.setStyleSheet('font-size:18pt;')
        self.baslikLabel.setText("<b>Buffalo File Manager</b>")
        
        '''
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(130, 90, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))'''
        
        self.pic = QtGui.QLabel(Form)
        self.pic.setGeometry(125, 60, 550, 225) #300,225
        self.pic.setPixmap(QtGui.QPixmap('../resources/img/buffalo-fm.png'))
        
        self.infoLabel = QtGui.QLabel(Form)
        self.infoLabel.setGeometry(QtCore.QRect(155, 290, 250, 13))
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.infoLabel.setText("<b><u>B</u>rowse <u>U</u>r <u>F</u>iles & <u>F</u>olders <u>A</u>nd <u>L</u>ive <u>O</u>n</b>")
        self.nameLabel = QtGui.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(0, 320, 550, 80))
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameLabel.setText(u"Yusuf Beyaz, A. Utku Soytaş, Yiğit Anıl<br><br><i>Buffalo File Manager is released under GPL v3 <br> This program is free software: you can redistribute it and/or modify it under the <br> terms of the GNU General Public License as published by the Free Software Foundation </i><br>2014")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "About Buffalo File Manager", None))


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