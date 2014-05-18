'''
Created on May 13, 2014
@author: utku
'''
import Main
from modules import bookmark

class addToBookmarks(Main.WindowSource):

    infoFile = "../resources/data/bookmarks.json"
    fullPath = ""
    
    def add(self):
        bookmark.addToBookmarks(self, self.infoFile, str(self.fullPath), 'utku')
        
    def __init__(self, fullPath):
        super(addToBookmarks, self).__init__(None)
        self.fullPath = fullPath
        self.add()


