'''
Created on May 13, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
import Main
from modules import bookmark
from ui import bookmarkUI


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class addToBookmarks(Main.WindowSource, bookmarkUI.Ui_Form):

    infoFile = "../resources/data/bookmarks.json"
    fullPath = ""
    
    def testFunction(self):
        print 'enter action'
        
    def closeDialog(self):
        self.dialog.close()
        
    def add(self):
        #bookmark.readBookmarks(self.infoFile)
        #bookmark.showAllBookmarks(self.infoFile)
        bookmark.addToBookmarks(self.infoFile, str(self.fullPath), 'utku')
        
    def showBookmarkDialog(self):
        dialog = QtGui.QDialog()
        self.dialog = dialog
        dialog.ui = bookmarkUI.Ui_Form()
        dialog.ui.setupUi(dialog)
        
        #passing parameter
        dialog.ui.path.setText(self.fullPath)
        #calling function
        dialog.ui.addButton.clicked.connect(self.testFunction)
        dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        
        
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
        
        
    def __init__(self, fullPath):
        super(addToBookmarks, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmarkDialog()

