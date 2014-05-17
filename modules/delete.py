'''
Created on Dec 25, 2013
@author: yusuf
'''

def deleteFile(filename):
    import os
    try:
        os.remove(str(filename))
        return True
    except IOError as e:
        print('An error has occured during deleting file:', e.errno, e.strerror)
    

def deleteDir(dirname):
    import shutil
    try:
        shutil.rmtree(str(dirname))
        return True
    except IOError as e:
        print('An error has occured during deleting directory:', e.errno, e.strerror)