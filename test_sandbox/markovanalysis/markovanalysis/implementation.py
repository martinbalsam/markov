"""This module provides the implementation"""

__all__ = ["getStationaryDistribution"]

import numpy as np


# draw random smaples from a given discrete distribution
def tower_sample(distribution):
    cdf = np.cumsum(distribution)
    rnd = np.random.rand() * cdf[-1]
    ind = (cdf > rnd)
    idx = np.where(ind == True)
    return np.min( idx )


# propagate a Markov chain with a given transition matrix
def evolve_chain(mu, P, length):
    chain = np.zeros(length, dtype=np.intc)
    chain[0] = tower_sample(mu)
    for i in xrange(1, length):
        chain[i] = tower_sample(P[chain[i-1],:])
    return chain


# compute a transition count matrix
def count_transitions(chain):
    n_markov_states = 5
    count_matrix = np.zeros((n_markov_states,n_markov_states), dtype=np.intc)
    for i in xrange(1, chain.shape[0]):
        count_matrix[chain[i-1], chain[i]] += 1
    return count_matrix



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



def getStationaryDistribution(P):
    eigenvalues, eigenvectors = np.linalg.eig(np.transpose(P))
    for i in xrange(eigenvalues.shape[0]):
        if (np.abs(eigenvalues[i] - 1)< 1.0E-15):
            return eigenvectors[i]/np.sum(eigenvectors[i])
