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

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class showBookmarksList(Main.WindowSource, bookmarkListUI.Ui_Form):
    
    infoFile = Paths.BOOKMARKS
    fullPath = ""
    
    def showBookmark(self):
        bookmarkList =  bookmark.showAllBookmarks(self.infoFile)
        
        self.dialog.ui.bookmarks.setColumnCount(2)
        self.labels = Qt.QStringList()
        self.labels.append("Name")
        self.labels.append("Path")
        self.dialog.ui.bookmarks.setHorizontalHeaderLabels(self.labels)
        self.listName = Qt.QStringList()
        self.listPath = Qt.QStringList()
        
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
            
        
        QtCore.QObject.connect(self.dialog.ui.bookmarks, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTableWidgetItem*)")), self.directToDir)
     
    
    def directToDir(self, index):
        self.dialog.close()
        newPath = unicode(index.toolTip())
        print "new path is " + newPath
        print "active " + str(0)
        if isdir(newPath):
            
            if self.activeTreeview == 0:
                print "t0"
                self.currentDirTxtLine.setText(newPath)
            elif self.activeTreeview == 1:
                print "t1"
                self.currentDirTxtLine.setText2(newPath)
            
            print "here"
            
        elif isfile(newPath):
            self.clickedFile = newPath
            self.callOpenFile()
    
    def showBookmarkListDialog(self):
        self.dialog = QtGui.QDialog()
        self.dialog.ui = bookmarkListUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.removeButton.clicked.connect(self.deleteFromBookmarkList)

        self.showBookmark()
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_() 
        
    def deleteFromBookmarkList(self):
        print self.dialog.ui.bookmarks.currentItem().text()

    def __init__(self, fullPath):
        super(showBookmarksList, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmarkListDialog()


