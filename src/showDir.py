'''
Created on Apr 8, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
from genericpath import isdir
import Main
from ui import mainWindow

class showDir(Main.WindowSource,QtGui.QDialog,mainWindow.Ui_Dialog):
    newDir = ''
    def showDirFunc(self):
        if(isdir(self.newDir)):
            self.setupUi(self)
            self.root = self.fileSystemModel.setRootPath(self.newDir)
            self.treeView.setModel(self.fileSystemModel)
            self.treeView.setRootIndex(self.root)
            self.setupUi(self)
            print "current dir is now " + self.newDir
            return self.newDir
        else:
            print self.newDir + " is not a directory"
            
    def __init__(self, currentDir):
        super(showDir, self).__init__(None)
        self.newDir = currentDir
        self.setupUi(self)
        self.showDirFunc()
        
