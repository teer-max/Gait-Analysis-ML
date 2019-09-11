import sklearn
from sklearn.pipeline import make_pipeline as MP
from sklearn.impute import SimpleImputer as Imp
from sklearn.neighbors import KNeighborsClassifier as KN
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle

# Import Data (using oriented data)
df2 = pd.read_csv('labeled feature matrix.csv')

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

feature_matrix1 = df2[features[:]].astype(float).values.tolist()
feature_matrix = df2[features[:]].astype(float).values.tolist()
feature_matrix = np.array(feature_matrix)
feature_matrix1 = np.array(feature_matrix1)
random.shuffle(feature_matrix)

X = feature_matrix1[:, :-1]
y = feature_matrix1[:, -1]

test_size = 0.2
train_data = X[:int(-test_size * len(feature_matrix))]
test_data = X[int(-test_size * len(feature_matrix)):]

train_label = y[:int(-test_size * len(feature_matrix))]
test_label = y[int(-test_size * len(feature_matrix)):]

#neigh = RadiusNeighborsClassifier(radius=1000.0, outlier_label=0)
#neigh.fit(X, y)

neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=1)
neigh.fit(train_data,train_label)

#pickle.dump(neigh, open('neighbors.pickle','wb'))
#neigh = pickle.load(open('neighbors.pickle','rb'))

print('Full Data Accuracy = ', str(neigh.score(X, y)))
predictions = neigh.predict(X)

plt.plot(predictions, 'ro', markersize=0.15)
plt.plot(X[:,1],'go',markersize=0.15)
# plt.plot(y, 'bo')
plt.show()

print('Training Data Accuracy = ', str(neigh.score(train_data, train_label)))
predictions = neigh.predict(train_data)
plt.plot(predictions, 'ro', markersize=0.15)
plt.plot(train_data[:,0],'go',markersize=0.15)
# plt.plot(train_label, 'bo')
plt.show()

print('Testing Data Accuracy = ', str(neigh.score(test_data, test_label)))
predictions = neigh.predict(test_data)
plt.plot(predictions, 'ro', markersize=0.15)
plt.plot(test_data[:,0],'go',markersize=0.15)
# plt.plot(test_label, 'bo')
plt.show()


