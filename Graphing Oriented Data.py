import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy.fftpack import fft
style.use('ggplot')



df = pd.read_csv('Some Features2.csv')


labels = df.columns.values
print(labels)

g, axes = plt.subplots(2,1)

print(df.iloc[:,0])

N  = len(df)
freq = 100
t = 1/freq
x = np.linspace(0.0,N*t,N)
ff =


axes[0,0].plot(df.iloc[:,0])
axes[0,0].plot(fft(df.iloc[:,0]),)

'''
f, axarr = plt.subplots(3,2)


axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Mean Accelerometer X Walking'])
axarr[0,0].plot(df['Mean Accelerometer X Running'])
axarr[0,1].plot(df['Mean Reoriented Accelerometer X Walking'])
axarr[0,1].plot(df['Mean Reoriented Accelerometer X Running'])
axarr[1,0].plot(df['Mean Accelerometer Y Walking'])
axarr[1,0].plot(df['Mean Accelerometer Y Running'])
axarr[1,1].plot(df['Mean Reoriented Accelerometer Y Walking'])
axarr[1,1].plot(df['Mean Reoriented Accelerometer Y Running'])
axarr[2,0].plot(df['Mean Accelerometer Z Walking'])
axarr[2,0].plot(df['Mean Accelerometer Z Running'])
axarr[2,1].plot(df['Mean Reoriented Accelerometer Z Walking'])
axarr[2,1].plot(df['Mean Reoriented Accelerometer Z Running'])

f.suptitle('Mean Accelerometer')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Mean Gyroscope X Running'])
axarr[0,0].plot(df['Mean Gyroscope X Walking'])
axarr[0,1].plot(df['Mean Reoriented Gyroscope X Walking'])
axarr[0,1].plot(df['Mean Reoriented Gyroscope X Running'])
axarr[1,0].plot(df['Mean Gyroscope Y Walking'])
axarr[1,0].plot(df['Mean Gyroscope Y Running'])
axarr[1,1].plot(df['Mean Reoriented Gyroscope Y Walking'])
axarr[1,1].plot(df['Mean Reoriented Gyroscope Y Running'])
axarr[2,0].plot(df['Mean Gyroscope Z Walking'])
axarr[2,0].plot(df['Mean Gyroscope Z Running'])
axarr[2,1].plot(df['Mean Reoriented Gyroscope Z Walking'])
axarr[2,1].plot(df['Mean Reoriented Gyroscope Z Running'])

f.suptitle('Mean Gryoscope')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Variance Accelerometer X Walking'])
axarr[0,0].plot(df['Variance Accelerometer X Running'])
axarr[0,1].plot(df['Variance Reoriented Accelerometer X Walking'])
axarr[0,1].plot(df['Variance Reoriented Accelerometer X Running'])
axarr[1,0].plot(df['Variance Accelerometer Y Walking'])
axarr[1,0].plot(df['Variance Accelerometer Y Running'])
axarr[1,1].plot(df['Variance Reoriented Accelerometer Y Walking'])
axarr[1,1].plot(df['Variance Reoriented Accelerometer Y Running'])
axarr[2,0].plot(df['Variance Accelerometer Z Walking'])
axarr[2,0].plot(df['Variance Accelerometer Z Running'])
axarr[2,1].plot(df['Variance Reoriented Accelerometer Z Walking'])
axarr[2,1].plot(df['Variance Reoriented Accelerometer Z Running'])

f.suptitle('Variance Accelerometer')

plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Variance Gyroscope X Running'])
axarr[0,0].plot(df['Variance Gyroscope X Walking'])
axarr[0,1].plot(df['Variance Reoriented Gyroscope X Walking'])
axarr[0,1].plot(df['Variance Reoriented Gyroscope X Running'])
axarr[1,0].plot(df['Variance Gyroscope Y Walking'])
axarr[1,0].plot(df['Variance Gyroscope Y Running'])
axarr[1,1].plot(df['Variance Reoriented Gyroscope Y Walking'])
axarr[1,1].plot(df['Variance Reoriented Gyroscope Y Running'])
axarr[2,0].plot(df['Variance Gyroscope Z Walking'])
axarr[2,0].plot(df['Variance Gyroscope Z Running'])
axarr[2,1].plot(df['Variance Reoriented Gyroscope Z Walking'])
axarr[2,1].plot(df['Variance Reoriented Gyroscope Z Running'])

f.suptitle('Variance Gyroscope')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Max Accelerometer X Walking'],'bo',markersize=2)
axarr[0,0].plot(df['Max Accelerometer X Running'],'ro',markersize=2)
axarr[0,1].plot(df['Max Reoriented Accelerometer X Walking'],'bo',markersize=2)
axarr[0,1].plot(df['Max Reoriented Accelerometer X Running'],'ro',markersize=2)
axarr[1,0].plot(df['Max Accelerometer Y Walking'],'bo',markersize=2)
axarr[1,0].plot(df['Max Accelerometer Y Running'],'ro',markersize=2)
axarr[1,1].plot(df['Max Reoriented Accelerometer Y Walking'],'bo',markersize=2)
axarr[1,1].plot(df['Max Reoriented Accelerometer Y Running'],'ro',markersize=2)
axarr[2,0].plot(df['Max Accelerometer Z Walking'],'bo',markersize=2)
axarr[2,0].plot(df['Max Accelerometer Z Running'],'ro',markersize=2)
axarr[2,1].plot(df['Max Reoriented Accelerometer Z Walking'],'bo',markersize=2)
axarr[2,1].plot(df['Max Reoriented Accelerometer Z Running'],'ro',markersize=2)

f.suptitle('Max Accelerometer')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Max Gyroscope X Running'],'bo',markersize=2)
axarr[0,0].plot(df['Max Gyroscope X Walking'],'ro',markersize=2)
axarr[0,1].plot(df['Max Reoriented Gyroscope X Walking'],'bo',markersize=2)
axarr[0,1].plot(df['Max Reoriented Gyroscope X Running'],'ro',markersize=2)
axarr[1,0].plot(df['Max Gyroscope Y Walking'],'bo',markersize=2)
axarr[1,0].plot(df['Max Gyroscope Y Running'],'ro',markersize=2)
axarr[1,1].plot(df['Max Reoriented Gyroscope Y Walking'],'bo',markersize=2)
axarr[1,1].plot(df['Max Reoriented Gyroscope Y Running'],'ro',markersize=2)
axarr[2,0].plot(df['Max Gyroscope Z Walking'],'bo',markersize=2)
axarr[2,0].plot(df['Max Gyroscope Z Running'],'ro',markersize=2)
axarr[2,1].plot(df['Max Reoriented Gyroscope Z Walking'],'bo',markersize=2)
axarr[2,1].plot(df['Max Reoriented Gyroscope Z Running'],'ro',markersize=2)

f.suptitle('Max Gyroscope')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0,0].set_title('Before Orientation')
axarr[0,1].set_title('After Orientation')

axarr[0,0].plot(df['Min Accelerometer X Walking'],'bo',markersize=2)
axarr[0,0].plot(df['Min Accelerometer X Running'],'ro',markersize=2)
axarr[0,1].plot(df['Min Reoriented Accelerometer X Walking'],'bo',markersize=2)
axarr[0,1].plot(df['Min Reoriented Accelerometer X Running'],'ro',markersize=2)
axarr[1,0].plot(df['Min Accelerometer Y Walking'],'bo',markersize=2)
axarr[1,0].plot(df['Min Accelerometer Y Running'],'ro',markersize=2)
axarr[1,1].plot(df['Min Reoriented Accelerometer Y Walking'],'bo',markersize=2)
axarr[1,1].plot(df['Min Reoriented Accelerometer Y Running'],'ro',markersize=2)
axarr[2,0].plot(df['Min Accelerometer Z Walking'],'bo',markersize=2)
axarr[2,0].plot(df['Min Accelerometer Z Running'],'ro',markersize=2)
axarr[2,1].plot(df['Min Reoriented Accelerometer Z Walking'],'bo',markersize=2)
axarr[2,1].plot(df['Min Reoriented Accelerometer Z Running'],'ro',markersize=2)

f.suptitle('Min Accelerometer')
plt.show()

f, axarr = plt.subplots(3,2)

axarr[0, 0].set_title('Before Orientation')
axarr[0, 1].set_title('After Orientation')

axarr[0,0].plot(df['Min Gyroscope X Running'],'bo',markersize=2)
axarr[0,0].plot(df['Min Gyroscope X Walking'],'ro',markersize=2)
axarr[0,1].plot(df['Min Reoriented Gyroscope X Walking'],'bo',markersize=2)
axarr[0,1].plot(df['Min Reoriented Gyroscope X Running'],'ro',markersize=2)
axarr[1,0].plot(df['Min Gyroscope Y Walking'],'bo',markersize=2)
axarr[1,0].plot(df['Min Gyroscope Y Running'],'ro',markersize=2)
axarr[1,1].plot(df['Min Reoriented Gyroscope Y Walking'],'bo',markersize=2)
axarr[1,1].plot(df['Min Reoriented Gyroscope Y Running'],'ro',markersize=2)
axarr[2,0].plot(df['Min Gyroscope Z Walking'],'bo',markersize=2)
axarr[2,0].plot(df['Min Gyroscope Z Running'],'ro',markersize=2)
axarr[2,1].plot(df['Min Reoriented Gyroscope Z Walking'],'bo',markersize=2)
axarr[2,1].plot(df['Min Reoriented Gyroscope Z Running'],'ro',markersize=2)

f.suptitle('Min Gyroscope')
plt.show()



features = ['Mean Reoriented Acceleration X Running', 'Mean Reoriented Acceleration X Walking',
            'Mean Reoriented Acceleration Z Running', 'Mean Reoriented Acceleration Z Walking',
            'Variance Reoriented Acceleration X Running', 'Variance Reoriented Acceleration X Walking',
            'Variance Reoriented Acceleration Y Running', 'Variance Reoriented Acceleration Y Walking',
            'Variance Reoriented Acceleration Z Running', 'Variance Reoriented Acceleration Z Walking',
            'Variance Reoriented Gyroscope Y Running', 'Variance Reoriented Gyroscope Y Walking',
            'Max Reoriented Acceleration Y Running', 'Max Reoriented Acceleration Y Walking',
            'Max Reoriented Acceleration Z Running', 'Max Reoriented Acceleration Z Walking',
            'Max Gyroscope X Running', 'Max Gyroscope X Walking',
            'Min Reoriented Acceleration X Running', 'Min Reoriented Acceleration X Walking',
            'Min Reoriented Acceleration Z Running', 'Min Reoriented Acceleration Z Walking',
            'Min Reoriented Gyroscope X Running', 'Min Reoriented Gyroscope X Walking',
            'Min Reoriented Gyroscope Y Running', 'Min Reoriented Gyroscope Y Walking',
             'Min Reoriented Gyroscope Z Running', 'Min Reoriented Gyroscope Z Walking',]

'''