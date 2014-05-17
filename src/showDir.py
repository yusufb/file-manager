'''
Created on Apr 8, 2014
@author: utku, yusuf
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
            
            self.roots[self.activeTreeview] = self.fileSystemModels[self.activeTreeview].setRootPath(self.newDir)
            self.treeViews[self.activeTreeview].setModel(self.fileSystemModels[self.activeTreeview])
            self.treeViews[self.activeTreeview].setRootIndex(self.roots[self.activeTreeview])
            
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
        
