import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from cluster import read_data
import rotations


df = read_data('TAS1F06180329 (2018-10-24)-IMU.csv')

# Choose the resting sample, with only gravity affecting the IMU
# Get a mean gravity vector and mean gravity vector of the bent ankle

range_flat = range(5500, 9000)
flat_g_vector = np.mean(df.iloc[range_flat, 0:3])
range_bent = range(9210, 12200)
bent_g_vector = np.mean(df.iloc[range_bent, 0:3])

# call reorient function which rotates to align the flat_g_vector with the z axis

acc_data = rotations.reorient(df.iloc[:, 0:3], [0, 0, 1])
ori_data = rotations.reorient(df.iloc[:, 0:3], flat_g_vector, bentmean=bent_g_vector)
rot_data = rotations.reorient(df.iloc[:, 4:7], [0, 0, 1])
oriented_rot = rotations.reorient(df.iloc[:, 4:7], flat_g_vector, bentmean=bent_g_vector)

# The following lines of code are pasting the oriented data
# back onto the dataframe file and writing it to a csv

axis = ['Accelerometer X', 'Accelerometer Y', 'Accelerometer Z', 'Gyroscope X', 'Gyroscope Y', 'Gyroscope Z']
columns = [0, 1, 2, 4, 5, 6]

for i in range(3):
    df[str("Reoriented " + axis[i])] = ori_data[:, columns[i]]
for i in range(3):
    df[str("Reoriented " + axis[i + 3])] = oriented_rot[:, columns[i]]

undesirables = ['Temperature','Magnetometer X','Magnetometer Y', 'Magnetometer Z']

for i in undesirables:
    df = df.drop(i, axis="columns")

# df.to_csv('Oriented data.csv')

# Plot for demonstration


f = plt.figure(figsize=(15,8))

ax1 = f.add_subplot(121,xlim = (6000,12000),ylim = (-.3,1.1))
ax2 = f.add_subplot(122,xlim = (6000,12000),ylim = (-.3,1.1))

ax1.plot(df.iloc[:,0:3].values)
ax1.set_title('Before orientation')
ax2.plot(df.iloc[:,10:13].values)
ax2.set_title('After orientation')
plt.suptitle('Acceleration Data')

plt.show()
#f.savefig("Before_after_orientation_acc.png")


fig = plt.figure(figsize=(13,7))

ax1 = fig.add_subplot(211,xlim = (6000,25000))
ax2 = fig.add_subplot(212,xlim = (6000,25000))

ax1.plot(df.iloc[:,3:6].values)
ax1.set_title('Before orientation')
ax2.plot(df.iloc[:,13:16].values)
ax2.set_title('After first orientation')

plt.suptitle("Rotation Data")
plt.show()
# fig.savefig("Before_after_orientation_rot.png")

