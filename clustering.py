import dataProcessing
import algorithms
import visualization

# reading the database
database = dataProcessing.readJson()
database = dataProcessing.transformCoordinate(database)

# choosing the stars with names
starsWithName = dataProcessing.chooseStarWithName(database)

# choosing the stars with brighness higher than 4.5
starsNeedClustering = dataProcessing.selectBrightness(starsWithName, 2.6)

# running K means for 1000 times with 20 centroids
standardKMeans = algorithms.Kmeans(starsNeedClustering,10)
#standardKMeans.randInitCentroid()
standardKMeans.decisiveInitCentroid()
#standardKMeans.runStandardKmeansWithIter(2000)
standardKMeans.runStandardKmeansWithoutIter()

# output the stars that belong to centroid 1
# cluster_1 = algorithms.getCluster(1, assignments)

visualization.visualize(standardKMeans.assignments)
#print len(assignments), len(cluster_1), cluster_1
# print centroids, assignments
