'''
Created on May 6, 2014
@author: yusuf
'''
import Main, sys, subprocess, os

class openFile(Main.WindowSource):
    toOpenFile = ""
    
    def openFileFunc(self):
        if sys.platform == 'linux2':
            subprocess.call(["xdg-open", self.toOpenFile])
        else:
            os.startfile(self.toOpenFile)
        


    def __init__(self, toOpenFile):
        super(openFile, self).__init__(None)
        self.toOpenFile = toOpenFile
        self.openFileFunc()


