
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import scipy.cluster.hierarchy as hac

def visualize(assignments):
	xs = []
	ys = []
	zs = []
	size = []
	color = []
	for idx in range(len(assignments)):
		star = assignments[idx]
		xs.append(star['x_coor'])
		ys.append(star['y_coor'])
		zs.append(star['z_coor'])
		size.append(600/math.exp(star['brightness']))
		color.append(2*int(star['assignment'][-1]))
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')
	ax.scatter(xs,ys,zs,s = size, c = color, marker='o')
	ax.set_xlabel('X Axis')
	ax.set_ylabel('Y Axis')
	ax.set_zlabel('Z Axis')

	plt.show()

def drawDendrogram(linkMatrix):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	tree = hac.dendrogram(linkMatrix)
	ax.set_yticks([])
	plt.show()

