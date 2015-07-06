
# coding: utf-8

# In[322]:

import numpy as np
import random as rd
from numpy import linalg as LA
get_ipython().magic(u'pylab inline')
class Point:
    def __init__(self, coordinates):
        self.coords=(np.array(coordinates),0)
    def AssignCluster(self,clusternumber):
        tmp1,tmp2=self.coords
        self.coords=(tmp1,clusternumber)
    def Distance(self, point):
        if (len(self.coords[0]) == len(point)):
            return np.linalg.norm(self.coords[0]-point)
        else:
            return (-1)
        


# In[329]:

class Cluster:
    def __init__(self,clusterID):
        self.ID=clusterID
        self.points=[]
        self.center=np.array([])
        self.oldCenter=[]
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
        
        
    #def CalcFitness(self):
        #sumtmp=0.0
        #for i in self.points:
           #sumtmp = sumtmp + i.Distance(self.Center)
    


# In[336]:

class Clustering:
    def __init__(self,path, clusternumber, maxit=10, tolerance=0.01):
        self.pointlist=self.SanitizeInput(np.loadtxt(path))
        self.k=clusternumber
        self.tolerance=tolerance
        self.maxit=maxit
        self.clusters=[]
        rndsample=rd.sample(xrange(0,len(self.pointlist)),clusternumber)
        for i in range(0,clusternumber):
            self.clusters.append(Cluster(i))
            self.clusters[i].AssignCenter(self.pointlist[rndsample[i]].coords[0])

    def SanitizeInput(self,data):
        sanlist=[]
        if (len(data)==0):
            return np.array(["EmptyList"])
        elif (type(data[0])==np.ndarray):
            for i in data:
                sanlist.append(Point(i))
            return sanlist

        else:
            for i in data:
                sanlist.append(Point([i]))
            return sanlist
    def Kmeans(self):
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
        #iterations
        

        
        for iterations in range(0,self.maxit):   
            
            for clusters in self.clusters:
                print (clusters.center, len(clusters.points))
                clusters.UpdateMean()
            print "#"  
            
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
            if (norm<self.tolerance):
                break
            
        
        
        
        
def k_means_clustering_faster(data,k):
        new_means=initial(k,data)
        old_means=zeros_as(new_means)
        while np.norm(new_means-old_means, np.inf)>1.0E-5: #Define max_norm or find something similar in numpy
                clusters=assignment(data,new_means)
                old_means=new_means
                for i in range(len(new_means)):
                        new_means[i]=np.mean(clusters[i])
        return clusters        
        
        
        


# In[9]:

test=np.loadtxt("C:\\test\markov\example_1.dat")
test2=np.loadtxt("C:\\test\markov\example_2.dat")


###### test

# In[88]:

test=(1,2)
print test[0]


# In[17]:

for i in test3:
    print i


# In[342]:

clustertest=Clustering("C:\\test\markov\example_2.dat",6,6)


# In[340]:

for clusters in clustertest.clusters:
    print clusters.center


# In[129]:

for clusters in clustertest.clusters:
    print type(clusters.center)


# In[343]:

clustertest.Kmeans()


# In[321]:

for clusters in clustertest.clusters:
    pointlist=[]
    for point in clusters.points:
        pointlist.append(point.coords[0])
    plt.plot(pointlist,np.zeros_like(pointlist),'o')
    print (clusters.center, len(clusters.points))
    #plt.plot(clusters.center,np.zeros_like(center)+1)


# In[277]:

testpoint=Point([3.0,5.9,5.3])
testpoint2=Point([1.0,1.9,3.6])


# In[286]:

clustertest.clusters[1].center


# In[247]:

(testpoint.coords[0]+testpoint2.coords[0])/2.0


# In[85]:

Clu


# In[86]:

test


# In[ ]:



