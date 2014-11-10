
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize(assignments):
	xs = []
	ys = []
	zs = []
	color = []
	for idx in range(len(assignments)):
		star = assignments[idx]
		xs.append(star['x_coor'])
		ys.append(star['y_coor'])
		zs.append(star['z_coor'])
		color.append(2*int(star['assignment'][-1]))
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')
	ax.scatter(xs,ys,zs, s = len(xs), c = color, marker='o')
	plt.show()
