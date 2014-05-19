'''
Created on May 13, 2014
@author: utku
'''

import json, random

def checkBookmarkList(path, filePath):
    return path in getAllPaths(filePath)
    
def addToBookmarks(jsonfile, path, name):
    if checkBookmarkList(path, jsonfile):
        print 'already in bookmarks'
    else:
        with open(jsonfile, 'a') as datafile:
            json.dump(createJSONObject(path, name), datafile)
            print 'added to bookmarks'

def createJSONObject(path, name):
    data = {'id':idGenerator(), 'path':str(path), 'name':name}
    return data

def readBookmarks(jsonFile):
    plainJSONString = open(jsonFile).read();
    plainJSONString = plainJSONString.replace('}{', '},{')
    jsonList = '[%s]'%(plainJSONString)
    jsonObj = json.loads(jsonList)
    return jsonObj

def getAllPaths(jsonFile):
    availablePaths = []
    jsonObjj = readBookmarks(jsonFile)
    for index in range(len(jsonObjj)):
        availablePaths.append(jsonObjj[index]['path'])
    return availablePaths

def showAllBookmarks(jsonFile):
    jsonObjj = readBookmarks(jsonFile)
    for index in range(len(jsonObjj)):
        print jsonObjj[index]['name'] +' - '+ jsonObjj[index]['path']
    
def idGenerator():
    id = random.randint(0,50)
    return id
