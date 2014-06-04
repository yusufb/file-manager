'''
Created on Jun 2, 2014
@author: yusuf
'''
import json
from pprint import pprint

class jsonFile():
    data = ""
    
    def jsonToFile(self, data, jsonFile):
        with open(jsonFile, 'w') as f:
            json.dump(data, f)
            return True
            
    def fileToJson(self, jsonFile):
        with open(jsonFile) as data_file:   
            try: 
                data = json.load(data_file)
            except:
                print "couldn't load the json file, creating the new one..."
                with open(jsonFile, 'w') as f:
                    f.write('[]')
                    f.close()
                data = json.load(data_file)
                
        return data
    #pprint data
