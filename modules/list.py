'''
Created on Dec 23, 2013
@author: yusuf
'''

#list by: type, name etc.
def listFilesAndDirs(listType='a'):
    
    from os import listdir
    from os.path import isfile, join
    from genericpath import isdir
    
    mypath = "."
    
    files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    directories = [ d for d in listdir(mypath) if isdir(join(mypath,d)) ]
    
    filesWithType = zip(["f"] * len(files), files)
    directoriesWithType = zip(["d"] * len(files), directories)
    
    
    if listType=='f':
        return filesWithType
    
    elif listType == 'd':
        return directoriesWithType
        
    else:
        return directoriesWithType + filesWithType