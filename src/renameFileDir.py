# -*- coding: utf-8 -*-

'''
Created on May 8, 2014
@author: yusuf
'''
from PyQt4 import QtGui
from modules import rename
import Main
from src import Utils

class renameFileDir(Main.WindowSource):
    newFileName = ''
    currentFileName = ''
    
    def renameFunc(self):
        if(self.renameDialog()):
            if rename.rename(unicode(self.currentFileName), Utils.getParentDir(unicode(self.currentFileName)) + "/" + unicode(self.newFileName)):
                print "file name changed from '" + unicode(self.currentFileName) + "' to '" + unicode(self.newFileName) + "'"
            else:
                print "name can not be changed"
        
    def renameDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'new name', 'Enter the new name:',  QtGui.QLineEdit.Normal , Utils.getFileNameFromFullPath(unicode(self.currentFileName)))
        
        if ok:
            print "*" , unicode(text)
            self.newFileName = unicode(text)
            print "file name is set to '" + self.newFileName + "'"
            return True

    def __init__(self, currentName):
        super(renameFileDir, self).__init__(None)
        self.currentFileName = currentName
        self.renameFunc()