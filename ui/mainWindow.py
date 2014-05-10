from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "File Manager", None, QtGui.QApplication.UnicodeUTF8))
        
        self.treeView = QtGui.QTreeView(Dialog)
        self.fileSystemModel = QtGui.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.root = self.fileSystemModel.setRootPath('.')
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(self.root)
        self.treeView.setMinimumWidth(Dialog.width())
        print "treeview of dir is created"
        
        self.verticalLayout = QtGui.QVBoxLayout(self.treeView)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        

        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(0, 250, 216, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.currentDirTxtLine = QtGui.QLineEdit(self.widget1)
        self.currentDirTxtLine.setObjectName(_fromUtf8("currentDirTxtLine"))
        self.horizontalLayout.addWidget(self.currentDirTxtLine)
        self.showDir = QtGui.QPushButton(self.widget1)
        self.showDir.setText(QtGui.QApplication.translate("Dialog", "show dir", None, QtGui.QApplication.UnicodeUTF8))
        self.showDir.setObjectName(_fromUtf8("showDir"))
        self.horizontalLayout.addWidget(self.showDir)
        
        self.parentDir = QtGui.QPushButton(self.widget1)
        self.parentDir.setText(QtGui.QApplication.translate("Dialog", "..", None, QtGui.QApplication.UnicodeUTF8))
        self.parentDir.setObjectName(_fromUtf8("parentDir"))
        self.horizontalLayout.addWidget(self.parentDir)
        
        self.newDirButton = QtGui.QPushButton(self.widget1)
        self.newDirButton.setText(QtGui.QApplication.translate("Dialog", "new dir", None, QtGui.QApplication.UnicodeUTF8))
        self.newDirButton.setObjectName(_fromUtf8("newDirButton"))
        self.horizontalLayout.addWidget(self.newDirButton)
        
        self.newFileButton = QtGui.QPushButton(self.widget1)
        self.newFileButton.setText(QtGui.QApplication.translate("Dialog", "new file", None, QtGui.QApplication.UnicodeUTF8))
        self.newFileButton.setObjectName(_fromUtf8("newFileButton"))
        self.horizontalLayout.addWidget(self.newFileButton)        
        
        self.openFileButton = QtGui.QPushButton(self.widget1)
        self.openFileButton.setText(QtGui.QApplication.translate("Dialog", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.openFileButton.setObjectName(_fromUtf8("openFileButton"))
        self.horizontalLayout.addWidget(self.openFileButton)

        self.renameButton = QtGui.QPushButton(self.widget1)
        self.renameButton.setText(QtGui.QApplication.translate("Dialog", "rename", None, QtGui.QApplication.UnicodeUTF8))
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        self.horizontalLayout.addWidget(self.renameButton)
        
        self.deleteButton = QtGui.QPushButton(self.widget1)
        self.deleteButton.setText(QtGui.QApplication.translate("Dialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
                        
    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
    Dialog.showMaximized()
#     Dialog.setFixedHeight(Dialog.height())
#     Dialog.setFixedWidth(Dialog.width())
    print "dialog ui is created"
    
    sys.exit(app.exec_())