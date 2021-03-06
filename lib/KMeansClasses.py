# coding: utf-8

import time
import numpy as np
import random as rd
from numpy import linalg as LA
#get_ipython().magic(u'pylab inline')
def keyf(point):
    return point.pointnum
def key2(tup):
    x,y = tup
    return y
class Point:
    def __init__(self, coordinates,pointnum):
        self.coords=(np.array(coordinates),0)
        self.pointnum=pointnum
    def AssignCluster(self,clusternumber):
        tmp1,tmp2=self.coords
        self.coords=(tmp1,clusternumber)
    def Distance(self, point):
        if (len(self.coords[0]) == len(point)):
            return np.linalg.norm(self.coords[0]-point)
        else:
            return (-1)
        


class Cluster:
    def __init__(self,clusterID):
        self.ID=clusterID
        self.points=[]
        self.center=np.array([])
        self.oldcenter=[]
        self.fitness=0.0
    def AssignCenter(self,center):
        self.center=center
    def AddPoint(self, Ipoint):
        Ipoint.AssignCluster(self.ID)
        self.points.append(Ipoint)
    def UpdateMean(self):
        self.oldcenter=self.center
        self.center=np.zeros_like(self.center)
        for point in self.points:
            self.center=self.center + point.coords[0]
        self.center=self.center/len(self.points)
        
        



