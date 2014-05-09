'''
Created on May 9, 2014
@author: yusuf
'''
from PyQt4 import QtGui
from modules import delete
import Main
from genericpath import isdir, isfile

class deleteFileDir(Main.WindowSource):
    currentName = ''
    
    def deleteFile(self):
        if self.deleteDialog():
            if delete.deleteFile(self.currentName):
                print "'" + self.currentName + "' file is deleted"
            else:
                print "'" + self.currentName + "' file couldn't be deleted"
    
    def deleteDir(self):
        if self.deleteDialog():
            if delete.deleteDir(self.currentName):
                print "'" + self.currentName + "' directory is deleted with all its contents"
            else:
                print "'" + self.currentName + "' directory couldn't be deleted"              
            
    def deleteDialog(self):
        
        if isfile(self.currentName):
            confirmText = "Are you sure to delete the file '" + self.currentName + "'?"
        elif isdir(self.currentDir):
            confirmText = "Are you sure to delete '" + self.currentName + "' directory and all its contents?"
        
        reply = QtGui.QMessageBox.question(self, 'delete', confirmText , QtGui.QMessageBox.Yes |  QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            print "deletion is confirmed"
            return True
        else:
            print "deletion is rejected"
            return False
    
    def __init__(self, currentName):
        super(deleteFileDir, self).__init__(None)
        self.currentName = currentName
        
        if isdir(currentName):
            self.deleteDir()
        elif isfile(currentName):
            self.deleteFile()
        
