'''
Created on Apr 8, 2014
@author: yusuf
'''
from PyQt4 import QtCore,QtGui
from ui import *
from modules import create
import Main

class newDir(Main.WindowSource):
    newDirName = "new dir"
    currentDir = "."
    
    def newDirFunc(self):
        self.newDirNameDialog()
        
        if create.createDir(str(self.newDirName), str(self.currentDir) ):
            print "new dir is created: '" + self.newDirName + "'"
        else:
            print "new dir can not be created"
        
    def newDirNameDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'new dir', 'Enter dir name:')
        
        if ok:
            self.newDirName = str(text)
            print "new dir name is set to '" + self.newDirName + "'"
            
    def __init__(self, currentDir):
        super(newDir, self).__init__(None)
        self.currentDir = currentDir
        self.newDirFunc()
