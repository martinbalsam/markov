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
import matplotlib.pyplot as plt
import numpy as np

def VisualizeCusters(cl):
    if cl.system_dimension <=0:
        raise ValueError("system dimention error")
    if cl.system_dimension == 1:
        for cluster in cl.clusters:
            pts =[]
            min = -100
            max = 100
            for point in cluster.points:
                pts.append(point.coords[0][0])
            min = amin(pts)
            
            plt.plot(pts,np.zeros_like(pts),'o')
    if cl.system_dimension >=2:
        pippo = "do stuff"
        
def VisualizeCusters_loc(cl):
    if cl.system_dimension <=0:
        raise ValueError("system dimention error")
    if cl.system_dimension == 1:
        for cluster in cl.clusters:
            pts =[]
            min = -100
            max = 100
            for point in cluster.points:
                pts.append(point.coords[0][0])

            plt.plot(pts,np.zeros_like(pts),'o')
    if cl.system_dimension >=2:
        pippo = "do stuff"
        
def VisualizeCenters(cl,x=0,y=1):
    if cl.system_dimension <=0:
        raise ValueError("system dimention error")
    if cl.system_dimension == 1:
        for cluster in cl.clusters:
            plt.plot(cluster.center[0],cluster.ID,'o')
    if cl.system_dimension >=2:
        if (x not in range(cl.system_dimension)) or (y not in range(cl.system_dimension)):
            raise ValueError("coordinates for projection are outside range")        
        for cluster in cl.clusters:
            plt.plot(cluster.center[x],cluster.center[y],'o')
