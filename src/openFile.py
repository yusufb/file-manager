'''
Created on May 6, 2014
@author: yusuf
'''
import Main, sys, subprocess, os
from src import Utils

class openFile(Main.WindowSource):
    toOpenFile = ""
    
    def openFileFunc(self):
        if Utils.getOsName().lower() == "linux":
            subprocess.call(["xdg-open", self.toOpenFile])
        elif Utils.getOsName().lower() == "windows":
            os.startfile(self.toOpenFile)
        


    def __init__(self, toOpenFile):
        super(openFile, self).__init__(None)
        self.toOpenFile = toOpenFile
        self.openFileFunc()


