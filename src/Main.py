from PyQt4 import QtCore,QtGui
import sys
from ui import *
from modules import *
from genericpath import isdir
import newDir

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class WindowSource(QtGui.QDialog,mainWindow.Ui_Dialog):
    currentDir = "."
    
    def __init__(self,parent=None):
        super(WindowSource,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        print self.__class__.__name__ + " is initialized"
        
    def main(self):
        self.showMaximized()
        print "window is showed"
        
    def connectActions(self):
        self.showDir.clicked.connect(self.showDirFunc)
        self.currentDirTxtLine.returnPressed.connect(self.showDirFunc)
        self.newDirButton.clicked.connect(self.callNewDir)
        self.treeView.clicked.connect(self.treeviewClicked)
    
    def callNewDir(self):
        nd = newDir.newDir(self.currentDir)
    
    def treeviewClicked(self, index):
        newPath = str(self.currentDir) + "/" + index.data().toString()
        if isdir(newPath):
            self.currentDir = newPath
            print "current dir is '" + self.currentDir + "'"
            self.currentDirTxtLine.setText(self.currentDir)
        

        
    def showDirFunc(self):
        newDir = self.currentDirTxtLine.text()
        
        if(isdir(newDir)):
            self.root = self.fileSystemModel.setRootPath(newDir)
            self.treeView.setModel(self.fileSystemModel)
            self.treeView.setRootIndex(self.root)
            self.currentDir = newDir
            print "current dir is now " + self.currentDir
        else:
            print newDir + " is not a directory"
        
    def mypwd(self):
        fdlist = ""
        for fd in list.listFilesAndDirs():
            fdlist += fd[1] + " "
            print fd[1]
        
        self.currentDirTxtLine.setText( fdlist )
        
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = WindowSource()
    hwl1.main()
    sys.exit(app.exec_())