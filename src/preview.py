'''
Created on May 13, 2014
@author: utku, yusuf
'''
from PyQt4 import QtCore,QtGui
from ui import design
import Main, Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class preview(Main.WindowSource, design.Ui_Dialog):
    fullPath = ''
    fileName = ''
    imgExts = ['png','jpg','jpeg','gif','tif','tiff','bmp', 'ico']
    
    def showPreview(self, fullPath):
        fileName = Utils.getFileNameFromFullPath(unicode(fullPath))
        if self.checkExts(fileName):
            print "file preview is showed"
            return True
        
    def checkExts(self, fileName):
        return Utils.getFileExtension((fileName).lower()) in self.imgExts
    
        
        
    def __init__(self):
        super(preview, self).__init__(None)
        #self.fullPath = fullPath
        #self.fileName = Utils.getFileNameFromFullPath(str(fullPath))
        #self.showPreview(self.fileName)
        
