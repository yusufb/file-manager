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
            if rename.rename(self.currentFileName, Utils.getParentDir(str(self.currentFileName)) + "/" + self.newFileName):
                print "file name changed from '" + self.currentFileName + "' to '" + self.newFileName + "'"
            else:
                print "name can not be changed"
        
    def renameDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'new name', 'Enter the new name:',  QtGui.QLineEdit.Normal , Utils.getFileNameFromFullPath(str(self.currentFileName)))
        
        if ok:
            self.newFileName = str(text)
            print "file name is set to '" + self.newFileName + "'"
            return True

    def __init__(self, currentName):
        super(renameFileDir, self).__init__(None)
        self.currentFileName = currentName
        self.renameFunc()