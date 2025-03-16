import numpy as np
import matplotlib.pyplot as plt
import delaunay as dt

N = 100
array = np.random.rand(N,2)

T = dt.Delaunay(array)

print(T.points)
T.show()
plt.show()

# # validate
# import matplotlib as mpl
# print(array)
# T2 = mpl.tri.Triangulation(array[:,0],array[:,1])
# plt.triplot(T2)
# plt.show()

# # compare

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# T.show(ax1)
# ax1.set_title('External Incremental Delaunay')

# tri = mpl.tri.Triangulation(array[:,0], array[:,1])
# ax2.triplot(tri)
# ax2.set_title('Matplotlib Triangulation')

# plt.show()