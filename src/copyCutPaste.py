'''
Created on May 25, 2014
@author: yusuf
'''

import Main

class copyCutPaste(Main.WindowSource):
    path = ""
    
    def doOp(self, op):
        
        print op + " " + self.path
        


    def __init__(self, path, op):
        super(copyCutPaste, self).__init__(None)
        self.path = path
        self.doOp(op)
