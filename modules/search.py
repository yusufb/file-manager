'''
Created on Dec 23, 2013
@author: yusuf
'''

def search(fileName, search_type='a', search_dir='.', exact=True):
    from os import listdir
    from os.path import isfile, join
    from genericpath import isdir

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