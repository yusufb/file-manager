'''
Created on May 11, 2014
@author: yusuf
'''
from PyQt4 import QtGui
import Main, Utils
import json
from pprint import pprint

class fileTypeInfo(Main.WindowSource):
    fileName = ""
    infoFile = "../resources/data/file_types.json"
    
    def fileTypeFunc(self):
        
        if Utils.getFileExtension(self.fileName):
            with open(self.infoFile) as data_file:    
                data = json.load(data_file)
            pprint(data)
            
            found = False
            
            for item in data:
                try:
                    if item["ext"] == Utils.getFileExtension(self.fileName).lower():
                        extData = item
                        pprint(extData)
                        found = True
                except:
                    found = False
            
            
            if found:       
                #ext found 
                self.showInfoDialog(extData["ext"], extData["name"], extData["desc"], extData["type"])
                
            else:
                #ext not found
                self.showInfoDialog(-1)
            
        else:
            #no ext
            self.showInfoDialog(False)
      
    def showInfoDialog(self, ext, name="", desc="", type=""):
        
        if not ext:
            ext = "Error!"
            msg = self.fileName +  " has no extension."
            
        elif ext == -1:
            ext = Utils.getFileExtension(self.fileName)
            msg = "'." + Utils.getFileExtension(self.fileName) + "' extension can not be found."
            
        else:
            ext = "." + ext + " file"
            msg = "<B>" + name + "</B> (" + type + ")<BR><BR>"+ desc
        
        QtGui.QMessageBox.about(self,  ext , msg)


    def __init__(self, fileName):
        super(fileTypeInfo, self).__init__(None)
        self.fileName = fileName
        self.fileTypeFunc()