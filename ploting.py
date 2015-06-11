MM= np.random.randint(1, 100, (4, 100, 2)) 
# create a a rndom matrix containe 4 amtrix, where every matrix is 100x2 
# 4 represant k in our case (the number of clusters)
# 2 represant the dimension (in our case is 1 or 5)
#100 is the number of elements in each clusters (here all are 100, but only to test the plot option, in our case every clusters has a given different number of elements)



for i in range(4):
    plt.plot(MM[i,:,0], MM[i,:,1], 'o') #MM[i,:,0] represnt the x line of the cluster i
    #MM[i,:,1] represnt the y line of the cluster i
plt.axis([-1, 101, -1, 101])
#of course in our case the points of the same color will be near
#here is not seem because I did not make the k-means, is only a plot test