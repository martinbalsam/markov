

import numpy as np
import random as rd
import math

"Lloyd Algerithm for k-means"


"Step 1:Initialization"

def initial(k,data):                            "choose k initial points from the data"
    m=np.zeros(k)
    for i in range (0,k-1):
        m[i]=data[rd.randint(0,len(data)-1])    "problem: the elements of m should differ pairwise"
    return m            
                                                "m are considered as the means of the k clusters" 


"Step2:assignment of all the data to k clusters by given points in m"

def distance(a,b):
    return math.sqrt((a-b)*(a-b))
    

def distance_vector(x,m):                       "determine the distances of one data point to the elements of m"
    z=np.zeros(len(m))
    for i in range (0,len(m)-1):
        z[i]=math.sqrt((x-m[i])*(x-m[i]))
    return z
    

def cluster(x,m):                               "one element x from the data is assigned to one cluster,"
    z=distance_vector(x,m)                      "so that the distance to the mean of the corresponding cluster"
    cluster_of_x=0                              "is minimal"
    b=np.ones(len(z),dtype=bool)
    for i in range(0,len(m)-1):
        b[i]=(z[i]==min(z))
        if b[i]=True:
            cluster_of_x=i
        else:
            pass
    return cluster_of_x


def cluster_vector(data,m):                    "the i-th element of the data is assigned to cluster"
    cluster vector=np.zeros(len(data)-1)       "cluster_vector[i]"
    for i in range(0,len(data)-1):
        cluster_vector[i]=cluster(data[i],m)
    return cluster_vector

    
def assignment(v,)
       

