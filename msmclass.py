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
        
TEST_LOG=LogFile("testLog")
class MSMAnalysis:
    def __init__(self, T, log=TEST_LOG):
        """ input:
        T : transition matrix, row stochastic np.array
        log : string of log file
        """
    
        #initialize the transition matrix
        if type(T)==np.ndarray:
            if (T.ndim==2):
                if (T.shape[0]==T.shape[1]):
                    check=1
                    for j in T:
                        for i in j:
                            if ((i<0) or (i>1)):
                                check=0
                    if (check==1):
                        self.T=T
                    else:
                        self.log.LogError("Unvalid transitionMatrix,entries not between 0 and 1 ",str(self),NPA_ENTRIE_ERROR)
                        self.T=NPA_SQUARE_ERROR
                        self.active=False
                else:
                    self.log.LogError("Unvalid transitionMatrix, not square but " +str(T.shape),str(self),NPA_DIMENSION_ERROR)
                    self.T=NPA_SQUARE_ERROR
                    self.active=False
            else:
                print "Unvalid transition matrix, Dimension must equal 2, object deleted"
                self.log.LogError("Unvalid transitionMatrix dimenion " +str(T.ndim),str(self),NPA_DIMENSION_ERROR)
                self.T=NPA_DIMENSION_ERROR
                self.active=False
                
        else:
            print "Unvalid transition matrix, must be of type numpy array, object deleted"
            self.log.LogError("Unvalid transitionMatrix type "+ str(type(T)),str(self),NPA_TYPE_ERROR)
            self.T=NPA_TYPE_ERROR
            self.active=False
        self.active=True
        self._stationaryDistribution=None
        self._eigenvectors=None
        self._eigenvalues=None
        self.log=log
        self.log.LogSystemEvent("New instance of MSMAnalysis created",str(self),SYS_CREATE_MSMANALYSIS)
        self.log.LogSystemEvent("Trying to assign transition matrix to object, variable type " + str(type(T)), str(self),SYS_ASSIGN_TRANSITION)
        
        
    @property    
    def stationaryDistribution(self):
        if (self.active==True):
            if (self._stationaryDistribution==None):
                T2= np.matrix.transpose(self.T)
                w,v=np.linalg.eig(T2)
                v2=np.matrix.transpose(v)
                for i in range(0,len(w)):
                    if (round(w[i],10)==1):
                        self._stationaryDistribution = v2[i]
            return self._stationaryDistribution
        
    @property
    def istransitionmatrix(self):
        for i in range(np.shape(self.T)[0]):
            if not np.allclose(sum(self.T[i,:]), 1):
                return False    
        return True

## TODO: order the eigenvalues in decreasing absolute value

    @property
    def eigenvalues(self):
        if (self.active==True):
            if (self._eigenvalues==None):
                self._eigenvalues = np.linalg.eig(self.T)[0]
            return self._eigenvalues
    @property
    def eigenvectors(self):
        if (self.active==True):
            if (self._eigenvectors==None):
                self._eigenvectors = np.linalg.eig(self.T)[1]
            return self._eigenvectors
        