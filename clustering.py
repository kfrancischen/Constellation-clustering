import dataProcessing
import algorithms
import visualization
import argparse

# add parsers
parser = argparse.ArgumentParser()
parser.add_argument('-a','--algorithm',type = str, help = 'Choose the algorithm')
algorithm = parser.add_subparsers(help = 'algorithm choices')
kmeans_parser = algorithm.add_parser('k', help = 'number of clusters')
kmeans_parser.add_argument('K', type = int, help = 'input the number of clusters')
DBS_parser = algorithm.add_parser('m',help = 'not implemented yet')
args = parser.parse_args()


# reading the database
database = dataProcessing.readJson()
database = dataProcessing.transformCoordinate(database)

# choosing the stars with names
starsWithName = dataProcessing.chooseStarWithName(database)

# choosing the stars with brighness higher than 4.5
starsNeedClustering = dataProcessing.selectBrightness(starsWithName, 4.5)
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
elif args.algorithm == 'DBSCAN':
	print 'not implemented yet'


