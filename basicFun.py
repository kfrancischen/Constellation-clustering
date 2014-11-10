from math import cos
from math import sin
from math import asin
import math

def getXCoor(theta, phi):
	'''
		This function will calculate the x coordinate for given theta and phi
	'''
	return cos(theta)*cos(phi)

def getYCoor(theta, phi):
	'''
		This function will calculate the y coordinate for given theta and phi
	'''
	return cos(theta)*sin(phi)

def getZCoor(theta, phi):
	'''
		This function will calculate the z coordinate for given theta and phi
	'''
	return sin(theta)

def getEuclideanDistance(list_1, list_2):
	'''
		This function will calculate the euclidean distance between two 3D points
	'''
	dist = 0
	for i in range(len(list_1)):
		dist += (list_1[i]-list_2[i])**2
	return math.sqrt(dist)

def getSphericalDistance(list_1, list_2):
	'''
		This function will calculate the spherical distance on two 3D points
	'''
	dist = getEuclideanDistance(list_1,list_2)
	return 2*asin(0.5*dist)

def cosDissimilarity(list_1, list_2):
	'''
			This function will calculate the cosine dissimilarity of two 3D points
	'''
	return 1 - (list_1[0] * list_2[0] + list_1[1] * list_2[1] + list_1[2] * list_2[2])

def getNorm(a_list):
	'''
		This function will calculate the norm of a 3D vector
	'''
	return math.sqrt(a_list[0]**2 + a_list[1]**2 + a_list[2]**2)

