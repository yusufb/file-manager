'''
Created on Dec 24, 2013
@author: yusuf
'''

def createDir(dirName="new", currentDir="."):
    import os
    os.chdir(currentDir)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        return True
    else:
        return False
    
def createFile(fileName="new"):
    import os
    with open(fileName, 'a'):
        os.utime(fileName, None)
        return True