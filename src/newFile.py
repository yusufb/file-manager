'''
Created on May 6, 2014
@author: yusuf
'''
from PyQt4 import QtCore,QtGui
from modules import create
import Main

class newFile(Main.WindowSource):
    newFileName = ''
    currentDir = '.'
    
    def newFileFunc(self):
        if(self.newFileNameDialog()):
            print ">",self.currentDir
            if create.createFile(self.currentDir + "/" + self.newFileName):
                print "new file is created: '" + self.newFileName + "'"
            else:
                print "new file can not be created"
        
    def newFileNameDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'new file', 'Enter file name:')
        
        if ok:
            self.newFileName = str(text)
            print "new file name is set to '" + self.newFileName + "'"
            return True

    def __init__(self, currentDir):
        super(newFile, self).__init__(None)
        self.currentDir = currentDir
        self.newFileFunc()