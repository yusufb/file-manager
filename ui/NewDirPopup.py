from PyQt4 import QtCore,QtGui
from src import Main
'''
Created on Apr 6, 2014
@author: yusuf
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

class NewDirPop:
    def newDirNameDialog(self, WindowSource):
            
        text, ok = QtGui.QInputDialog.getText(WindowSource, 'new dir', 'Enter dir name:')
            
        if ok:
            WindowSource.newDirName = str(text)
            print "new dir name is set to '" + WindowSource.newDirName + "'"