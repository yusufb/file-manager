'''
Created on Apr 8, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
from genericpath import isdir
import Main

class showDir(Main.WindowSource):
    newDir = ''
    def showDirFunc(self):
        if(isdir(self.newDir)):
            self.root = self.fileSystemModel.setRootPath(self.newDir)
            self.treeView.setModel(self.fileSystemModel)
            self.treeView.setRootIndex(self.root)
            print "current dir is now " + self.newDir
            return self.newDir
        else:
            print self.newDir + " is not a directory"
            
    def __init__(self, currentDir):
        super(showDir, self).__init__(None)
        self.newDir = currentDir
        self.setupUi(self)
        self.showDirFunc()
        
