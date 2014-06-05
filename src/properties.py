'''
Created on May 27, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui,Qt
import Main
from ui import propertiesUI
from modules import tag
from src import Paths

class properties(Main.WindowSource, propertiesUI.Ui_Form):
    fullPath = ""
    infoFile = Paths.TAGS
    
    def showGeneralProperties(self):
        return
    
    def showPermissionProperties(self):
        return
    
    def showPropertiesDialog(self):
        import os, datetime, stat
        availableTagName = []
        self.dialog = QtGui.QDialog()
        self.dialog.ui = propertiesUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.lineEdit.setText(unicode(self.fullPath))
        self.dialog.ui.lineEdit_2.setText(unicode(self.fullPath))
        self.dialog.ui.sizeValueLabel.setText(unicode(os.path.getsize(unicode(self.fullPath))) + ' bytes')
        self.dialog.ui.createdValueLabel_2.setText(unicode(datetime.datetime.fromtimestamp(int(os.path.getctime(self.fullPath))).strftime('%d-%m-%Y %H:%M:%S')))
        self.dialog.ui.lastmodifValuelabel.setText(unicode(datetime.datetime.fromtimestamp(int(os.path.getmtime(self.fullPath))).strftime('%d-%m-%Y %H:%M:%S')))
        self.dialog.ui.permissionValueLabel.setText(oct(os.stat(self.fullPath)[stat.ST_MODE] & 0777))
        self.tagList = ''
        print self.fullPath
        availableTagName = tag.getAllRecordsByPath(self.infoFile, unicode(self.fullPath))
        print availableTagName
        for value in availableTagName:
            self.tagList += value + ' '
            
        self.dialog.ui.tagLabelValue.setText(self.tagList)   
        '''
            change permission os.chmod(path, octal code)
        '''
        
        
        #self.dialog.ui.removeButton.clicked.connect(self.deleteFromBookmarkList)

        #self.showBookmark()
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_() 
        


    def __init__(self, fullPath):
        super(properties, self).__init__(None)
        self.fullPath = fullPath
        self.showPropertiesDialog()


