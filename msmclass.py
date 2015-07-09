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
        
        # eigenvalues eigenvectors and stationary distribution

        unsorted_eigenvalues,unsorted_Reigenvectors= LA.eig(self.T)
        _, unsorted_Leigenvectors = LA.eig(np.transpose(self.T))
        elf._unsorted_eigenvalues = unsorted_eigenvalues
        self._unsorted_Reigenvectors = np.transpose(unsorted_Reigenvectors)
        self._unorted_Leigenvectors = np.transpose(unsorted_Leigenvectors)
        #zip eigenvalues and eigenvectors
        Rzipper = zip(unsorted_eigenvalues,np.transpose(unsorted_Reigenvectors))
        Lzipper = zip(unsorted_eigenvalues,np.transpose(unsorted_Leigenvectors))
        
        #sort zippers
        sorted_Rzipper = sorted(Rzipper, reverse = True, key = lambda x: np.abs(x[0]))
        sorted_Lzipper = sorted(Lzipper, reverse = True, key = lambda x: np.abs(x[0]))
        
        #unzip
        self.eigenvalues, self.Reigenvectors = zip(*sorted_Rzipper)
        _trash, self.Leigenvectors = zip(*sorted_Lzipper)
        
        # we want to check first the transition matrix, thus the lazy definition
        self._stationaryDistribution = None
        
        self.log=log
        self.log.LogSystemEvent("New instance of MSMAnalysis created",str(self),SYS_CREATE_MSMANALYSIS)
        self.log.LogSystemEvent("Trying to assign transition matrix to object, variable type " + str(type(T)), str(self),SYS_ASSIGN_TRANSITION)
    
    
    # Eigenvalues & left and right eigenvectors 
            
    @property    
    def stationaryDistribution(self):
        if (self.active==True):
            if self._stationaryDistribution is None:
                if np.allclose(self.eigenvalues[0],1):
                    self._stationaryDistribution = self.Leigenvectors[0]
            return self._stationaryDistribution
        
    @property
    def istransitionmatrix(self):
        for i in range(np.shape(self.T)[0]):
            if not np.allclose(sum(self.T[i,:]), 1):
                return False    
        return True
    @property
    def isreversible(self):
        """
        checks the reversed balance condition p_i T_ij == p_j T_ij
        """
        P=diag(self.stationaryDistribution)
        return np.allclose(np.dot(P,T),np.dot(T.T,P))  #T.T is T transposed, I know...
    
## TODO: order the eigenvalues in decreasing absolute value
