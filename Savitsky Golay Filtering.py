import scipy.signal._savitzky_golay as sg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv(r'C:\Users\TeerM\OneDrive\Desktop\Research\Codes\PycharmProjects\untitled\Oriented data.csv', index_col=0)

print(data.head())
for j in range(len(data.columns)):
    f,(ax1,ax2) = plt.subplots(1,2,sharey='row')
    ax2.plot(sg.savgol_filter(data.iloc[20500:21000,j],99,7))
    ax2.set_title(data.columns[j])
    ax1.plot(data.iloc[20500:21000,j])
    ax1.set_title(data.columns[j])
    plt.show()

