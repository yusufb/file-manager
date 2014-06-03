'''
Created on May 31, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui
import Main
from modules import tag
from src import Paths
from ui import createTagUI

class createTag(Main.WindowSource, createTagUI.Ui_Form):
    fullPath = ""
    infoFile = Paths.TAGS
    
    def closeDialog(self):
        self.dialog.close()
        
    def add(self):
        if tag.createTag2(self.infoFile, '', unicode(self.dialog.ui.name.text()), str(self.dialog.ui.comboBox.currentText()).lower()):#create.createFile(self.currentDir + "/" + self.newFileName):
            print "new tag is created: '" + unicode(self.dialog.ui.name.text()) + "'"
        else:
            print "new tag can not be created"
                
        self.dialog.close()
    
    def showNewTagDialog(self):
        self.dialog = QtGui.QDialog()
        
        self.dialog.ui = createTagUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.addButton.clicked.connect(self.add)
        self.dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()


    def __init__(self, fullPath):
        super(createTag, self).__init__(None)
        self.fullPath = fullPath
        self.showNewTagDialog()


