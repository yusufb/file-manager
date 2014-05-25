'''
Created on Dec 25, 2013
@author: yusuf
'''
def move(filename, dest):
    import shutil, errno
    try:
        shutil.move(filename, dest)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.move(filename, dest)
        else: raise