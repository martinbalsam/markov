### plot clusters with centers 1d
#def visualizeCLusters(clu):
#    """
#    clu is of class: Clustering
#    """
#    if clu.system_dimension ==1:
#        for cluster in clu:
#            pnts = []
#            plt.plot(cluster.points.coords[0],np.zeros_like)
#
### plot clusters with centers general dimention and project on 2d (maybe a couple fo projections, keeping the same colors for the same clusters)
#def plotCenters(clustering):
#    
#
### scatter plot stationary distribution (correlate with cluster centers)
#
#def plot_stat_dist(clustering,msm):
#    plt.scatter()
### PCCA plot metastable sets
#
#
#def plot_free_energy(clustering,msm):
#    free_energy = - np.log(msm.stationaryDistribution)
#    plot(free_energy)