'''
Created on Dec 25, 2013
@author: yusuf
'''
def copy(filename, dest):
    import shutil
    try:
        shutil.copy2(filename, dest)
    except IOError as e:
        print('An error has occured during copying:', e.errno, e.strerror)