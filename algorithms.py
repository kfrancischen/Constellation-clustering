'''
This file is for the algorithms in the clustering problem
'''
import math
import random
import copy
import basicFun

# algorithm 1: standard K-means algorithm

class Kmeans:
	'''
		This class will take in all the filtered data and perform K-means algorithm
	'''
	def __init__(self, stars, K, centroid = None):
		'''
			initializing the class
		'''
		self.K = K
		self.assignments = copy.deepcopy(stars)
		for idx in range(len(self.assignments)):
			self.assignments[idx]['assignment'] = 'centroid_1'
		if centroid == None:
		 	self.centroid = {}
			for i in range(K):
				key = 'centroid_' + str(i+1)
				self.centroid[key] = [0, 0, 0]
		else:
		  self.centroid = centroid

	def randInitCentroid(self):
		'''
			This function is for random initializing the centroid
		'''
		for i in range(self.K):
			key = 'centroid_' + str(i+1)
			theta = (random.random()-0.5) * math.pi
			phi = random.random() * 2 * math.pi
			self.centroid[key] = [basicFun.getXCoor(theta, phi), basicFun.getYCoor(theta, phi), basicFun.getZCoor(theta, phi)]
		return
	
	def decisiveInitCentroid(self):
		'''
			This function is for initializing centroid on existing stars
		'''
		chosenStars = random.sample(self.assignments, self.K)
		for i in range(self.K):
			key = 'centroid_' + str(i+1)
			self.centroid[key] = [chosenStars[i]['x_coor'], chosenStars[i]['y_coor'], chosenStars[i]['z_coor']]
		return
	
	def densityBasedInitCentroid(self):
		'''
			This function is for initializing centroid based on data density distribution
		'''
		return

	def getCluster(self,centroidIdx):
		'''
			This function is for post data processing.
			@centroid index: the index of the centroid, range from 1-K
			@return: stars in the index_th cluster
		'''
		key = 'centroid_' + str(centroidIdx)
		cluster = []
		for i in range(len(self.assignments)):
			if self.assignments[i]['assignment'] == key:
				cluster.append(self.assignments[i])
		return cluster

	def getDissimilarity(self):
		'''
			This function will return the dissimilarity of the centroids and the originial data
		'''
		dissimilarity = 0
		for idx in range(len(self.assignments)):
			star = self.assignments[idx]
			belong = star['assignment']
#			dissimilarity += basicFun.cosDissimilarity([star['x_coor'], star['y_coor'], star['z_coor']], \
#					[self.centroid[belong][0], self.centroid[belong][1], self.centroid[belong][2]])
			dissimilarity += basicFun.weightedCosDissimilarity([star['x_coor'], star['y_coor'], star['z_coor']], \
					[self.centroid[belong][0], self.centroid[belong][1], self.centroid[belong][2]])
		return dissimilarity
		return dissimilarity

	def runStandardKmeansWithIter(self, maxIter):
		'''
			function for standard K-means algorithm
			@maxIter: the maximum iteration that K means is going to run
		'''
		# performing K-means
		count = 1
		while count <= maxIter:
			count += 1
			# step 1: updating the assignments
			for star in self.assignments:
				dist = []
				x = star['x_coor']
				y = star['y_coor']
				z = star['z_coor']
				for i in range(len(self.centroid)):
					key = 'centroid_' + str(i+1)
					x_center = self.centroid[key][0]
					y_center = self.centroid[key][1]
					z_center = self.centroid[key][2]
