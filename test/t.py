'''
Created on Apr 7, 2014
@author: yusuf
'''
from PyQt4 import QtGui
import sys

def main():
    
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("Main Window")
    w.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    print "selam"
    main()