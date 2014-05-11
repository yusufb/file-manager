'''
Created on May 6, 2014
@author: yusuf
'''
import platform

def getParentDir(currentDir):
    return currentDir.rsplit('/',1)[0]

def getFileExtension(fileName):
    ext = fileName.rsplit('.')[-1]
    if len(ext)>0 and len(fileName.rsplit('.',1)[0])>0 and "." in fileName:
        return ext
    else:
        return False
    

def getOsName():
    return str(platform.system())
