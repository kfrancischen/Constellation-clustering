import json
import math
import basicFun

inputFileName = 'database.json'

def readJson():
	'''
		This file will read in the json data base and return a list of dictionary about the database
	'''
	outputDict = {}
	inputJson = open(inputFileName)
	data = json.load(inputJson)
#	pprint(data)
	inputJson.close()
	return data

def transformCoordinate(data):
	'''
		This function will transform all the angles into pi unit
	'''
	for i in range(len(data)):
		if data[i]['theta'] == None or data[i]['phi'] == None:
			continue
		data[i]['theta'] *= math.pi/180
		data[i]['phi'] *= math.pi/180
		data[i]['x_coor'] = basicFun.getXCoor(data[i]['theta'], data[i]['phi'])
		data[i]['y_coor'] = basicFun.getYCoor(data[i]['theta'], data[i]['phi'])
		data[i]['z_coor'] = basicFun.getZCoor(data[i]['theta'], data[i]['phi'])
	return data

def chooseStarWithName(data):
	'''
		This function will select all the stars with names and proper coordinates
	'''
	starWithName = []
	for index in range(len(data)):
		if data[index]['name'] == '' or 'NOVA' in data[index]['name'] or data[index]['brightness'] == None:
			continue
		starWithName.append(data[index])

	return starWithName


def selectBrightness(data, threshold, constellationName = None):
	'''
		This function will pick the stars with brightness larger than the threshold
		and with the third argument as the constellation name
		Without the third input, the function will not select star names
	'''
	selectedStars = []
	for index in range(len(data)):
		if constellationName == None:
			if data[index]['brightness'] <= threshold:
				selectedStars.append(data[index])
		else:
			if data[index]['brightness'] <= threshold and constellationName in data[index]['name']:
				selectedStars.append(data[index])
	return selectedStars

def selectNames(data, constellationName, threshold = None):
	'''
		This function has almost the same function as the previous one, but with different 
		argument input order. It will focus on the names of the stars.
	'''
	selectedStars = []
	for index in range(len(data)):
		if threshold == None:
			if constellationName in data[index]['name']:
				selectedStars.append(data[index])
		else:
			if constellationName in data[index]['name'] and data[index]['brightness'] <= threshold:
				selectedStars.append(data[index])
	return selectedStars

def getConstellationNames(data):
	'''
		This function will return all the constellation names
	'''
	constellationNames = {}
	for index in range(len(data)):
		constellationNames[data[index]['name'][-3:]] = 1
	return constellationNames

def getTrueLabel(data):
	'''
		This function will give the true label for all the data
	'''
	trueLabel = []
	constellationNames = getConstellationNames(data).keys()
	for i in range(len(data)):
		for j in range(len(constellationNames)):
			if data[i]['name'][-3:] == constellationNames[j]:
				trueLabel.append(j)
				continue
	return trueLabel

'''
database = readJson()
data = transformCorrdinate(database)
starWithName = chooseStarWithName(data)
selectedStars = selectBrightness(starWithName, 4.5)
selectedStars_2 = selectNames(starWithName, 'And')
print len(selectedStars)
print selectedStars_2
'''
