from PyQt4 import QtCore,QtGui
import sys
from ui import design
from genericpath import isdir, isfile
from collections import OrderedDict
from src import Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class WindowSource(QtGui.QMainWindow,design.Ui_Dialog):
    currentDir = "."
    clickedFile = ""
    clickedFileOrDir = ""
    activeTreeview = 0
    filter = ""
    
    def __init__(self,parent=None):
        super(WindowSource,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        print self.__class__.__name__ + " is initialized"
        
        self.treeViews = [ self.treeView, self.treeView_2 ]
        self.fileSystemModels = [ self.fileSystemModel, self.fileSystemModel2 ]
        self.roots = [ self.root, self.root2 ]
        
        
        self.treeviewClicked(self.root)
        self.currentDirTxtLine2.setText(self.currentDir)
        
    def main(self):
        #self.showMaximized()
        self.show()
        print "window is showed"
        
    def connectActions(self):
        
        #self.showDir.clicked.connect(self.doShowDir)
        self.currentDirTxtLine.returnPressed.connect(lambda: self.doShowDir(0))
        self.currentDirTxtLine2.returnPressed.connect(lambda: self.doShowDir(1))
        self.newDirButton.triggered.connect(self.callNewDir)
        
        self.homeTreeView.clicked.connect(self.homeTreeviewClicked)
        
        self.treeView.clicked.connect(lambda: self.changeActiveTreeview(0))
        self.treeView_2.clicked.connect(lambda: self.changeActiveTreeview(1))
        self.treeView.clicked.connect(self.changeclickedFileOrDir)
        self.treeView_2.clicked.connect(self.changeclickedFileOrDir)

        
        self.treeView.doubleClicked.connect(self.treeviewClicked)
        self.treeView_2.doubleClicked.connect(self.treeviewClicked)
        
        self.newFileButton.triggered.connect(self.callNewFile)
        self.parentDir.triggered.connect(self.showParentDir)
        self.openFileButton.triggered.connect(self.callOpenFile)
        self.renameButton.triggered.connect(self.callRename)
        self.deleteButton.triggered.connect(self.callDelete)
        self.fileTypeButton.triggered.connect(self.callFileTypeInfo)
        self.bookmarkButton.triggered.connect(self.callAddToBookmarks)
        self.bookmarkListButton.triggered.connect(self.callListBookmarks)
        
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.rightClickMenu)
        
        self.treeView_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView_2.customContextMenuRequested.connect(self.rightClickMenu)
        
        self.filterTxtLine.textChanged.connect(self.setFilter)
        
    
    def setFilter(self):
        self.filter = unicode( self.filterTxtLine.text() )
        self.doShowDir(self.activeTreeview)
        
    def changeActiveTreeview(self, i):
        self.activeTreeview = i
        print "active treeview is now " + str(i)
        if i==0:
            self.currentDir = self.currentDirTxtLine.text()
            self.currentDirTxtLine2.setStyleSheet("QLineEdit { background-color : #ccc; color : #999; }")
            self.currentDirTxtLine.setStyleSheet("")
        elif i==1:
            self.currentDir = self.currentDirTxtLine2.text()
            self.currentDirTxtLine.setStyleSheet("QLineEdit { background-color : #ccc; color : #999; }")
            self.currentDirTxtLine2.setStyleSheet("")
            
    def rightClickMenu(self, pos):
        print "right clicked"
        
        menu = QtGui.QMenu()
        actionsList = OrderedDict((('Open', 'callOpenFile'), ('Rename', 'callRename'), ('Copy', 'copyFile'), ('Cut' , 'cutFile'), ('Paste', 'pasteFile'), ('Delete', 'callDelete'), ('File Type Info', 'callFileTypeInfo'), ('Add to Bookmarks', 'callAddToBookmarks'), ('Add to Tag', 'callAddToTag'), ('Properties', 'callProperties')))
        actions = []
        actionFunctions = []
        
        for k,v in actionsList.iteritems():
            actions.append(menu.addAction(k))
            actionFunctions.append(v)
        
        action = menu.exec_(self.treeViews[self.activeTreeview].mapToGlobal(pos))
        
        for i in range(0, len(actions)):
            if action == actions[i]:
                getattr(self, actionFunctions[i])()
                
                
    def copyFile(self):
        self.copyCutFile = ['copy', self.currentDir + "/" + self.clickedFileOrDir]
        print self.clickedFileOrDir + " file set to be copied"
    
    def cutFile(self):
        self.copyCutFile = ['cut', self.currentDir + "/" + self.clickedFileOrDir]
        print self.clickedFileOrDir + " file set to be cut"
        
    def pasteFile(self):
        import copyCutPaste
        if self.activeTreeview == 0:
            p = unicode(self.currentDirTxtLine.text())
        elif self.activeTreeview == 1:
            p = unicode(self.currentDirTxtLine2.text())
        copyCutPaste.copyCutPaste(self.copyCutFile[0], self.copyCutFile[1], p)
    
    def callFileTypeInfo(self):
        import fileTypeInfo
        fileTypeInfo.fileTypeInfo(self.clickedFileOrDir)
        
    def callAddToBookmarks(self):
        import addToBookmarks
        addToBookmarks.addToBookmarks(self.currentDir + "/" + self.clickedFileOrDir)
        
    def callListBookmarks(self):
        import showBookmarksList
        showBookmarksList.showBookmarksList(self.currentDir + "/" + self.clickedFileOrDir)
    
    def callDelete(self):
        import deleteFileDir
        deleteFileDir.deleteFileDir(self.currentDir + "/" + self.clickedFileOrDir)
        
    def callRename(self):
        import renameFileDir
        renameFileDir.renameFileDir(self.currentDir + "/" + self.clickedFileOrDir)

    def callOpenFile(self):
        print "to open"
        import openFile
        from os.path import isfile
        toOpenFile = self.clickedFile
        if(isfile(toOpenFile)):
            openFile.openFile(toOpenFile)
    
    def callAddTotag(self):
        return
    
    def callProperties(self):
        import properties
        properties.properties(self.currentDir + "/" + self.clickedFileOrDir)
        
    def callNewFile(self):
        import newFile
        newFile.newFile(self.currentDir)
    
    def callNewDir(self):
        import newDir
        newDir.newDir(self.currentDir)
    
    def callShowDir(self):
        import showDir
        if self.activeTreeview==0:
            self.currentDir = showDir.showDir(self.currentDirTxtLine.text())
        elif self.activeTreeview==1:
            self.currentDir = showDir.showDir(self.currentDirTxtLine2.text())
    
    def showParentDir(self):
        self.clickedFileOrDir = ""
        parentDir = str(self.currentDir).rsplit('/',1)[0]
        if(isdir(parentDir)):
            self.roots[self.activeTreeview] = self.fileSystemModels[self.activeTreeview].setRootPath(parentDir)
            self.treeViews[self.activeTreeview].setModel(self.fileSystemModels[self.activeTreeview])
            self.treeViews[self.activeTreeview].setRootIndex(self.roots[self.activeTreeview])
            self.currentDir = parentDir
            if self.activeTreeview==0:
                self.currentDirTxtLine.setText(self.currentDir)
            elif self.activeTreeview==1:
                self.currentDirTxtLine2.setText(self.currentDir)
        else:
            print parentDir + " is not a directory"
        
    def doShowDir(self, tv):
        self.activeTreeview = tv
        if self.activeTreeview==0:
            newDir = self.currentDirTxtLine.text()
        elif self.activeTreeview==1:
            newDir = self.currentDirTxtLine2.text()
            
        self.clickedFileOrDir = ""
        
        if(isdir(newDir)):
            
            self.fileSystemModels[self.activeTreeview].setNameFilters([self.filter+"*"])  
            self.fileSystemModels[self.activeTreeview].setNameFilterDisables(False)

            self.roots[self.activeTreeview] = self.fileSystemModels[self.activeTreeview].setRootPath(newDir)
            self.treeViews[self.activeTreeview].setModel(self.fileSystemModels[self.activeTreeview])
            self.treeViews[self.activeTreeview].setRootIndex(self.roots[self.activeTreeview])
            self.currentDir = newDir
            
            self.changeActiveTreeview(tv)
            
        else:
            print newDir + " is not a directory"
    
    def treeviewClicked(self, index):
        print "> " + self.fileSystemModels[self.activeTreeview].filePath(index)
        newPath = unicode(self.fileSystemModels[self.activeTreeview].filePath(index))
        print "new path is " + newPath
        if isdir(newPath):
            self.currentDir = newPath
            if self.activeTreeview==0:
                self.currentDirTxtLine.setText(self.currentDir)
            elif self.activeTreeview==1:
                self.currentDirTxtLine2.setText(self.currentDir)
            self.doShowDir(self.activeTreeview)
        elif isfile(newPath):
            self.clickedFile = newPath
            self.callOpenFile()
            
    def homeTreeviewClicked(self, index):
        
        newPath = unicode(self.fileSystemModel3.filePath(index))
        print "new path is set to" + newPath + " by home treeview"
        self.currentDir = newPath
        if self.activeTreeview==0:
            self.currentDirTxtLine.setText(self.currentDir)
        elif self.activeTreeview==1:
            self.currentDirTxtLine2.setText(self.currentDir)
        self.doShowDir(self.activeTreeview)
    
    def changeclickedFileOrDir(self, index):
        self.clickedFileOrDir = unicode(self.fileSystemModels[self.activeTreeview].filePath(index)).rsplit('/')[-1]
        from genericpath import isfile
        if isfile(self.currentDir + "/" + self.clickedFileOrDir):
            self.clickedFile = self.currentDir + "/" + self.clickedFileOrDir
        elif isdir(self.clickedFileOrDir):
            self.currentDir = self.clickedFileOrDir
        print self.clickedFileOrDir + " is clicked"
        
        from preview import preview
        preImg = preview()
        if preImg.showPreview(self.currentDir + "/" + self.clickedFileOrDir):
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(self.currentDir + "/" + self.clickedFileOrDir)))
            self.imageLabel.setVisible(True)
            self.scrollArea.setVisible(True)
        else:
            self.imageLabel.setVisible(False)
            self.scrollArea.setVisible(False)
        
            
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    hwl1 = WindowSource()
    hwl1.main()
    sys.exit(app.exec_())