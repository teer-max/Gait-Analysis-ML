#This script is to Cluster the Data.
# It acts on an array of data and outputs
# clusters of the data under some function.
# The parameters for these clusters are
# Window, Stepsize, starts, stops, etc.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(data):
    df = pd.read_csv(data, header=10, index_col=0, float_precision="high")
    return df


def cluster(data, columns, function, start, stop, window, stepsize):
    
    clusters = int((stop-window-start)/stepsize)
    
    clust = np.empty((clusters, len(columns)))
    
    for k in range(0, len(columns)):
        j = columns[k]
        for i in range(0, clusters):
            clust[i, k] = function(data.iloc[(i*stepsize)+start:(i*stepsize)+start+window,j])
    return clust


