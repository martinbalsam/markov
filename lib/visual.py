
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
    if cl.system_dimension >=2:
        if (x not in range(cl.system_dimension)) or (y not in range(cl.system_dimension)):
            raise ValueError("coordinates for projection are outside range")  
        for cluster in cl.clusters:
            pts = []
            for point in cluster.points:
                pts.append(point.coords[0])
            plt.plot(zip(*pts)[x],zip(*pts)[y],'o')
        
        
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


def plot_stat_dist(cl,ms):
    """
    cl is a CLustering object
    ms is a MSMAnalysis object
    """
    plt.scatter(log