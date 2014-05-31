# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prop.ui'
#
# Created: Tue May 27 19:56:10 2014
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
        Form.resize(330, 400)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 329, 399))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pathLabel = QtGui.QLabel(self.tab)
        self.pathLabel.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(81, 30, 235, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 101, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sizeLabel = QtGui.QLabel(self.layoutWidget)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.verticalLayout.addWidget(self.sizeLabel)
        self.createdLabel_2 = QtGui.QLabel(self.layoutWidget)
        self.createdLabel_2.setObjectName(_fromUtf8("createdLabel_2"))
        self.verticalLayout.addWidget(self.createdLabel_2)
        self.lastmodiflabel = QtGui.QLabel(self.layoutWidget)
        self.lastmodiflabel.setObjectName(_fromUtf8("lastmodiflabel"))
        self.verticalLayout.addWidget(self.lastmodiflabel)
        self.layoutWidget1 = QtGui.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 80, 196, 101))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.sizeValueLabel = QtGui.QLabel(self.layoutWidget1)
        self.sizeValueLabel.setObjectName(_fromUtf8("sizeValueLabel"))
        self.verticalLayout_2.addWidget(self.sizeValueLabel)
        self.createdValueLabel_2 = QtGui.QLabel(self.layoutWidget1)
        self.createdValueLabel_2.setObjectName(_fromUtf8("createdValueLabel_2"))
        self.verticalLayout_2.addWidget(self.createdValueLabel_2)
        self.lastmodifValuelabel = QtGui.QLabel(self.layoutWidget1)
        self.lastmodifValuelabel.setObjectName(_fromUtf8("lastmodifValuelabel"))
        self.verticalLayout_2.addWidget(self.lastmodifValuelabel)
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 60, 306, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(81, 30, 235, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.permissionLabel = QtGui.QLabel(self.layoutWidget_2)
        self.permissionLabel.setObjectName(_fromUtf8("permissionLabel"))
        self.verticalLayout_9.addWidget(self.permissionLabel)
        self.pathLabel_2 = QtGui.QLabel(self.tab_2)
        self.pathLabel_2.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.pathLabel_2.setObjectName(_fromUtf8("pathLabel_2"))
        self.layoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(120, 80, 196, 31))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.permissionValueLabel = QtGui.QLabel(self.layoutWidget_3)
        self.permissionValueLabel.setObjectName(_fromUtf8("permissionValueLabel"))
        self.verticalLayout_10.addWidget(self.permissionValueLabel)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 306, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Properties", None))
        self.pathLabel.setText(_translate("Form", "Location :", None))
        self.sizeLabel.setText(_translate("Form", "Size :", None))
        self.createdLabel_2.setText(_translate("Form", "Created Time :", None))
        self.lastmodiflabel.setText(_translate("Form", "Last Modified Time : ", None))
        self.sizeValueLabel.setText(_translate("Form", "TextLabel", None))
        self.createdValueLabel_2.setText(_translate("Form", "TextLabel", None))
        self.lastmodifValuelabel.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "General", None))
        self.permissionLabel.setText(_translate("Form", "Permission :", None))
        self.pathLabel_2.setText(_translate("Form", "Location :", None))
        self.permissionValueLabel.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Permission", None))



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