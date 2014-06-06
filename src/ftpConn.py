'''
Created on May 31, 2014
@author: ANIL
'''
import Main
from PyQt4 import QtCore,QtGui
from modules import ftp
from ui import ftpConnWidget
import os
import platform
from modules.ftp import ftpConnection



class ftpConn(Main.WindowSource,ftpConnWidget.Ui_Form):
    path = ""
    host=""
    
    def makeConnection(self):
        self.host=unicode(self.dialog.ui.hostTxt.text())
        password=unicode(self.dialog.ui.passwordTxt.text())
        username=unicode(self.dialog.ui.usernameTxt.text())
        port=unicode(self.dialog.ui.portTxt.text())
        if len(port)<1:
            port=21
        else:
            port=int(port)    
        ftp.ftpConnection(self.host,port, username, password)
        print self.getPath()
        self.closeDialog()
        
    def closeDialog(self):
        self.dialog.close()  
        
    def showFtpConnDialog(self):
        self.dialog = QtGui.QDialog()
        self.dialog.ui = ftpConnWidget.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        
        self.dialog.ui.connectButton.clicked.connect(self.makeConnection)
        self.dialog.ui.cancelButton.clicked.connect(self.closeDialog)
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
    def getPath(self):
        if platform.system()=='Windows':
            self.path=""
        else:    
            self.path="/run/user/" + str(os.getuid()) + "/gvfs/ftp:host=" + self.host
        return self.path

    def __init__(self):
        super(ftpConn, self).__init__(None)
        
        self.showFtpConnDialog()
        



