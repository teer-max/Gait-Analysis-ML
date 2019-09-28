import pandas as pd
import numpy as np
import cluster
import rotations
import pickle
import matplotlib.pyplot as plt

# Goal is to extract these features from the raw data:

features = ['Mean Reoriented Accelerometer X',
            'Mean Reoriented Accelerometer Z',
            'Variance Reoriented Accelerometer X',
            'Variance Reoriented Accelerometer Y',
            'Variance Reoriented Accelerometer Z',
            'Variance Reoriented Gyroscope Y',
            'Max Reoriented Accelerometer Y',
            'Max Reoriented Accelerometer Z',
            'Min Reoriented Accelerometer X',
            'Min Reoriented Accelerometer Z',
            'Min Reoriented Gyroscope X',
            'Min Reoriented Gyroscope Y',
            'Min Reoriented Gyroscope Z',
            'label']

# Read Data
df = cluster.read_data('TAS1F06180329 (2018-10-24)-IMU.csv')

# Reorient data
# Requires a couple parameters: The average g vector for the flat foot,
# and the average g vector (on the xz plane) after being rotated about the y axis

range_flat = range(5500, 9000)
flat_g_vector = np.mean(df.iloc[range_flat, 0:3])
range_bent = range(9210, 12200)
bent_g_vector = np.mean(df.iloc[range_bent, 0:3])

ori_data = rotations.reorient(df.iloc[:, 0:3], flat_g_vector, bentmean=bent_g_vector)
oriented_rot = rotations.reorient(df.iloc[:, 4:7], flat_g_vector, bentmean=bent_g_vector)

ori_data = pd.DataFrame(ori_data, index=df.index)
oriented_rot = pd.DataFrame(oriented_rot, index=df.index)

# This is the reoriented data: Notice it has the same index as the original

df2 = pd.concat([ori_data,oriented_rot],axis=1)
df2.index = df.index

# Extract features: Make feature dictionary

fdict = {'Mean Reoriented Accelerometer X':[np.mean,0],
            'Mean Reoriented Accelerometer Z':[np.mean,2],
            'Variance Reoriented Accelerometer X':[np.var,0],
            'Variance Reoriented Accelerometer Y':[np.var,1],
            'Variance Reoriented Accelerometer Z':[np.var,2],
            'Variance Reoriented Gyroscope Y':[np.var,4],
            'Max Reoriented Accelerometer Y':[np.max,1],
            'Max Reoriented Accelerometer Z':[np.max,2],
            'Min Reoriented Accelerometer X':[np.min,0],
            'Min Reoriented Accelerometer Z':[np.min,2],
            'Min Reoriented Gyroscope X':[np.min,3],
            'Min Reoriented Gyroscope Y':[np.min,4],
            'Min Reoriented Gyroscope Z':[np.min,5]}

# Define some parameters for clustering: start of clustering, end of clustering,
# window length, steplength between windows, etc. the two parameters are function and column.

window = 200
stepsize = 25
index = df.index[:-400:25]

# cluster_data = pd.DataFrame(index=index)
# for f in fdict:
#     cls = cluster.cluster(df2, [fdict[f][1]], fdict[f][0], start=0,
#                           stop=len(df) - window,window=window,
#                           stepsize=stepsize)
#     cls = pd.DataFrame(cls, index=index)
#     print(f)
#     cluster_data = pd.concat([cluster_data, cls], axis=1)
#
# print(cluster_data)
#
# cluster_data.to_csv('feature_cluster.csv')


cluster_data = pd.read_csv('feature_cluster.csv', index_col=0)
print(cluster_data)
# Now we can finally run the Classifier saved in the pickle file. Importing sklearn...

neigh = pickle.load(open('neighbors.pickle','rb'))

predictions = neigh.predict(cluster_data)

plt.plot(predictions, 'ro', markersize=1)
cluster_data[cluster_data.columns[1]].plot()
plt.suptitle('Classification overlaying Accelerometer X-Axis')
plt.show()