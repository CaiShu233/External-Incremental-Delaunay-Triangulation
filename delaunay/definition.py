import numpy as np
import matplotlib.pyplot as plt
from .incremental import *
class Delaunay:
	def __init__(self,points,sorted=False):
		if sorted:
			self.points=points
		else:
			self.points=points[np.lexsort((points[:, 1], points[:, 0]))]
		self.sorted=True
		self.create()
		
	def create(self):
		self.L_ch_i,self.D_tri=incremental_sorted(self.points)
		
		
	def show(self,ax1 = plt.gca()):
		for key1,key2 in self.D_tri:
			if key1>key2:
				ax1.plot([self.points[key1][0],self.points[key2][0]],[self.points[key1][1],self.points[key2][1]],
				# color = 'cyan',
				color = '#1f77b4',
				)
		