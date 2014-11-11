import dataProcessing
import algorithms
import visualization
import argparse

# add parsers
parser = argparse.ArgumentParser()
parser.add_argument('-a','--algorithm',type = str, help = 'Choose the algorithm')
algorithm = parser.add_subparsers(help = 'algorithm choices')

'''
	Running K means algorithm:
	python clustering.py -a Kmeans k [the k value]
'''
kmeans_parser = algorithm.add_parser('k', help = 'number of clusters')
kmeans_parser.add_argument('K', type = int, help = 'input the number of clusters')

'''
	Running DBSCAN:
	python clustering.py -a DBSCAN eps [the eps value] mindist [the mindist value]
'''
eps_parser = algorithm.add_parser('eps',help = 'the epsilon value of a cluster')
eps_parser.add_argument('Eps', type = float, help = 'the input epsilon')
min_dist = eps_parser.add_subparsers(help = 'the minimum distance')
minDist_parser = min_dist.add_parser('mindist', help = 'minimum distance for a reachable point')
minDist_parser.add_argument('minDist', type = int, help = 'the value of minimum distance')
args = parser.parse_args()


# reading the database
database = dataProcessing.readJson()
database = dataProcessing.transformCoordinate(database)

# choosing the stars with names
starsWithName = dataProcessing.chooseStarWithName(database)

# choosing the stars with brighness higher than 4.5
starsNeedClustering = dataProcessing.selectBrightness(starsWithName, 4.5)

# if the user runs kmeans
if args.algorithm == 'Kmeans':
	K = args.K
	# running K means for 1000 times with 20 centroids
	standardKMeans = algorithms.Kmeans(starsNeedClustering,K)
	#standardKMeans.randInitCentroid()
	standardKMeans.decisiveInitCentroid()
	#standardKMeans.runStandardKmeansWithIter(2000)
	standardKMeans.runStandardKmeansWithoutIter()

	# output the stars that belong to centroid 1
	# cluster_1 = algorithms.getCluster(1, assignments)

	visualization.visualize(standardKMeans.assignments)
	#print len(assignments), len(cluster_1), cluster_1
	# print centroids, assignments

# if the user runs DBSCAN
elif args.algorithm == 'DBSCAN':
	Eps = args.Eps
	minDist = args.minDist
	standardDBS = algorithms.densityBasedClustering(starsNeedClustering, Eps, minDist) 
	standardDBS.runDBA()
	print standardDBS.getNumOfClusters()
	visualization.visualize(standardDBS.assignments)
	


