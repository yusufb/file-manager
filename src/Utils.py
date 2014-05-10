'''
Created on May 6, 2014
@author: yusuf
'''
import platform

def getParentDir(currentDir):
    return currentDir.rsplit('/',1)[0]

def getOsName():
    return str(platform.system())
        