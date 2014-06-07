'''
Created on May 13, 2014
@author: utku
'''
import Main
from PyQt4 import QtCore,QtGui
from ui import about

class aboutDialog(Main.WindowSource, about.Ui_Form):

    def __init__(self):
        super(aboutDialog, self).__init__(None)
        self.dialog = QtGui.QDialog()
        self.dialog.ui = about.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        
        #self.dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()


