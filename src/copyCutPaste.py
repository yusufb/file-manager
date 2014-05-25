'''
Created on May 25, 2014
@author: yusuf
'''

import Main
from modules import move, copy

class copyCutPaste(Main.WindowSource):
    
    def doOp(self, op, pasteFile, path):
        
        if op == "copy":
            copy.copy(unicode(pasteFile), unicode(path))
        
        elif op == "cut":
            move.move(unicode(pasteFile), unicode(path))
        
        print op + " " + unicode(pasteFile) + " " + unicode(path)
        


    def __init__(self, op, pasteFile, path):
        super(copyCutPaste, self).__init__(None)
        self.doOp(op, pasteFile, path)
