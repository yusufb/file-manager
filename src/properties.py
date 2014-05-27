'''
Created on May 27, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui,Qt
import Main
from ui import propertiesUI

class properties(Main.WindowSource, propertiesUI.Ui_Form):
    fullPath = ""
    
    def showGeneralProperties(self):
        return
    
    def showPermissionProperties(self):
        return
    
    def showPropertiesDialog(self):
        import os
        self.dialog = QtGui.QDialog()
        self.dialog.ui = propertiesUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.lineEdit.setText(unicode(self.fullPath))
        self.dialog.ui.sizeValueLabel.setText(unicode(os.path.getsize(unicode(self.fullPath))) + ' bytes')
        self.dialog.ui.typeValueLabel.setText('')
        #self.dialog.ui.removeButton.clicked.connect(self.deleteFromBookmarkList)

        #self.showBookmark()
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_() 
        


    def __init__(self, fullPath):
        super(properties, self).__init__(None)
        self.fullPath = fullPath
        self.showPropertiesDialog()


