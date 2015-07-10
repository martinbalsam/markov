from log import *
import numpy as np
from pyemma.msm.analysis import pcca as pyemmapcca
MSM_DEF_LOG=LogFile("MSM_DEF_LOG")
class MSMAnalysis:
    def __init__(self, T, log=MSM_DEF_LOG, lagtime = 1.):
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
        
        self.lagtime = lagtime
        
        # eigenvalues eigenvectors and stationary distribution

        unsorted_eigenvalues,unsorted_Reigenvectors= np.linalg.eig(self.T)
        _, unsorted_Leigenvectors = np.linalg.eig(np.transpose(self.T))
        self._unsorted_eigenvalues = unsorted_eigenvalues
        unsorted_Reigenvectors = np.transpose(unsorted_Reigenvectors)
        unsorted_Leigenvectors = np.transpose(unsorted_Leigenvectors)
        #zip eigenvalues and eigenvectors
        Rzipper = zip(unsorted_eigenvalues,unsorted_Reigenvectors)
        Lzipper = zip(unsorted_eigenvalues,unsorted_Leigenvectors)
        
        #sort zippers
        sorted_Rzipper = sorted(Rzipper, reverse = True, key = lambda x: np.abs(x[0]))
        sorted_Lzipper = sorted(Lzipper, reverse = True, key = lambda x: np.abs(x[0]))
        
        #unzip
        self.eigenvalues, self.Reigenvectors = zip(*sorted_Rzipper)
        _trash, self.Leigenvectors = zip(*sorted_Lzipper)
        
        # we want to check first the transition matrix, thus the lazy definition
        self._stationaryDistribution = None
        
        self._timescales = None
        
        self.log=log
        self.log.LogSystemEvent("New instance of MSMAnalysis created",str(self),SYS_CREATE_MSMANALYSIS)
        self.log.LogSystemEvent("Trying to assign transition matrix to object, variable type " + str(type(T)), str(self),SYS_ASSIGN_TRANSITION)
    
    
    # Eigenvalues & left and right eigenvectors 
            
    @property    
    def stationaryDistribution(self):
        if (self.active==True):
            if self._stationaryDistribution is None:
                if np.allclose(self.eigenvalues[0],1):
                    self._stationaryDistribution = np.abs(self.Leigenvectors[0]/np.sum(self.Leigenvectors[0]))
                else:
                    raise ValueError("the biggest eigenvalue is not 1, something is wrong")
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
        P=np.diag(self.stationaryDistribution)
        return np.allclose(np.dot(P,self.T),np.dot(np.transpose(self.T),P))  #T.T is T transposed, I know...
    
    @property
    def timescales(self,num_of_val = 7):
        if self._timescales is None:
            real_val = np.real(self.eigenvalues[:num_of_val])
            
            self._timescales = -self.lagtime /np.log(np.absolute(real_val))
            for i in range(len(self._timescales)):
                if self._timescales[i]<0:
                    self._timescales[i] = np.inf
                    
        return self._timescales
    
    def pcca(self, m):
        """
        m is the number of metastable sets
        """
        return pyemmapcca(self.T,m)
## TODO: order the eigenvalues in decreasing absolute value
    def check_stat_dist(self):
        return np.linalg.norm(self.stationaryDistribution - np.dot(self.stationaryDistribution,self.T))
