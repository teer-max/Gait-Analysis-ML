from scipy.signal import butter, lfilter, filtfilt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def butter_bandpass(lowcut,highcut,fs,order=5):
    nyq = 0.5 *fs
    low = lowcut / nyq
    high = highcut/nyq
    b,a = butter (order, [low,high], btype='band')
    return b,a

def butter_bandpass_filter(data,lowcut,highcut,fs,order=5):
    b,a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y


df = pd.read_csv(r'C:\Users\TeerM\OneDrive\Desktop\Research\Codes\PycharmProjects\untitled\Oriented data.csv')

motion_data_columns = [7, 8, 9, 10, 11, 12]
filtered_columns = ['Filt Reor X Accelerometer', 'Filt Reor Y Accelerometer',
                    'Filt Reor Z Accelerometer', 'Filt Reor Gyroscope X',
                    'Filt Reor Gyroscope Y', 'Filt Reor Gyroscope Z']


filtered_df = pd.DataFrame(index=df.index, columns = filtered_columns)
filtered_df2 = pd.DataFrame(index=df.index, columns = filtered_columns)


j = 0
for i in motion_data_columns:
    flt = butter_bandpass_filter(df.iloc[:, i], .8, 12, 100, 3)
    filtered_df[filtered_df.columns.values[j]] = flt
    j = j + 1
k=0
for i in motion_data_columns:
    flt2 = butter_bandpass_filter(df.iloc[:, i], 2, 18, 100, 3)
    filtered_df2[filtered_df.columns.values[k]] = flt2
    k = k + 1


f, axarr = plt.subplots(3,2,sharey="row",sharex='col')

axarr[0, 0].plot(df.iloc[20150:20400, 7].values)
axarr[1, 0].plot(df.iloc[20150:20400, 8].values)
axarr[2, 0].plot(df.iloc[20150:20400, 9].values)
axarr[0, 1].plot(filtered_df.iloc[20150:20400, 0].values)
axarr[1, 1].plot(filtered_df.iloc[20150:20400, 1].values)
axarr[2, 1].plot(filtered_df.iloc[20150:20400, 2].values)
axarr[0, 0].set_title(str(df.columns[7]))
axarr[1, 0].set_title(str(df.columns[8]))
axarr[2, 0].set_title(str(df.columns[9]))
axarr[0, 1].set_title(str(filtered_df.columns[0]))
axarr[1, 1].set_title(str(filtered_df.columns[1]))
axarr[2, 1].set_title(str(filtered_df.columns[2]))
plt.show()

f, axarr = plt.subplots(3,2,sharey="row",sharex='col')

axarr[0, 0].plot(df.iloc[20050:20400, 10].values)
axarr[1, 0].plot(df.iloc[20050:20400, 11].values)
axarr[2, 0].plot(df.iloc[20050:20400, 12].values)
axarr[0, 1].plot(filtered_df2.iloc[20050:20400, 3].values)
axarr[1, 1].plot(filtered_df2.iloc[20050:20400, 4].values)
axarr[2, 1].plot(filtered_df2.iloc[20050:20400, 5].values)
axarr[0, 0].set_title(str(df.columns[10]))
axarr[1, 0].set_title(str(df.columns[11]))
axarr[2, 0].set_title(str(df.columns[12]))
axarr[0, 1].set_title(str(filtered_df2.columns[3]))
axarr[1, 1].set_title(str(filtered_df2.columns[4]))
axarr[2, 1].set_title(str(filtered_df2.columns[5]))
plt.show()

