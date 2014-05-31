'''
Created on May 31, 2014
@author: utku
'''

import json


def createTag(jsonFile, path, tagName, color):
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

def printTagsName(jsonFile):
    availableTags = []
    jsonObjj = readTags(jsonFile)
    for index in range(len(jsonObjj)):
        availableTags.append(jsonObjj[index]['name'])
    return availableTags


