
from   __future__ import division     # To assure that division between two integers gives a sensible result
import sys                            # The 'sys' library is needed to handle command line args
from matplotlib import rc             # Configuration files
#mpl.use('PDF')                       # Uncomment to generate figures in PDF format

import numpy as np
import matplotlib as mpl              # A plotting framework
import matplotlib.pyplot as plt       # A plotting framework similar to MATLAB


from pylab import *
import sys

#ax = plt.subplot(111)

mpl.rcParams['xtick.major.width'] = 1.5
mpl.rcParams['xtick.minor.width'] = 1.0
mpl.rcParams['ytick.major.width'] = 1.5
mpl.rcParams['ytick.minor.width'] = 1.0
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['font.size'] = 24
mpl.rcParams['text.usetex'] = True
mpl.rcParams['legend.fontsize'] = "small"
mpl.rcParams['axes.labelsize'] = "large"
mpl.rcParams['figure.subplot.bottom'] = 0.2
mpl.rcParams['figure.subplot.left'] = 0.2
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['axes.grid'] = False
#mpl.rcParams['figure.figsize'] = 10, 8


# draw random smaples from a given discrete distribution
def tower_sample(distribution):
    cdf = np.cumsum(distribution)
    rnd = np.random.rand() * cdf[-1]
    ind = (cdf > rnd)
    idx = np.where(ind == True)
    return np.min( idx )
# propagate a Markov chain with a given transition matrix
def evolve_chain(x, P, length):
    chain = np.zeros(length, dtype=np.intc)
    chain[0] = x
    for i in xrange(1, length):
        chain[i] = tower_sample(P[chain[i-1]])
    return chain
# compute a transition count matrix
def count_transitions(chain):
    n_markov_states = np.max(chain)+1
    count_matrix = np.zeros((n_markov_states,n_markov_states), dtype=np.intc)
    for i in xrange(1, chain.shape[0]):
        count_matrix[chain[i-1], chain[i]] += 1
    return count_matrix
    
P = np.array([[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
print P
P.shape
P.shape[0]

   

"""
"""
    
