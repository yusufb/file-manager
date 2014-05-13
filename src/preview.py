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
    imgExts = ['png','jpg','jpeg','gif','tif','tiff','bmp']
    
    def showPreview(self):
        if self.checkExts():
            self.createImagePane()
        else:
            print 'hayir'
        
    def checkExts(self):
        return Utils.getFileExtension((str(self.fullPath)).lower()) in self.imgExts
    
    def createImagePane(self):
        
        
    def __init__(self, fullPath):
        super(preview, self).__init__(None)
        self.fullPath = fullPath
        self.fileName = Utils.getFileNameFromFullPath(str(fullPath))
        self.showPreview()
        
