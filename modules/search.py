'''
Created on Dec 23, 2013
@author: yusuf
'''

import os   
from os import listdir
from os.path import isfile, join
from genericpath import isdir
from fileinput import filename
    
def search(fileName, search_type='a', search_dir='.', exact=True):


    if exact:
        if search_type == 'f':
            files = [f for f in listdir(search_dir) if isfile(join(search_dir, f)) and f == fileName]
        
        elif search_type == 'd':
            files = [f for f in listdir(search_dir) if isdir(join(search_dir, f)) and f == fileName]
            
        else:
            files = [f for f in listdir(search_dir) if f == fileName]
        
    
    else:
        if search_type == 'f':
            files = [f for f in listdir(search_dir) if isfile(join(search_dir, f)) and fileName in f]
            
        elif search_type == 'd':
            files = [f for f in listdir(search_dir) if isdir(join(search_dir, f)) and fileName in f]
        
        else:
            files = [f for f in listdir(search_dir) if fileName in f]
    
    withFileType = []
    
    for fd in files:
        if isfile(join(search_dir,fd)):
            withFileType.append(("f", fd))
        elif isdir(join(search_dir,fd)):
            withFileType.append(("d", fd))
    
    return withFileType

def recursiveSearch(fileName, search_type='a', search_dir='.', exact=True):
    
    matches = []
    fileName = fileName.lower()
    
    for root, dirnames, filenames in os.walk(search_dir):
        
        if exact:
            if search_type == "f" or search_type == "a":
                for filename in filenames:
                    if filename.lower() == fileName:
                            matches.append(os.path.join(root, filename))
            if search_type == "d" or search_type == "a":
                for dirname in dirnames:
                    if dirname.lower() == fileName:
                            matches.append(os.path.join(root, dirname))
        else:
            if search_type == "f" or search_type == "a":
                for filename in filenames:
                    if fileName in filename.lower():
                            matches.append(os.path.join(root, filename))
            if search_type == "d" or search_type == "a":
                for dirname in dirnames:
                    if fileName in dirname.lower():
                            matches.append(os.path.join(root, dirname))           
            
    return matches

print recursiveSearch("test", "f", "/", False)