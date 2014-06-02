'''
Created on May 13, 2014
@author: utku
'''

import json
import pprint
from src import jsonFile

def addToBookmarks2(jsonfile, path, name):
    
    # ! check bookmark
    
    j = jsonFile.jsonFile()
    toAdd = {'path' : unicode(path), 'name' : unicode(path)}
    readFromFile = j.fileToJson(jsonfile)
    pprint(readFromFile)
    toWriteList = []
    toWriteList.append(readFromFile)
    toWrite = toWriteList.append(toAdd)
    if j.jsonToFile(toWrite, jsonfile):
        print 'added to bookmarks'

def checkBookmarkList(path, filePath):
    return path in getAllPaths(filePath)
    
def addToBookmarks(jsonfile, path, name):
    if checkBookmarkList(path, jsonfile):
        print 'already in bookmarks'
    else:
        with open(jsonfile, 'a') as datafile:
            json.dump(createJSONObject(jsonfile, path, name), datafile)
            print 'added to bookmarks'

def createJSONObject(jsonfile, path, name):
    data = {'id':idGenerator(jsonfile), 'path':str(path), 'name':name}
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
    allBookmarks = []
    for index in range(len(jsonObjj)):
        allBookmarks.append(jsonObjj[index])
    return allBookmarks
    
def idGenerator(jsonFile):
    jsonObjj = readBookmarks(jsonFile)
    if jsonObjj != []:
        return jsonObjj[len(jsonObjj)-1]['id'] + 1
    else:
        return 0
