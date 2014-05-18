'''
Created on May 13, 2014
@author: utku
'''

import json, os

def checkBookmarkList(self):
    return False
    
def addToBookmarks(self, jsonfile, path, name):
    print 'girdi'
    with open(jsonfile, 'a') as datafile:
        json.dump(createJSONObject(self, path, name),datafile)
        datafile.write(os.linesep)

def createJSONObject(self, path, name):
    data = {'path':path, 'name':name}
    return data