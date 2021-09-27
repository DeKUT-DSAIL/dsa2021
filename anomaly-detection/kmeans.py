import numpy as np
import matplotlib.pyplot as plt

def kmeans(data, centers):

    new_cent = np.zeros(centers.shape)
    #assignment step
    dist = np.zeros((data.shape[0], centers.shape[0]))
    for i in range(centers.shape[0]):
        dist[:,i] = np.sum((data - centers[i,:])**2, 1)

    assign = np.argmin(dist,1)

    #compute new centers and cost
    cost = 0
    for i in range(centers.shape[0]):
        new_cent[i,:] = np.mean(data[assign==i,:], 0)
        cost += np.sum(np.sum((data[assign==i,:] - centers[i,:])**2, 1))

    return new_cent, cost, assign