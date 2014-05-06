from PyQt4 import QtCore,QtGui
import sys
from ui import *
from genericpath import isdir

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
        self.treeviewClicked(self.root)
        
    def main(self):
        #self.showMaximized()
        self.show()
        print "window is showed"
        
    def connectActions(self):
        self.showDir.clicked.connect(self.doShowDir)
        self.currentDirTxtLine.returnPressed.connect(self.doShowDir)
        self.newDirButton.clicked.connect(self.callNewDir)
        self.treeView.clicked.connect(self.treeviewClicked)
        self.newFileButton.clicked.connect(self.callNewFile)
        self.parentDir.clicked.connect(self.showParentDir)
        
    def callNewFile(self):
        import newFile
        newFile.newFile(self.currentDir)
    
    def callNewDir(self):
        import newDir
        newDir.newDir(self.currentDir)
    
    def callShowDir(self):
        import showDir
        self.currentDir = showDir.showDir(self.currentDirTxtLine.text())
    
    def showParentDir(self):
        parentDir = str(self.currentDir).rsplit('/',1)[0]
        if(isdir(parentDir)):
            self.root = self.fileSystemModel.setRootPath(parentDir)
            self.treeView.setModel(self.fileSystemModel)
            self.treeView.setRootIndex(self.root)
            self.currentDir = parentDir
            print "current dir is now " + self.currentDir
            self.currentDirTxtLine.setText(self.currentDir)
        else:
            print parentDir + " is not a directory"
        
    def doShowDir(self):
        newDir = self.currentDirTxtLine.text()
        
        if(isdir(newDir)):
            self.root = self.fileSystemModel.setRootPath(newDir)
            self.treeView.setModel(self.fileSystemModel)
            self.treeView.setRootIndex(self.root)
            self.currentDir = newDir
            print "current dir is now " + self.currentDir
        else:
            print newDir + " is not a directory"
    
    def treeviewClicked(self, index):
        # ***
        print self.fileSystemModel.filePath(index)
        newPath = str(self.fileSystemModel.filePath(index))
        print "new path is " + newPath
        if isdir(newPath):
            self.currentDir = newPath
            print "current dir is '" + self.currentDir + "'"
            self.currentDirTxtLine.setText(self.currentDir)
            self.doShowDir()
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = WindowSource()
    hwl1.main()
    sys.exit(app.exec_())