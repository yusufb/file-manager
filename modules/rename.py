'''
Created on Dec 23, 2013
@author: yusuf
'''

def rename(old, new):
    import os
    try:
        os.rename(old, new)
        return True
    except OSError as e:
        print('An error has occured during renaming:', e.errno, e.strerror)