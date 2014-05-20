'''
Created on May 20, 2014
@author: utku
'''
import Main
from PyQt4 import QtCore,QtGui
from modules import bookmark
from ui import bookmarkListUI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class showBookmarksList(Main.WindowSource):
    
    infoFile = "../resources/data/bookmarks.json"
    fullPath = ""
    
    def showBookmark(self):
        #bookmark.showAllBookmarks(self.infoFile)
        return
    
    def showBookmarkListDialog(self):
        #UI gelecek
        return  

    def __init__(self, fullPath):
        super(showBookmarksList, self).__init__(None)
        self.fullPath = fullPath
        self.showBookmark()


