import numpy as np
NPA_DIMENSION_ERROR=1
NPA_SQUARE_ERROR=1
NPA_TYPE_ERROR=2
NPA_ENTRIE_ERROR=2
SYS_CREATE_MSMANALYSIS=100
SYS_ASSIGN_TRANSITION=101
class LogFile:
    def __init__(self,comment):
        self.comment=comment
        self.logfile=[]
    def LogSystemEvent(self, message, objectdesc,code):
        self.logfile.append((message,objectdesc,str(code)))
    def LogError(self,errormessage, objectdesc,code):
        self.logfile.append((errormessage,objectdesc, str(code)))
        
