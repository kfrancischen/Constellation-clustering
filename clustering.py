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

'''
	Running Hierarchical Clustering
	python clustering.py -a HC n [the n value]
'''
HC_parser = algorithm.add_parser('n', help = 'the number of clusters in Hierarchical Clustering')
HC_parser.add_argument('N', type = int, help = 'the value of n')

'''
	Running Hierachical to get the dendrogram
	python clustering.py -a HC_2
'''
HC_2_parser = algorithm.add_parser('default', help = 'no input arguments')
HC_2_parser.add_argument('n', type = int, help = 'the second HC algorithm')

'''
	Running Spectral Clustering
	python clustering.py -a spectral n [the n value]
'''
spectral_parser = algorithm.add_parser('n', help = 'the number of clusters in spectral clustering')
spectral_parser.add_argument('N', type = int, help = 'the value of n')
'''
	Running affinity propagation
	python clustering.py -a affinity d [the damping value] mi [value of max_iter]
'''
damping_parser = algorithm.add_parser('d', help = 'the damping factor')
damping_parser.add_argument('D', type = float, help ='the value of d')
MI = damping_parser.add_subparsers(help = 'the mi parser')
mi_parser = MI.add_parser('mi', help = 'the max_iter')
mi_parser.add_argument('MI', type = int, help = 'the value of mi')
'''
	adding all the parsers
'''
args = parser.parse_args()


# reading the database
database = dataProcessing.readJson()
database = dataProcessing.transformCoordinate(database)

# choosing the stars with names
starsWithName = dataProcessing.chooseStarWithName(database)

# choosing the stars with brighness higher than 4.5
starsNeedClustering = dataProcessing.selectBrightness(starsWithName, 4.6)

# get all the constellation names among the selected stars
constellationNames = dataProcessing.getConstellationNames(starsNeedClustering)

#print constellationNames, len(constellationNames)
#print len(starsNeedClustering)
# if the user runs kmeans 
if args.algorithm == 'Kmeans':
	K = args.K
	# running K means for 1000 times with 20 centroids
	standardKMeans = algorithms.Kmeans(starsNeedClustering,K)
	standardKMeans.randInitCentroid()
	#standardKMeans.decisiveInitCentroid()
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
	#print Eps, minDist, len(starsNeedClustering)
	standardDBS = algorithms.densityBasedClustering(starsNeedClustering, Eps, minDist) 
	standardDBS.runDBA()
	#print standardDBS.getNumOfClusters()
	noise = standardDBS.getNoise()
	#print 'Number of noise stars: ', len(noise)
	visualization.visualize(standardDBS.assignments)

# if the user runs Hierachical Clustering
elif args.algorithm == 'HC':
	n_cluster = args.N
	standardHC = algorithms.aggolomerativeClustering(starsNeedClustering, n_cluster)
	standardHC.runHierachicalClustering()
	#visualization.visualize(standardHC.assignments)

# if the user runs Hierachical Clustering_2
elif args.algorithm == 'HC_2':
	HC_version_2 = algorithms.hierarchicalClustering(starsNeedClustering)
	HC_version_2.runHC_Version_2()
	visualization.drawDendrogram(HC_version_2.linkMatrix)

# if the user runs spectral clustering
elif args.algorithm == 'spectral':
	n_cluster = args.N
	standardSpectralClustering = algorithms.spectralClustering(starsNeedClustering, n_cluster)
	standardSpectralClustering.runSpectralClustering()
	visualization.visualize(standardSpectralClustering.assignments)

# if the user runs affinity propagation
elif args.algorithm == 'affinity':
	damping = args.D
	max_iter = args.MI
	standardAP = algorithms.affinityPropagation(starsNeedClustering, damping, max_iter)
	standardAP.runAffinityPropagation()
	visualization.visualize(standardAP.assignments)

# if no such algorithm
else:
	raise Exception('No Such Bult-in Algorithm')

