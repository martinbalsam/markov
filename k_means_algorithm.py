

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
    
    
    
"input: data set and the number k of clusters that we want
"output: clusters_new is a list of lists, each one is a cluster
def k_means_clustering(data,k):
        means=initial(k,data)
        clusters_old=[]
        clusters_new=assignment(data,means)
        while not (clusters_old==clusters_new):
            for i in range(len(means)):
                means[i]=np.mean(clusters_new[i])
            old_means=means
            clusters_old=clusters_new
            clusters_new=assignment(data,old_means)
        return clusters_new


def k_means_clustering_faster(data,k):
        new_means=initial(k,data)
        old_means=zeros_as(new_means)
        while np.norm(new_means-old_means, np.inf)>1.0E-15: #Define max_norm or find something similar in numpy
                clusters=assignment(data,new_means)
                old_means=new_means
                for i in range(len(new_means)):
                        new_means[i]=np.mean(clusters[i])
        return clusters