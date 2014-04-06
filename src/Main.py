from PyQt4 import QtCore,QtGui
import sys
from ui import *
from modules import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class hwl(QtGui.QDialog,mainWindow.Ui_Dialog):
    def __init__(self,parent=None):
        super(hwl,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
    def main(self):
        self.showMaximized()
    def connectActions(self):
        self.showDir.clicked.connect(self.showDirFunc)
        self.txtLine.returnPressed.connect(self.showDirFunc)
        
    def showDirFunc(self):
        self.root = self.fileSystemModel.setRootPath(self.txtLine.text())
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(self.root)
        
    def myprint(self):
        self.txtLine.setText('Python -- ')        
        self.txtEdit.setText('This')
#         self.lblShow.setText('is a test')
        
    def mypwd(self):
        fdlist = ""
        for fd in list.listFilesAndDirs():
            fdlist += fd[1] + " "
            print fd[1]
        
        self.txtLine.setText( fdlist )
        
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = hwl()
    hwl1.main()
    sys.exit(app.exec_())