class Clustering:
    def __init__(self,path, clusternumber, maxit=10, tolerance=0.01):
        self.pointlist=self.SanitizeInput(np.loadtxt(path))
        self.k=clusternumber
        self.tolerance=tolerance
        self.maxit=maxit
        self.clusters=[]
        self._cluster_centers = None
        self.trajectory = []
        self.system_dimension = len(self.pointlist[0].coords[0] )          
        rndsample=rd.sample(xrange(0,len(self.pointlist)),clusternumber)
        rndsample2=[]
        #order in 1d case
        if (self.system_dimension==1):
            for i in range(0,len(rndsample)):
                rndsample2.append((rndsample[i],self.pointlist[rndsample[i]].coords[0]))
            rndsample2 = sorted(rndsample2,key=key2)
            rndsample=[]
            for i in rndsample2:
                rndsample.append(i[0]) 
        for i in range(0,clusternumber):
            self.clusters.append(Cluster(i))
            self.clusters[i].AssignCenter(self.pointlist[rndsample[i]].coords[0])

    @property
    def clustercenters(self):
        if self._cluster_centers is None:
            centers = []
            for cluster in self.clusters:
                centers.append(cluster.center)
            self._cluster_centers =  centers
        return self._cluster_centers
    
    def SanitizeInput(self,data):
        sanlist=[]
        if (len(data)==0):
            return np.array(["EmptyList"])
        elif (type(data[0])==np.ndarray):
            for i in range(0,len(data)):
                sanlist.append(Point(data[i],i))
            return sanlist

        else:
            for i in range(0,len(data)):
                sanlist.append(Point([data[i]],i))
            return sanlist
    def Kmeans(self):
        tic = time.clock()
        for cluster in self.clusters:
            cluster.points=[]
        for point in self.pointlist:
            pointco = point.coords[0]
            #bestcluster=self.clusters
            closestcluster = (self.clusters[0],point.Distance(self.clusters[0].center))
            for cluster in self.clusters:
                if (point.Distance(cluster.center)<closestcluster[1]):
                    closestcluster=(cluster,point.Distance(cluster.center))
            tmppointer=closestcluster[0]
            tmppointer.AddPoint(point)
        self.pointlist=[]
        toc = time.clock()
        print toc-tic
        #iterations
        if (self.system_dimension==1):
            self.Kmeans1D()
        else:
            for iteration in range(0,self.maxit):   
            
                for clusters in self.clusters:
                #    print (clusters.center, len(clusters.points))
                    clusters.UpdateMean()
                #print "#"  
                for cluster in self.clusters:
                    for point in cluster.points:
                        self.pointlist.append(point)
                    cluster.points=[]
                for point in self.pointlist:
                    pointco = point.coords[0]
                    bestcluster=self.clusters
                    closestcluster = (self.clusters[0],point.Distance(self.clusters[0].center))
                    for cluster in self.clusters:
                        if (point.Distance(cluster.center)<closestcluster[1]):
                            closestcluster=(cluster,point.Distance(cluster.center))
                    tmppointer=closestcluster[0]
                    tmppointer.AddPoint(point)
                self.pointlist=[]
                #check if norm is not changing anymonre
                centervectornew=[]
                centervectorold=[]
                for cluster in self.clusters:
                    centervectornew.append(cluster.center)
                    centervectorold.append(cluster.oldcenter)
                norm = LA.norm(np.array(centervectornew)-np.array(centervectorold))
                print norm
                print iteration
                if (norm<self.tolerance):
                    break
                
            for cluster in self.clusters:
                for point in cluster.points:
                    self.pointlist.append(point)
                #cluster.points=[]
            returnlist=[]
            for i in sorted(self.pointlist,key=keyf):
                returnlist.append(i.coords[1])
            self.trajectory = returnlist
    def Kmeans1D(self):
        print "entering accelerated stage"
        clusterlen=len(self.clusters)-1
        for iteration in range(0,self.maxit):
            tic=time.clock()
            for clusters in self.clusters:
                #    print (clusters.center, len(clusters.points))
                clusters.UpdateMean()
                #print "#"  
            for cluster in self.clusters:
                for point in cluster.points:
                    self.pointlist.append(point)
                cluster.points=[]

            for point in self.pointlist:
                pointco = point.coords[0]
                #bestcluster=self.clusters
                closestcluster = (point.coords[1],point.Distance(self.clusters[point.coords[1]].center))
                stat=0
                if (point.coords[1]==clusterlen):
                    stat=-1
                elif (point.coords[1]==0):
                    stat=1
                elif (point.coords[0]>self.clusters[point.coords[1]+1].center):
                    stat=1
                elif (point.coords[0]<self.clusters[point.coords[1]-1].center):
                    stat=-1
                if (stat==0):
                    for runvar in range(-1,2,1):
                        if (point.Distance(self.clusters[point.coords[1]+runvar].center)<closestcluster[1]):
                            closestcluster=(point.coords[1]+runvar,point.Distance(self.clusters[point.coords[1]+runvar].center))
                elif (stat==1):
                    center=point.coords[1]
                    done=False
                    while (done==False):
                        center=center+1
                        if (center==clusterlen):
                            center=center-1
                            done=True
                        if (point.coords[0]<self.clusters[center+1].center):
                            done=True
                    for runvar in range(-1,2,1):
                        if (point.Distance(self.clusters[center+runvar].center)<closestcluster[1]):
                            closestcluster=(center+runvar,point.Distance(self.clusters[center+runvar].center))


                elif (stat==-1):
                    center=point.coords[1]
                    done=False
                    while (done==False):
                        center=center-1
                        if (center==0):
                            center=center+1
                            done=True
                        if (point.coords[0]>self.clusters[center-1].center):
                            done=True
                    for runvar in range(-1,2,1):
                        if (point.Distance(self.clusters[center+runvar].center)<closestcluster[1]):
                            closestcluster=(center+runvar,point.Distance(self.clusters[center+runvar].center))                    
                    #biggerstuff
                    
                self.clusters[closestcluster[0]].AddPoint(point)
            self.pointlist=[]
            #check if norm is not changing anymore
            centervectornew=[]
            centervectorold=[]
            for cluster in self.clusters:
                centervectornew.append(cluster.center)
                centervectorold.append(cluster.oldcenter)
            norm = LA.norm(np.array(centervectornew)-np.array(centervectorold))
            print norm
            print iteration
            toc=time.clock()
            print (toc-tic)
            if (norm<self.tolerance):
                break
                
        for cluster in self.clusters:
            for point in cluster.points:
                self.pointlist.append(point)
            #cluster.points=[]
        returnlist=[]
        for i in sorted(self.pointlist,key=keyf):
            returnlist.append(i.coords[1])
        self.trajectory = returnlist

            
    def GetEstimator(self):
        return Estimation(self.trajectory,self.k)
        
        
        
class Estimation:
    def __init__(self,dtraj,number_of_clusters):        
        self.dtraj = dtraj
        self.number_of_clusters = number_of_clusters
        self.count_matrix = self.ComputeCountMatrix()
        self.transition_matrix = None
        
    @property
    def isconnected(self):
        return ( len(kosaraju(self.count_matrix)) == 1 )
        
    def ComputeCountMatrix(self):
        """
        computes the count matrix from the discrete trajectory
        
        TODO: add
        -timelag
        -time slide
        """
        C=np.zeros((self.number_of_clusters,self.number_of_clusters))
        for k in range(len(self.dtraj)-1):
            for i in range(self.number_of_clusters):
                if self.dtraj[k]==i:
                    for j in range(self.number_of_clusters):
                        if self.dtraj[k+1]==j:
                            C[i,j]=C[i,j]+1
        return C
    
    
