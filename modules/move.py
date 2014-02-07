'''
Created on Dec 25, 2013
@author: yusuf
'''
def move(filename, dest):
    import os
    try:
        os.rename(filename, dest + "/" + filename)
        return True
    except OSError as e:
        print('An error has occured during moving:', e.errno, e.strerror)