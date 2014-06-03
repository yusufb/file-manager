'''
Created on May 20, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui,Qt
import Main
from genericpath import isdir, isfile
from modules import bookmark
from ui import bookmarkListUI
from src import Paths
from src import jsonFile

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class showBookmarksList(Main.WindowSource, bookmarkListUI.Ui_Form):
    
    infoFile = Paths.BOOKMARKS
    fullPath = ""
    clickedPath = ""
    newBookmarkPath = ""
    
    def showBookmark(self):
        bookmarkList =  bookmark.showAllBookmarks(self.infoFile)
        
        j = jsonFile.jsonFile()
        readFromFile = j.fileToJson(self.infoFile)
        
        self.dialog.ui.bookmarks.setColumnCount(2)
        self.labels = Qt.QStringList()
        self.labels.append("Name")
        self.labels.append("Path")
        self.dialog.ui.bookmarks.setHorizontalHeaderLabels(self.labels)
        self.listName = Qt.QStringList()
        self.listPath = Qt.QStringList()
        
        index = 0
        for values in readFromFile:
            
            self.listName.append(Qt.QString(unicode(values['name'])))
            self.listPath.append(Qt.QString(unicode(values['path'])))
            self.name =  QtGui.QTableWidgetItem(self.listName[index])
            self.name.setToolTip(Qt.QString(unicode(values['path'])))
            self.path =  QtGui.QTableWidgetItem(self.listPath[index])
            self.path.setToolTip(Qt.QString(unicode(values['path'])))
            self.name.setFlags(self.name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.path.setFlags(self.path.flags() & ~QtCore.Qt.ItemIsEditable)
            self.dialog.ui.bookmarks.insertRow(index)
            self.dialog.ui.bookmarks.setItem(index, 0, self.name) ## satir, sutuun
            self.dialog.ui.bookmarks.setItem(index, 1, self.path) ## satir, sutuun
            
            index = index + 1
            
            
        '''
        for index, values in enumerate(bookmarkList):
            self.listName.append(Qt.QString(unicode(values['name'])))
            self.listPath.append(Qt.QString(unicode(values['path'])))
            self.name =  QtGui.QTableWidgetItem(self.listName[index])
            self.name.setToolTip(Qt.QString(unicode(values['path'])))
            self.path =  QtGui.QTableWidgetItem(self.listPath[index])
            self.path.setToolTip(Qt.QString(unicode(values['path'])))
            self.name.setFlags(self.name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.path.setFlags(self.path.flags() & ~QtCore.Qt.ItemIsEditable)
            self.dialog.ui.bookmarks.insertRow(index)
            self.dialog.ui.bookmarks.setItem(index, 0, self.name) ## satir, sutuun
            self.dialog.ui.bookmarks.setItem(index, 1, self.path) ## satir, sutuun
        '''
            
        
        QtCore.QObject.connect(self.dialog.ui.bookmarks, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTableWidgetItem*)")), self.directToDir)
        QtCore.QObject.connect(self.dialog.ui.bookmarks, QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")), self.setClickedPath)
    
    def setClickedPath(self, index):
        self.clickedPath = unicode(index.toolTip())
    
    def directToDir(self, index):
        newPath = unicode(index.toolTip())
        if isdir(newPath):
            self.newBookmarkPath = newPath
            
        elif isfile(newPath):
            self.clickedFile = newPath
            self.callOpenFile()
            
        self.dialog.close()
        
    
    def showBookmarkListDialog(self):
        self.dialog = QtGui.QDialog()
        self.dialog.ui = bookmarkListUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.removeButton.clicked.connect(self.deleteFromBookmarkList)

        self.showBookmark()
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
    def deleteFromBookmarkList(self, index):
        if self.clickedPath:
            j = jsonFile.jsonFile()
            newList = []
            readFromFile = j.fileToJson(self.infoFile)
            
            i = 0
            for values in readFromFile:
                if unicode(values['path']) != self.clickedPath:
                    newList.append(dict({'path' : values['path'], 'name' : values['name']}))
                    #self.dialog.ui.bookmarks.removeRow(i)
                i = i + 1
                
            if j.jsonToFile(newList, self.infoFile):
                print "bookmark file is updated"
                self.dialog.close()
                
            

    def __init__(self, fullPath):
        super(showBookmarksList, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmarkListDialog()


