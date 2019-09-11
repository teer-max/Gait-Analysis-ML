import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\TeerM\OneDrive\Desktop\Research\Codes\PycharmProjects\untitled\Oriented data.csv")

print(data.head())
print(data.columns)

xf = np.fft.rfftn(data.iloc[:,1:])

xf = np.fft.rfft(Sin+Sin2+Sin3)

plt.plot()
plt.show()