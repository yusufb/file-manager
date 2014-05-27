'''
Created on May 13, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
import Main
from modules import bookmark
from ui import bookmarkUI
from src import Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class addToBookmarks(Main.WindowSource, bookmarkUI.Ui_Form):

    infoFile = "../resources/data/bookmarks.json"
    fullPath = ""
    bookmarkName = ''
    
    def closeDialog(self):
        self.dialog.close()
        
    def add(self):
        #bookmark.readBookmarks(self.infoFile)
        #bookmark.showAllBookmarks(self.infoFile)
        name = unicode(self.dialog.ui.name.text())
        fullPath = unicode(self.dialog.ui.path.text())
        bookmark.addToBookmarks(self.infoFile, fullPath, name)
        self.closeDialog()
        
    def showBookmarkDialog(self):
        self.dialog = QtGui.QDialog()
        
        self.dialog.ui = bookmarkUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        
        self.dialog.ui.path.setText(self.fullPath)
        self.dialog.ui.name.setText(Utils.stripExtension( Utils.getFileNameFromFullPath(unicode(self.fullPath)) ) )
       
        self.dialog.ui.addButton.clicked.connect(self.add)
        self.dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
        
    def __init__(self, fullPath):
        super(addToBookmarks, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmarkDialog()

