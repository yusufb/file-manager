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

class addToBookmarks(Main.WindowSource):

    infoFile = "../resources/data/bookmarks.json"
    fullPath = ""
    
    def add(self):
        #bookmark.readBookmarks(self.infoFile)
        #bookmark.showAllBookmarks(self.infoFile)
        bookmark.addToBookmarks(self.infoFile, str(self.fullPath), 'utku')
        
    def showBookmarkDialog(self):
        dialog = QtGui.QDialog()
        dialog.ui = bookmarkUI.Ui_Form()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
        
    def __init__(self, fullPath):
        super(addToBookmarks, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmarkDialog()


