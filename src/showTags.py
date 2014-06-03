'''
Created on Jun, 3 2014
@author: yusuf
'''
from src import jsonFile, Paths

class showTags():
    classVar = ""
    
    def getTags(self):
        j = jsonFile.jsonFile()
        readTags = j.fileToJson(Paths.TAGS)
        return readTags


    def __init__(self):
        print "tags class"
        self.getTags()

s = showTags()
