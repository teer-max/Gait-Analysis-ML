import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cluster


# We will be clustering the data, parsing the raw data into features extracted over
# a variable length window. The default will be size 200 which is 2 seconds
# with respect to our data. The default step length will be 25 hz or .25s.
# Some features that we will extract from the 200 hz sample windows will be
# mean, variance, max, min, average norm, max/min norm, etc.

df = pd.read_csv('Oriented data.csv')

# We really only want the clustered data from the test/evaluation data
# to train our classifier. We will have to label manually the walking
# or running data.

#Walking Data
start_walking = 17000       #We might have to partition some of these
stop_walking = 33000        #Slices to use as training vs. testing data
#Running Data
start_running = 44000
stop_running = 60000

window = 200
steps = 25


features = {'Mean': np.mean, 'Variance': np.var, 'Max': np.max, 'Min': np.min, 'Median': np.median}

# Call Clustering algorithm to cluster the data.
# Note that the data is clustered forward, that is at
# sample 1000, we are taking the features from 1000 to 1200


walking_index = df.iloc[start_walking:stop_walking-window:25,0]
running_index = df.iloc[start_running:stop_running-window:25,0]
walkingdf = pd.DataFrame(index=walking_index)
runningdf = pd.DataFrame(index=running_index)

i = 0
for f in features:
    walkingdf = pd.concat([walkingdf,
                           pd.DataFrame(cluster.cluster(df, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                                        features[f], start=start_walking,
                                                        stop=stop_walking, window=window,
                                                        stepsize=steps), index=walking_index)],
                          axis = 1)
    i += 12
for f in features:
    runningdf = pd.concat([runningdf, pd.DataFrame(cluster.cluster(df, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], features[f],
                                                                   start=start_running, stop=stop_running,
                                                                   window=window, stepsize=steps),
                                                   index=running_index)], axis = 1)
    i += 12

# Label the data:
walkingdf.loc[:,'label'] = 1
runningdf.loc[:,'label'] = 2

# Generate the column names for the features
columns = []
for f in features:
    for j in df.columns.values[1:]:
        columns.append(str(f) + ' ' + str(j))
columns.append('label')

index = pd.concat([walking_index,running_index])

feature_matrix = pd.concat([walkingdf,runningdf])
feature_matrix.columns = columns

print(feature_matrix)

feature_matrix.to_csv('labeled feature matrix.csv')












