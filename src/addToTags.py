'''
Created on May 31, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
import Main
from modules import tag
from src import Paths
from ui import tagUI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class addToTags(Main.WindowSource, tagUI.Ui_Form):
    fullPath = ""
    infoFile = Paths.TAGS
    availableTags = []
    
    def closeDialog(self):
        self.dialog.close()
        
    def addToTags(self):
        if tag.createTag(self.infoFile, unicode(self.dialog.ui.path.text()), unicode(self.dialog.ui.comboBox.currentText()), ''):#create.createFile(self.currentDir + "/" + self.newFileName):
            print "the file add to : '" + unicode(self.dialog.ui.comboBox.currentText()) + "' tag" 
        else:
            print "the file can not be added"
                
        print tag.printTagsName(self.infoFile)
        self.dialog.close()
        
    def showAddToTagDialog(self):
        self.dialog = QtGui.QDialog()
        self.availableTags = tag.printTagsName(self.infoFile)
        self.dialog.ui = tagUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.path.setText(self.fullPath)
        
        for tags in self.availableTags:
            self.dialog.ui.comboBox.addItem(_fromUtf8(tags))
            
        self.dialog.ui.addButton.clicked.connect(self.addToTags)
        self.dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()


    def __init__(self, fullPath):
        super(addToTags, self).__init__(None)
        self.fullPath = fullPath
        self.showAddToTagDialog()


