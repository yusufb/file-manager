'''
Created on Dec 25, 2013
@author: yusuf
'''
from distutils import dir_util
from os.path import isdir, isfile
from shutil import copy2
from os import mkdir


def copy(src, dst):
    if isdir(src):
        srcDir= src.rsplit('/',1)[1]
        mkdir(srcDir)
        dir_util.copy_tree(src, dst + "/" + srcDir)
    elif isfile(src):
        copy2(src, dst)