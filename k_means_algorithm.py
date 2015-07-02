

import numpy as np
import random as rd
import math
from numpy import linalg as LA


"Lloyd Algerithm for k-means"


"Step 1:Initialization"

def initial(k,data):
    m=[]
    sampl = rd.sample(xrange(data.shape[0]), k)
    for i in sampl:
            m.append(data[i])
    return m           
                                                
    
    
"m are considered as the means of the k clusters" 


"Step2:assignment of all the data to k clusters by given points in m"
def assignment(data, means):
        k=len(means)
        clusters=[]
        for i in range(k):
                clusters.append([])
        for x in data:
                distance_vector=[]
                for m in means:
                        distance_vector.append(LA.norm(x-m))
                clusters[np.argmin(distance_vector)].append(x)
        return clusters
    
    
    
"input: data set and the number k of clusters that we want"
"output: clusters_new is a list of lists, each one is a cluster"
def k_means_clustering_faster(data,k):
        new_means=np.array(initial(k,data))
        old_means=np.zeros_like(new_means)
        while not np.allclose(new_means,old_means,rtol=1e-5): #Define max_norm or find something similar in numpy
                clusters=assignment(data,new_means)
                old_means=new_means
                for i in range(len(new_means)):
                        new_means[i]=np.mean(clusters[i])
        return clusters

def time_series_states_vector(data,clusters):
        ts_states_vector=[]:
                for x in data:
                        for i in len(clusters):

def fitness(clusters,centers):
        fitness=0
        for cluster in clusters:
                

def getStatesFromTimeSeries(data, clusters):
        for i in range(len(clusters)):
                