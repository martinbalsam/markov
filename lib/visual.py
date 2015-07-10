
import matplotlib.pyplot as plt
import numpy as np

def VisualizeCusters(cl,x=0,y=1):
    if cl.system_dimension <=0:
        raise ValueError("system dimention error")
    if cl.system_dimension == 1:
        for cluster in cl.clusters:
            pts =[]
            for point in cluster.points:
                pts.append(point.coords[0][0])
            
            plt.plot(pts,cluster.ID * np.ones_like(pts),'o')
        plt.suptitle("Clusters")            
    if cl.system_dimension >=2:
        if (x not in range(cl.system_dimension)) or (y not in range(cl.system_dimension)):
            raise ValueError("coordinates for projection are outside range")  
        for cluster in cl.clusters:
            pts = []
            for point in cluster.points:
                pts.append(point.coords[0])
            plt.plot(zip(*pts)[x],zip(*pts)[y],'o')
        plt.suptitle("Clusters")
        
        
def VisualizeCenters(cl,x=0,y=1):
    if cl.system_dimension <=0:
        raise ValueError("system dimention error")
    if cl.system_dimension == 1:
        for cluster in cl.clusters:
            plt.plot(cluster.center[0],cluster.ID,'o')
        plt.suptitle("Cluster centers")
    if cl.system_dimension >=2:
        if (x not in range(cl.system_dimension)) or (y not in range(cl.system_dimension)):
            raise ValueError("coordinates for projection are outside range")        
        for cluster in cl.clusters:
            plt.plot(cluster.center[x],cluster.center[y],'o')
        plt.suptitle("Cluster centers")


def plot_stat_dist(cl,ms):
    """
    cl is a CLustering object
    ms is a MSMAnalysis object
    """
    if cl.system_dimension == 1:
        centers = [center[0] for center in cl.clustercenters]
        plt.scatter(centers, np.log(ms.stationaryDistribution))
        plt.suptitle("log(stationaryDistribution)")
    else:
        raise ValueError("not a 1 dimentional system")

def plot_free_energy(cl,ms):
    """
    cl is a CLustering object
    ms is a MSMAnalysis object
    """
    if cl.system_dimension == 1:
        centers = [center[0] for center in cl.clustercenters]
        plt.scatter(centers, -np.log(ms.stationaryDistribution))
        plt.suptitle("Free energy")
    else:
        raise ValueError("not a 1 dimentional system")


def plot_eigenvalues(ms,number = 5):
    if number<1 or number>ms.T.shape[0]:
        raise ValueError("number of eigenvalues requested is out of range")
    plt.plot(range(number),np.absolute(ms.eigenvalues)[:number],'o')
    plt.suptitle("Absolute value of the first eigenvalues")

def plot_eigenvector(cl,ms,index):
    """
    plot the index-th eigenvector
    """
    if index > cl.k or index < 0:
        raise ValueError("index not in range")
    
    if cl.system_dimension == 1:
        centers = [center[0] for center in cl.clustercenters]
        plt.plot(centers, ms.Reigenvectors[index])
        plt.suptitle("Eigenvector")
    else:
        raise ValueError("not a 1 dimentional system")
    
def visualize_pcca(cl,ms,m):
    memb = ms.pcca(m)
    centers = [center[0] for center in cl.clustercenters]
    for i in range(m):
        plt.plot(centers_loc,zip(*memb)[i],'o')
    plt.suptitle("pcca membership probability")
    