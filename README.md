# External-Incremental-Delaunay-Triangulation

Maybe the most easiest and clever way to construct Delaunay triangulation


## Introduction of Algorithm
### Step 1: sort the points
  assume the sorted points are \[P1, P2, P3, ..., Pn]
### Step 2: initial first triangle
  always be the \[P1, P2, P3], sometimes be the \[P1, P2, P3, ..., Pi]

### Step 3: keep increasing the point to the delaunay triangulation
  notice that the border of the delaunay trianglulation is convex hull
Find the upper tangent line and lower tangent line of convex hull
  notice that the point always out of the convex hull
update delaunay triangulation


## How to use

### Click the "Test.py" if you have python Library numpy and matplotlib
  You will get a result of delaunay triangulation

### The Algorithm is in './delaunay/incremental.py'
  You can check the source code of External-Incremental-Delaunay-Triangulation Algorithm

### You want use
  Very easy to understand
  '''python
import numpy as np
import matplotlib.pyplot as plt
import delaunay as dt

N = 100
array = np.random.rand(N,2)

T = dt.Delaunay(array)

print(T.points)
T.show()
plt.show()
  '''
