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
        self.fileSystemModel.setReadOnly(False)
        self.root = self.fileSystemModel.setRootPath('.')
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(self.root)
        self.treeView.setMinimumWidth(Dialog.width())
        self.verticalLayout = QtGui.QVBoxLayout(self.treeView)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        

        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(0, 250, 216, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtLine = QtGui.QLineEdit(self.widget1)
        self.txtLine.setObjectName(_fromUtf8("txtLine"))
        self.horizontalLayout.addWidget(self.txtLine)
        self.showDir = QtGui.QPushButton(self.widget1)
        self.showDir.setText(QtGui.QApplication.translate("Dialog", "show dir", None, QtGui.QApplication.UnicodeUTF8))
        self.showDir.setObjectName(_fromUtf8("showDir"))
        self.horizontalLayout.addWidget(self.showDir)

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
    
    
    sys.exit(app.exec_())