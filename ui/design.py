from PyQt4 import QtCore, QtGui
import sys
from PyQt4.Qt import QDir
from os.path import expanduser
#from gi.repository import GLib
from src import Utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("Dialog", "File Manager", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.resize(1366, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        
        self.homeTreeViewLabel = QtGui.QLabel(self.centralwidget)
        self.homeTreeViewLabel.setText("<b>Quick Links</b>")
        self.homeTreeViewLabel.setGeometry(QtCore.QRect(10, 35, 440, 24))
        self.homeTreeViewLabel.setObjectName(_fromUtf8("homeTreeViewLabel"))
        
        self.homeTreeView = QtGui.QListView(self.centralwidget)
        self.homeTreeView.setGeometry(QtCore.QRect(10, 60, 190, 461))
        self.homeTreeView.setObjectName((_fromUtf8("homeTreeView")))
        self.fileSystemModel3 = QtGui.QFileSystemModel(self.homeTreeView)
        self.fileSystemModel3.setReadOnly(True)
        
        self.filterTxtLine = QtGui.QLineEdit(self.centralwidget)
        self.filterTxtLine.setGeometry(QtCore.QRect(10, 530, 190, 24))
        self.filterTxtLine.setObjectName(_fromUtf8("filterTxtLine"))
        self.filterTxtLine.setPlaceholderText("Quick Filter")
        
        
        #desktopDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_DESKTOP)) )
        #downloadsDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_DOWNLOAD)) )
        #documentsDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_DOCUMENTS)) )
        #musicDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_MUSIC)) )
        #picturesDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_PICTURES)) )
        #sharedDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_PUBLIC_SHARE)) )
        #videosDir = Utils.getFileNameFromFullPath( unicode(GLib.get_user_special_dir(GLib.USER_DIRECTORY_VIDEOS)) )
        
        #self.fileSystemModel3.setNameFilters([desktopDir, downloadsDir, documentsDir, musicDir, picturesDir, sharedDir, videosDir])     
        self.fileSystemModel3.setNameFilterDisables(False);
        self.root3 = self.fileSystemModel3.setRootPath(unicode(expanduser("~")))
        self.fileSystemModel3.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        self.homeTreeView.setModel(self.fileSystemModel3)
        self.homeTreeView.setRootIndex(self.root3)
        '''
        self.homeTreeView.hideColumn(1)
        self.homeTreeView.hideColumn(2)
        self.homeTreeView.hideColumn(3)
        '''
        
        self.treeView = QtGui.QListView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(220, 60, 440, 461))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.fileSystemModel = QtGui.QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(True)
        self.root = self.fileSystemModel.setRootPath('.')
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(self.root)
        
        self.treeView_2 = QtGui.QListView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(690, 60, 440, 461))
        self.treeView_2.setObjectName(_fromUtf8("treeView_2"))
        self.fileSystemModel2 = QtGui.QFileSystemModel(self.treeView_2)
        self.fileSystemModel2.setReadOnly(True)
        self.root2 = self.fileSystemModel2.setRootPath('.')
        self.treeView_2.setModel(self.fileSystemModel2)
        self.treeView_2.setRootIndex(self.root2)
        
        '''
        self.showDir = QtGui.QPushButton(self.centralwidget)
        self.showDir.setGeometry(QtCore.QRect(690, 20, 41, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/go-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showDir.setIcon(icon)
        self.showDir.setFlat(False)
        self.showDir.setObjectName(_fromUtf8("showDir"))
        '''
        
        self.currentDirTxtLine = QtGui.QLineEdit(self.centralwidget)
        self.currentDirTxtLine.setGeometry(QtCore.QRect(220, 20, 440, 24))
        self.currentDirTxtLine.setObjectName(_fromUtf8("currentDirTxtLine"))
        
        self.currentDirTxtLine2 = QtGui.QLineEdit(self.centralwidget)
        self.currentDirTxtLine2.setGeometry(QtCore.QRect(690, 20, 440, 24))
        self.currentDirTxtLine2.setObjectName(_fromUtf8("currentDirTxtLine2"))
        self.currentDirTxtLine2.setStyleSheet("QLineEdit { background-color : #ccc; color : #999; }")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.newDirButton = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/new-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newDirButton.setIcon(icon1)
        self.newDirButton.setText("New Directory")
        self.newDirButton.setObjectName(_fromUtf8("newDirButton"))
        
        self.newFileButton = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/new-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFileButton.setIcon(icon2)
        self.newFileButton.setText("New File")
        self.newFileButton.setObjectName(_fromUtf8("newFileButton"))
        
        self.parentDir = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/up-dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.parentDir.setIcon(icon3)
        self.parentDir.setText("Go to Parent")
        self.parentDir.setObjectName(_fromUtf8("parentDir"))
        
        self.openFileButton = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/open-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFileButton.setIcon(icon4)
        self.openFileButton.setText("Open File")
        self.openFileButton.setObjectName(_fromUtf8("openFileButton"))
        
        self.renameButton = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renameButton.setIcon(icon5)
        self.renameButton.setText("Rename")
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        
        self.deleteButton = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon6)
        self.deleteButton.setText("Delete")
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        
        self.fileTypeButton = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/file-type-info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileTypeButton.setIcon(icon7)
        self.fileTypeButton.setText("File Type Info")
        self.fileTypeButton.setObjectName(_fromUtf8("fileTypeButton"))
        
        self.bookmarkButton = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/bookmark_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkButton.setIcon(icon8)
        self.bookmarkButton.setText("Add to Bookmarks")
        self.bookmarkButton.setObjectName(_fromUtf8("bookmarkButton"))
        
        self.bookmarkListButton = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/bookmark-list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkListButton.setIcon(icon9)
        self.bookmarkListButton.setText("List Bookmarks")
        self.bookmarkListButton.setObjectName(_fromUtf8("bookmarkListButton"))
        
        self.ftpConnectionButton = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/ftp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ftpConnectionButton.setIcon(icon10)
        self.ftpConnectionButton.setText("FTP Connection")
        self.ftpConnectionButton.setObjectName(_fromUtf8("ftpConnectionButton"))
        
        self.createTagButton = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/img/bookmark_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createTagButton.setIcon(icon10)
        self.createTagButton.setText("Create Tag")
        self.createTagButton.setObjectName(_fromUtf8("createTagButton"))
        
     
        self.toolBar.addAction(self.newDirButton)
        self.toolBar.addAction(self.newFileButton)
        self.toolBar.addAction(self.parentDir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.openFileButton)
        self.toolBar.addAction(self.renameButton)
        self.toolBar.addAction(self.deleteButton)
        self.toolBar.addAction(self.fileTypeButton)
        self.toolBar.addAction(self.bookmarkButton)
        self.toolBar.addAction(self.bookmarkListButton)
        self.toolBar.addAction(self.ftpConnectionButton)
        self.toolBar.addAction(self.createTagButton)
        
        
        ######################
        previewFileName = "../resources/img/blank.png"
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        image = QtGui.QImage(previewFileName)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        self.imageLabel.adjustSize()
        self.imageLabel.resize(150, 150*self.imageLabel.height()/self.imageLabel.width())
        
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setGeometry(QtCore.QRect(1150, 220, 152, 150*self.imageLabel.height()/self.imageLabel.width()+2))
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setVisible(False)
        
        MainWindow.setCentralWidget(self.centralwidget)
        ##########################
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
    Dialog.show()
#     Dialog.showMaximized()
    Dialog.setFixedHeight(Dialog.height())
    Dialog.setFixedWidth(Dialog.width())
    print "dialog ui is created"
    
    sys.exit(app.exec_())

