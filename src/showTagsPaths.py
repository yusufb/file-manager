'''
Created on May 20, 2014
@author: utku
'''
from PyQt4 import QtCore,QtGui,Qt
import Main
from genericpath import isdir, isfile
from modules import tag
from ui import tagListUI
from src import Paths
from src import jsonFile, Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class showTagsPaths(Main.WindowSource, tagListUI.Ui_Form):
    
    infoFile = Paths.TAGS
    tagName = ""
    clickedPath = ""
    newTagPath = ""
    
    def showTagsPaths(self):
        tagsPathsList =  tag.showAllTags(self.infoFile, self.tagName)
        
        self.dialog.ui.tags.setColumnCount(2)
        self.labels = Qt.QStringList()
        self.labels.append("Name")
        self.labels.append("Path")
        self.dialog.ui.tags.setHorizontalHeaderLabels(self.labels)
        self.listName = Qt.QStringList()
        self.listPath = Qt.QStringList()
        
        index = 0
        for values in tagsPathsList:
            name = Utils.getFileNameFromFullPath(values)
            self.listName.append(Qt.QString(unicode(name)))
            self.listPath.append(Qt.QString(unicode(values)))
            self.name =  QtGui.QTableWidgetItem(self.listName[index])
            self.name.setToolTip(Qt.QString(unicode(values)))
            self.path =  QtGui.QTableWidgetItem(self.listPath[index])
            self.path.setToolTip(Qt.QString(unicode(values)))
            self.name.setFlags(self.name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.path.setFlags(self.path.flags() & ~QtCore.Qt.ItemIsEditable)
            self.dialog.ui.tags.insertRow(index)
            self.dialog.ui.tags.setItem(index, 0, self.name) ## satir, sutuun
            self.dialog.ui.tags.setItem(index, 1, self.path) ## satir, sutuun
            
            index = index + 1
            
            
        '''
        for index, values in enumerate(bookmarkList):
            self.listName.append(Qt.QString(unicode(values['name'])))
            self.listPath.append(Qt.QString(unicode(values['path'])))
            self.name =  QtGui.QTableWidgetItem(self.listName[index])
            self.name.setToolTip(Qt.QString(unicode(values['path'])))
            self.path =  QtGui.QTableWidgetItem(self.listPath[index])
            self.path.setToolTip(Qt.QString(unicode(values['path'])))
            self.name.setFlags(self.name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.path.setFlags(self.path.flags() & ~QtCore.Qt.ItemIsEditable)
            self.dialog.ui.bookmarks.insertRow(index)
            self.dialog.ui.bookmarks.setItem(index, 0, self.name) ## satir, sutuun
            self.dialog.ui.bookmarks.setItem(index, 1, self.path) ## satir, sutuun
        '''
            
        
        QtCore.QObject.connect(self.dialog.ui.tags, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTableWidgetItem*)")), self.directToDir)
        QtCore.QObject.connect(self.dialog.ui.tags, QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")), self.setClickedPath)
    
    def setClickedPath(self, index):
        self.clickedPath = unicode(index.toolTip())
    
    def directToDir(self, index):
        newPath = unicode(index.toolTip())
        if isdir(newPath):
            self.newTagPath = newPath
            self.dialog.close()
            
        elif isfile(newPath):
            self.clickedFile = newPath
            self.callOpenFile()
            
    
    def showTagsPathsListDialog(self):
        self.dialog = QtGui.QDialog()
        self.dialog.ui = tagListUI.Ui_Form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.removeButton.clicked.connect(self.deleteFromTagList)
        self.dialog.ui.deleteThisTag.clicked.connect(self.deleteTag)
        
        self.showTagsPaths()
        
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.exec_()
        
    def deleteFromTagList(self, index):
        if self.clickedPath:
            j = jsonFile.jsonFile()
            newList = []
            readFromFile = j.fileToJson(self.infoFile)
            
            i = 0
            for values in readFromFile:
                if unicode(values['path']) != self.clickedPath:
                    newList.append(dict({'name' : values['name'], 'path' : values['path'], 'color' : values['color']}))
                    #self.dialog.ui.bookmarks.removeRow(i)
                i = i + 1
                
            if j.jsonToFile(newList, self.infoFile):
                print "tags file is updated"
                
    def deleteTag(self):
        '''if self.deleteDialog():
            if delete.deleteFile(self.currentName):
                print "'" + self.currentName + "' file is deleted"
            else:
                print "'" + self.currentName + "' file couldn't be deleted"    '''
        if self.deleteDialog():
            j = jsonFile.jsonFile()
            newList = []
            readFromFile = j.fileToJson(self.infoFile)
            
            i = 0
            for values in readFromFile:
                if unicode(values['name']) != self.tagName:
                    newList.append(dict({'name' : values['name'], 'path' : values['path'], 'color' : values['color']}))
                    #self.dialog.ui.bookmarks.removeRow(i)
                i = i + 1
                
            if j.jsonToFile(newList, self.infoFile):
                print "tags file is updated"
    
    def deleteDialog(self):
        confirmText = "Are you sure to delete this tag?"        
        reply = QtGui.QMessageBox.question(self, 'Delete Tag', confirmText , QtGui.QMessageBox.Yes |  QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            print "deletion is confirmed"
            return True
        else:
            print "deletion is rejected"
            return False
    
    def __init__(self, name):
        super(showTagsPaths, self).__init__(None)
        self.tagName = name
        self.showTagsPathsListDialog()
