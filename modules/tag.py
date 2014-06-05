'''
Created on May 31, 2014
@author: utku
'''

import json
from src import jsonFile
from json.decoder import JSONObject


def createTag2(jsonFilePath, path, tagName, color):
    
    j = jsonFile.jsonFile()
    toAdd = {'name' : tagName, 'path' : path, 'color' : color}
    readFromFile = j.fileToJson(jsonFilePath)
    tagHasThesePaths = []
    for index in range(len(readFromFile)):
        if(readFromFile[index]['name'] == tagName):
            tagHasThesePaths.append(readFromFile[index]['path'])
    #pprint(readFromFile)
    
    if path in tagHasThesePaths:
        print 'already this path signed this tag'
        return
    
    toWriteList = []
    toWriteList.extend(readFromFile)
    toWriteList.append(dict(toAdd))
    
    if j.jsonToFile(toWriteList, jsonFilePath):
        print 'tag has created'



def printTagsName(jsonFilePath):
    j = jsonFile.jsonFile()
    readFromFile = j.fileToJson(jsonFilePath)
    availableTags = []
    for index in range(len(readFromFile)):
        availableTags.append(readFromFile[index]['name'])
    return availableTags

def showAllTags(jsonFilePath, tagName):
    j = jsonFile.jsonFile()
    readFromFile = j.fileToJson(jsonFilePath)
    allTagsPaths = []
    for index in range(len(readFromFile)):
        if readFromFile[index]['name'] == tagName and len(readFromFile[index]['path'])>0:
            allTagsPaths.append(readFromFile[index]['path'])
    return allTagsPaths


def getAllRecordsByPath(jsonFilePath, path):
    j = jsonFile.jsonFile()
    readFromFile = j.fileToJson(jsonFilePath)
    availableTagName = []
    for index in range(len(readFromFile)):
        if readFromFile[index]['path'] == path:
            availableTagName.append(readFromFile[index]['name'])
    return availableTagName




'''def getAllRecordsByTagName(jsonFile, name):
    availablePaths = []
    jsonObjj = readTags(jsonFile)
    for index in range(len(jsonObjj)):
        if jsonObjj[index]['name'] == name:
            availablePaths.append(jsonObjj[index]['path'])
    return availablePaths





def createTag(jsonFile, path, tagName, color):
    if(checkTagList(path, tagName, jsonFile)):
        print 'already this tag sign this file'
        return False
    else:
        with open(jsonFile, 'a') as datafile:
            json.dump(createJSONObject(path, tagName, color), datafile)
            print 'added to tags or created tag'
        return True

def createJSONObject(path, name, color):
    data = {'path':path, 'name':name, 'color':color}
    return data

def readTags(jsonFile):
    plainJSONString = open(jsonFile).read();
    plainJSONString = plainJSONString.replace('}{', '},{')
    jsonList = '[%s]' % (plainJSONString)
    jsonObj = json.loads(jsonList)
    return jsonObj


def checkTagList(path, name, filePath):
    return path in getAllRecordsByTagName(filePath, name)
'''