# depth_first_search
def depth_first_search(graph, node, node_list):
    node_list.append(node)
    for i in range(graph.shape[0]):
        if (graph[node,i]>0) and (i not in node_list):
            depth_first_search(graph,i,node_list)
    node_list.remove(node)
    node_list.append(node)
# kosaraju
def kosaraju(graph):
    V=[]
    com_classes=[]
    gra=np.array(graph)
    dimention=gra.shape[0]
    while len(V)<dimention:
        for i in range(dimention):
            if i not in V:
                depth_first_search(gra,i,V)
    while len(V)>0:
        C=[]
        depth_first_search(np.transpose(gra),V[-1],C)
        com_classes.append(C)
        for i in C:
            V.remove(i)  #remove the elements in C from V
            gra[i,:]=0 #remove the nodes in C from the graph
            gra[:,i]=0
    return com_classes   #return the comunication classes as a list of lists

def isCountMatrix(C):
    """
    Checks if every row has at least one non zero entry
    """
    if np.any(np.isclose([C[i, :].sum() for i in range(len(C))], 0)):
        return False
    return True
def estimate_irreversible(C):
    """
    naive irreversible transition matrix
    input:
    C : count matrix, integer valued, each row must contain at least one positive value
    
    output:
    T : transition matrix, row-stochastic, numpy array, dtype= "float"
    """
    if not isCountMatrix(C):
        raise ValueError("the input matrix is not a count matrix")
    
    d = np.shape(C)[0]
    T = np.zeros_like(C, dtype=float)
    for i in range(d):
        for j in range(d):
            T[i,j]=C[i,j]/C[i].sum()
    return T

def estimate_reversible(C,maxiter=10000000,tolerance = 1e-13):
    """
    estimator of maximum likelihood of a reversible transition matrix
    
    input:
    C : count matrix
    maxiter : the maximum number of iterations before stopping automatically. Default: 10'000'000
    tolerance : the olgorithm stops when the maximum difference between two entries of two iterations is below "tollerance"
    """
    dim = C.shape[0]
    # first estimation using "estimate_irreversible()"
    X_new = estimate_irreversible(C)
    
    #compute C[i,j]+C[j,i] and the vector csum (the sum of each row of C) only once,  better than doing it everytime in the loop [giulio]
    csum = [sum(C[i,:]) for i in range(dim)]
    C2 = C + C.T
    
    # convergence
    #first iteration == True
    diff = 1.
    iteration = 1
    while diff > tolerance and iteration < maxiter:
        diff = 0.
        #copy the matrix, not just reassign the value
        X = np.copy(X_new)
        xsum = [sum(X[i,:]) for i in range(dim)]
        for i in range(dim):
            for j in range(dim):
                X_new[i,j]=C2[i,j]/((csum[i]/xsum[i]) + (csum[j]/xsum[j]) )
                if abs(X_new[i,j]-X[i,j]>diff):
                    diff = abs(X_new[i,j]-X[i,j]>diff)
        iteration += 1
    T = np.zeros_like(X_new)
    for i in range(dim):
        T[i] = X_new[i]/sum(X_new[i])
    print "number of iterations: ", iteration
    return T 


# depth_first_search
def depth_first_search(graph, node, node_list):
    node_list.append(node)
    for i in range(graph.shape[0]):
        if (graph[node,i]>0) and (i not in node_list):
            depth_first_search(graph,i,node_list)
    node_list.remove(node)
    node_list.append(node)
# kosaraju
def kosaraju(graph):
    V=[]
    com_classes=[]
    gra=np.array(graph)
    dimention=gra.shape[0]
    while len(V)<dimention:
        for i in range(dimention):
            if i not in V:
                depth_first_search(gra,i,V)
    while len(V)>0:
        C=[]
        depth_first_search(np.transpose(gra),V[-1],C)
        com_classes.append(C)
        for i in C:
            V.remove(i)  #remove the elements in C from V
            gra[i,:]=0 #remove the nodes in C from the graph
            gra[:,i]=0
    return com_classes   #return the comunication classes as a list of lists


def get_size_largest_element(array):
    sizes=[]
    for i in array:
        sizes.append(len(i))
    return max(sizes)

def isConnected(count_matrix):
    return len(kosaraju(count_matrix)) == 1