#					dist.append(basicFun.cosDissimilarity([x,y,z], [x_center, y_center, z_center]))
					dist.append(basicFun.weightedCosDissimilarity([x,y,z], [x_center, y_center, z_center], star['brightness']))
				idx = dist.index(min(dist))
				star['assignment'] = 'centroid_' + str(idx+1)

			# step 2: updating the centroids
			for i in range(len(self.centroid)):
				key = 'centroid_' + str(i+1)
				self.centroid[key]=[0,0,0]
				for star in self.assignments:
					if star['assignment'] == key:
						self.centroid[key][0] += star['x_coor']
						self.centroid[key][1] += star['y_coor']
						self.centroid[key][2] += star['z_coor']
				norm = basicFun.getNorm(self.centroid[key])
				if norm == 0:
					continue
				self.centroid[key][0] /= norm
				self.centroid[key][1] /= norm
				self.centroid[key][2] /= norm
		return 

	def runStandardKmeansWithoutIter(self):
		'''
			function for K-means algorithm without maximum iteration. It will automatically stop at convergence
		'''
		CONTINUE_FLAG = True
		while CONTINUE_FLAG:
		 	CONTINUE_FLAG = False
		 	preCentroid = copy.deepcopy(self.centroid)

			# step 1: updating the assignments
			for star in self.assignments:
				dist = []
				x = star['x_coor']
				y = star['y_coor']
				z = star['z_coor']
				for i in range(len(self.centroid)):
					key = 'centroid_' + str(i+1)
					x_center = self.centroid[key][0]
					y_center = self.centroid[key][1]
					z_center = self.centroid[key][2]
#					dist.append(basicFun.cosDissimilarity([x,y,z], [x_center, y_center, z_center]))
					dist.append(basicFun.weightedCosDissimilarity([x,y,z], [x_center, y_center, z_center], star['brightness']))
				idx = dist.index(min(dist))
				star['assignment'] = 'centroid_' + str(idx+1)
			
			# step 2: updating the centroids
			for i in range(len(self.centroid)):
				key = 'centroid_' + str(i+1)
				self.centroid[key]=[0,0,0]
				for star in self.assignments:
					if star['assignment'] == key:
						self.centroid[key][0] += star['x_coor']
						self.centroid[key][1] += star['y_coor']
						self.centroid[key][2] += star['z_coor']
				norm = basicFun.getNorm(self.centroid[key])
				if norm == 0:
					continue
				self.centroid[key][0] /= norm
				self.centroid[key][1] /= norm
				self.centroid[key][2] /= norm

			# step 3: update continue flag
			for i in range(len(self.centroid)):
				key = 'centroid_' + str(i+1)
				diff_x = preCentroid[key][0] - self.centroid[key][0]
				diff_y = preCentroid[key][1] - self.centroid[key][1]
				diff_z = preCentroid[key][2] - self.centroid[key][2]
				if basicFun.getNorm([diff_x, diff_y, diff_z]) >= 0.000001:
					CONTINUE_FLAG = True
					break
		return
		


# algorithm 2:
from sklearn.cluster import DBSCAN
from scipy.spatial import distance
import numpy
class densityBasedClustering:
	'''
		This class will take all the filtered data and perform DBSCAN
	'''
	def __init__(self, stars, Eps, minDist):
		self.assignments = copy.deepcopy(stars)
		self.Eps = Eps
		self.minDist = minDist
		self.coordinates = []
		self.numOfClusters = 0
		for i in range(len(self.assignments)):
			coordinate = [self.assignments[i]['x_coor'], self.assignments[i]['y_coor'], self.assignments[i]['z_coor']]
			self.coordinates.append(coordinate)

	def runDBA(self):
		distMatrix = distance.squareform(distance.pdist(self.coordinates, 'cosine'))
		db = DBSCAN(eps = self.Eps, min_samples = self.minDist).fit(distMatrix)
		belongs = db.labels_.tolist()
		print belongs
		for i in range(len(belongs)):
			self.assignments[i]['assignment'] = 'centroid_' + str(belongs[i]+1)
		self.numOfClusters = len(set(belongs)) - (1 if -1 in belongs else 0)

	def getNumOfClusters(self):
		return self.numOfClusters

	def getCluster(self, clusterIdx):
		cluster = []
		key = 'centroid' + str(clusterIdx+1)
		for i in range(len(self.assignments)):
			if self.assignments[i]['assignment'] == key:
				cluster.append(self.assignments[i])
		return cluster

	def getCoordinates(self):
		return self.coordinates
	
	def getNoise(self):
		noise = []
		for i in range(len(self.assignments)):
			if self.assignments[i]['assignment'] == 'centroid_-1':
				noise.append(self.assignments[i])
		return noise

		
# algorithm 3:
