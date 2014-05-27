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
        Form.resize(375, 270)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 371, 271))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pathLabel = QtGui.QLabel(self.tab)
        self.pathLabel.setGeometry(QtCore.QRect(2, 11, 47, 16))
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setGeometry(QtCore.QRect(61, 11, 291, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 40, 51, 81))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sizeLabel_2 = QtGui.QLabel(self.widget)
        self.sizeLabel_2.setObjectName(_fromUtf8("sizeLabel_2"))
        self.verticalLayout.addWidget(self.sizeLabel_2)
        self.sizeLabel = QtGui.QLabel(self.widget)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.verticalLayout.addWidget(self.sizeLabel)
        self.createdLabel_2 = QtGui.QLabel(self.widget)
        self.createdLabel_2.setObjectName(_fromUtf8("createdLabel_2"))
        self.verticalLayout.addWidget(self.createdLabel_2)
        self.widget1 = QtGui.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(60, 40, 291, 81))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.typeValueLabel = QtGui.QLabel(self.widget1)
        self.typeValueLabel.setObjectName(_fromUtf8("typeValueLabel"))
        self.verticalLayout_2.addWidget(self.typeValueLabel)
        self.sizeValueLabel = QtGui.QLabel(self.widget1)
        self.sizeValueLabel.setObjectName(_fromUtf8("sizeValueLabel"))
        self.verticalLayout_2.addWidget(self.sizeValueLabel)
        self.createdValueLabel_2 = QtGui.QLabel(self.widget1)
        self.createdValueLabel_2.setObjectName(_fromUtf8("createdValueLabel_2"))
        self.verticalLayout_2.addWidget(self.createdValueLabel_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pathLabel.setText(_translate("Form", "Location :", None))
        self.sizeLabel_2.setText(_translate("Form", "File Type :", None))
        self.sizeLabel.setText(_translate("Form", "Size :", None))
        self.createdLabel_2.setText(_translate("Form", "Created :", None))
        self.typeValueLabel.setText(_translate("Form", "TextLabel", None))
        self.sizeValueLabel.setText(_translate("Form", "TextLabel", None))
        self.createdValueLabel_2.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "General", None))
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