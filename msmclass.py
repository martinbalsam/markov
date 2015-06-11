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
class MSMAnalysis:
    def __init__(self, npa_transition, log):
        self.active=True
        self.log=log
        self.log.LogSystemEvent("New instance of MSMAnalysis created",str(self),SYS_CREATE_MSMANALYSIS)
        self.log.LogSystemEvent("Trying to assign transition matrix to object, variable type " + str(type(npa_transition)), str(self),SYS_ASSIGN_TRANSITION)
        if type(npa_transition)==np.ndarray:
            if (npa_transition.ndim==2):
                if (npa_transition.shape[0]==npa_transition.shape[1]):
                    check=1
                    for j in npa_transition:
                        for i in j:
                            if ((i<0) or (i>1)):
                                check=0
                    if (check==1):
                        self.npa_transition=npa_transition
                    else:
                        self.log.LogError("Unvalid transitionMatrix,entries not between 0 and 1 ",str(self),NPA_ENTRIE_ERROR)
                        self.npa_transition=NPA_SQUARE_ERROR
                        self.active=False
                else:
                    self.log.LogError("Unvalid transitionMatrix, not square but " +str(npa_transition.shape),str(self),NPA_DIMENSION_ERROR)
                    self.npa_transition=NPA_SQUARE_ERROR
                    self.active=False
            else:
                print "Unvalid transition matrix, Dimension must equal 2, object deleted"
                self.log.LogError("Unvalid transitionMatrix dimenion " +str(npa_transition.ndim),str(self),NPA_DIMENSION_ERROR)
                self.npa_transition=NPA_DIMENSION_ERROR
                self.active=False
                
        else:
            print "Unvalid transition matrix, must be of type numpy array, object deleted"
            self.log.LogError("Unvalid transitionMatrix type "+ str(type(npa_transition)),str(self),NPA_TYPE_ERROR)
            self.npa_transition=NPA_TYPE_ERROR
            self.active=False
