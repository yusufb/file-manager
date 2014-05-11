from PyQt4 import QtCore,QtGui
import sys
from ui import design
from genericpath import isdir, isfile
from collections import OrderedDict

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class WindowSource(QtGui.QMainWindow,design.Ui_Dialog):
    currentDir = "."
    clickedFile = ""
    clickedFileOrDir = ""
    
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
        
        #new design: self.newDirButton.triggered.connect(self.callNewDir)
        
        self.showDir.clicked.connect(self.doShowDir)
        self.currentDirTxtLine.returnPressed.connect(self.doShowDir)
        self.newDirButton.triggered.connect(self.callNewDir)
        self.treeView.clicked.connect(self.changeclickedFileOrDir)
        self.treeView.doubleClicked.connect(self.treeviewClicked)
        self.newFileButton.triggered.connect(self.callNewFile)
        self.parentDir.triggered.connect(self.showParentDir)
        self.openFileButton.triggered.connect(self.callOpenFile)
        self.renameButton.triggered.connect(self.callRename)
        self.deleteButton.triggered.connect(self.callDelete)
        self.fileTypeButton.triggered.connect(self.callFileTypeInfo)
        
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.rightClickMenu)
        
    def rightClickMenu(self, pos):
        menu = QtGui.QMenu()
        actionsList = OrderedDict((('Open', 'callOpenFile'), ('Rename', 'callRename'), ('Delete', 'callDelete')))
        actions = []
        actionFunctions = []
        
        for k,v in actionsList.iteritems():
            actions.append(menu.addAction(k))
            actionFunctions.append(v)

        action = menu.exec_(self.treeView.mapToGlobal(pos))
        
        for i in range(0, len(actions)):
            if action == actions[i]:
                getattr(self, actionFunctions[i])()
    
    def callFileTypeInfo(self):
        import fileTypeInfo
        fileTypeInfo.fileTypeInfo(self.clickedFileOrDir)
    
    def callDelete(self):
        import deleteFileDir
        if len(self.clickedFileOrDir) > 0:
            deleteFileDir.deleteFileDir(self.clickedFileOrDir)
        
    def callRename(self):
        import renameFileDir
        renameFileDir.renameFileDir(self.clickedFileOrDir)

    def callOpenFile(self):
        print "to open"
        import openFile
        from os.path import isfile
        toOpenFile = self.clickedFile
        if(isfile(toOpenFile)):
            openFile.openFile(toOpenFile)
                
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
        self.clickedFileOrDir = ""
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
        self.clickedFileOrDir = ""
        
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
            self.currentDirTxtLine.setText(self.currentDir)
            self.doShowDir()
        elif isfile(newPath):
            self.clickedFile = newPath
            self.callOpenFile()
    
    def changeclickedFileOrDir(self, index):
        self.clickedFileOrDir = str(self.fileSystemModel.filePath(index)).rsplit('/')[-1]
        from genericpath import isfile
        if isfile(self.clickedFileOrDir):
            self.clickedFile = self.clickedFileOrDir
        print self.clickedFileOrDir + " is clicked"
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = WindowSource()
    hwl1.main()
    sys.exit(app.exec_())