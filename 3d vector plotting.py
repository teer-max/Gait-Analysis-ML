import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

p0 = [0.799319, -3.477045e-01, 0.490093]
p1 = [0.852512, 9.113778e-16, -0.522708]
p2 = [0.296422, 9.376042e-01, 0.181748]

origin = [1,1,1]
X, Y, Z = zip(origin,origin,origin)
U, V, W = zip(p0,p1,p2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio=0.01)
plt.show()