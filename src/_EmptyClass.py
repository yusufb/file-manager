'''
Created on May 13, 2014
@author: yusuf
'''
import Main

class className(Main.WindowSource):
    classVar = ""
    
    def classFunc(self):
        return
        


    def __init__(self, classVar):
        super(className, self).__init__(None)
        self.classVar = classVar
        self.classFunc()


