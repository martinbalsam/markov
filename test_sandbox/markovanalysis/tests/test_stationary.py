"""This is the test collection for the Horner scheme"""

from nose.tools import assert_true
from markovanalysis import getStationaryDistribution
import numpy as np

def test_A():
    """Testing the the getStationaryDistribution function"""
    tr_matrix = np.array([
        [0.5, 0.2, 0.2, 0.1],
        [0.5, 0.1, 0.2, 0.2],
        [0.1, 0.2, 0.3, 0.4],
        [0.2, 0.3, 0.4, 0.1]], dtype=np.float64)
    pi = getStationaryDistribution(tr_matrix)
    
    for i in xrange(pi.shape[0]):
        assert_true(np.abs(np.dot(pi,tr_matrix)[i] - pi[i])<1.0E-15)