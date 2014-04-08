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
        
    def main(self):
        self.showMaximized()
        print "window is showed"
        
    def connectActions(self):
        self.showDir.clicked.connect(self.callShowDir)
        self.currentDirTxtLine.returnPressed.connect(self.callShowDir)
        self.newDirButton.clicked.connect(self.callNewDir)
        self.treeView.clicked.connect(self.treeviewClicked)
    
    def callNewDir(self):
        import newDir
        newDir.newDir(self.currentDir)
    
    def callShowDir(self):
        import showDir
        self.currentDir = showDir.showDir(self.currentDirTxtLine.text())
    
    def treeviewClicked(self, index):
        newPath = str(self.currentDir) + "/" + index.data().toString()
        if isdir(newPath):
            self.currentDir = newPath
            print "current dir is '" + self.currentDir + "'"
            self.currentDirTxtLine.setText(self.currentDir)
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = WindowSource()
    hwl1.main()
    sys.exit(app.exec_())