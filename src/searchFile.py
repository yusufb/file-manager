'''
Created on Jun 3, 2014
@author: yusuf
'''
import Main
from PyQt4 import QtCore,QtGui,Qt
from modules import search
from src import Utils
from ui import searchUI, searchListUI

class searchFile(Main.WindowSource):
    newFileName = ""
    searchResults = []
    
    def search(self):
        self.dialog.close()
        searchDir = unicode(self.dialog.ui.lineEdit_2.text() )
        searchName = unicode(self.dialog.ui.lineEdit.text() )
        isExact = self.dialog.ui.checkBox_3.isChecked()
        type = "a"
        
        if self.dialog.ui.checkBox.isChecked() and self.dialog.ui.checkBox_2.isChecked():
            type = "a"
        else:
            if self.dialog.ui.checkBox.isChecked() :
                type = "f"
            if self.dialog.ui.checkBox_2.isChecked():
                type = "d"
                
        print "search parameters: " + searchName + " " + type + " " + searchDir + " " + str(isExact)
        print search.recursiveSearch(searchName, type, searchDir, isExact)
        self.searchResults = search.recursiveSearch(searchName, type, searchDir, isExact)
    
        self.showResults()
    
    def searchDialog(self):
        self.dialog = QtGui.QDialog()
        self.dialog.ui = searchUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.lineEdit_2.setText(self.searchDir)
        self.dialog.ui.pushButton_2.clicked.connect(self.closeDialog)
        self.dialog.ui.pushButton.clicked.connect(self.search)

        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
    def showResults(self):
        
        self.dialog = QtGui.QDialog()
        self.dialog.ui = searchListUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        #self.dialog.ui.removeButton.clicked.connect(self.deleteFromBookmarkList)
        
        self.dialog.ui.searchList.setColumnCount(2)
        self.labels = Qt.QStringList()
        self.labels.append("Name")
        self.labels.append("Path")
        self.dialog.ui.searchList.setHorizontalHeaderLabels(self.labels)
        self.listName = Qt.QStringList()
        self.listPath = Qt.QStringList()
        
        index = 0
        for path in self.searchResults:
            name = Utils.getFileNameFromFullPath(path)
            
            self.listName.append(Qt.QString(unicode(name)))
            self.listPath.append(Qt.QString(unicode(path)))
            self.name =  QtGui.QTableWidgetItem(self.listName[index])
            self.name.setToolTip(Qt.QString(unicode(path)))
            self.path =  QtGui.QTableWidgetItem(self.listPath[index])
            self.path.setToolTip(Qt.QString(unicode(path)))
            self.name.setFlags(self.name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.path.setFlags(self.path.flags() & ~QtCore.Qt.ItemIsEditable)
            self.dialog.ui.searchList.insertRow(index)
            self.dialog.ui.searchList.setItem(index, 0, self.name)
            self.dialog.ui.searchList.setItem(index, 1, self.path)
            
            index = index + 1
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
    def closeDialog(self):
        self.dialog.close()

    def __init__(self, searchDir):
        super(searchFile, self).__init__(None)
        self.searchDir = searchDir
        self.searchDialog()

