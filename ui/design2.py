# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sun May 11 15:33:50 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(80, 70, 301, 461))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView_2 = QtGui.QTreeView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(430, 70, 301, 461))
        self.treeView_2.setObjectName(_fromUtf8("treeView_2"))
        self.goToDirButton = QtGui.QPushButton(self.centralwidget)
        self.goToDirButton.setGeometry(QtCore.QRect(690, 20, 41, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/go-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goToDirButton.setIcon(icon)
        self.goToDirButton.setFlat(False)
        self.goToDirButton.setObjectName(_fromUtf8("goToDirButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 601, 24))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Directory = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/new-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Directory.setIcon(icon1)
        self.actionNew_Directory.setObjectName(_fromUtf8("actionNew_Directory"))
        self.actionNew_File = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/new-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_File.setIcon(icon2)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))
        self.actionParent_Directory = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/up-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionParent_Directory.setIcon(icon3)
        self.actionParent_Directory.setObjectName(_fromUtf8("actionParent_Directory"))
        self.actionOpen_File = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/open-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_File.setIcon(icon4)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionRename = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon5)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon6)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.toolBar.addAction(self.actionNew_Directory)
        self.toolBar.addAction(self.actionNew_File)
        self.toolBar.addAction(self.actionParent_Directory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOpen_File)
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addAction(self.actionDelete)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.goToDirButton.setText(_translate("MainWindow", "Go", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew_Directory.setText(_translate("MainWindow", "New Directory", None))
        self.actionNew_Directory.setToolTip(_translate("MainWindow", "Create new directory/folder", None))
        self.actionNew_File.setText(_translate("MainWindow", "New File", None))
        self.actionNew_File.setToolTip(_translate("MainWindow", "Create new file", None))
        self.actionParent_Directory.setText(_translate("MainWindow", "Parent Directory", None))
        self.actionParent_Directory.setToolTip(_translate("MainWindow", "Go to parent directory", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File", None))
        self.actionOpen_File.setToolTip(_translate("MainWindow", "Open the selected file", None))
        self.actionRename.setText(_translate("MainWindow", "rename", None))
        self.actionRename.setToolTip(_translate("MainWindow", "Rename file/folder", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete file/directory", None))

