# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:20:52 2015

@author: Patze
"""

import numpy as np


"""given data count the transitions and write the result in a matrix"""

def count_matrix(data,number_of_states):
    M=np.zeros((number_of_states,number_of_states))
    for c in range(len(data)-1):
        for i in range(number_of_states):
            if data[c]==i:
                for j in range(number_of_states):
                    if data[c+1]==j:
                        M[i,j]=M[i,j]+1
    return M


"""from the count matrix compute the maximum orobability estimator (without
any other constraints)"""

def transition_matrix(data,number_of_states):
    M=count_matrix(data,number_of_states)
    T=np.zeros((number_of_states,number_of_states))
    for i in range(number_of_states):
        for j in range(number_of_states):
            T[i,j]=M[i,j]/M[i].sum()
    return T



"""Test"""

data=[0,1,1,0,0,1,2,2,2,2]
print count_matrix(data,3)
print transition_matrix(data,3)
