from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import*
from GUI import *
import sys
import dataProcessing
import algorithms
import basicFun
import visualization
import os
import numpy

# this class is for the user interface of the software
class clusteringApplication(QWidget):
	
	def __init__(self):
		'''
			Initializing the ui
		'''
		super(clusteringApplication, self).__init__()
		
		self.ui = Ui_Widget()
		self.ui.setupUi(self)
		self.algorithmList = ['','K-means','DBSCAN','Hierachical','Hierachical_2','Spectral', 'Affinity']
		self.database = dataProcessing.readJson()
		self.database = dataProcessing.transformCoordinate(self.database)
		self.starsWithName = dataProcessing.chooseStarWithName(self.database)	
		self.assignments = []

	def addItemToAlgorithmbox(self):
		'''
			add algorithms to the combobox
		'''
		self.ui.algorithmBox.addItems(self.algorithmList)
		self.ui.algorithmBox.activated.connect(self._setParameterTable)
		return

	def addContentsToParameterTable(self):
		'''
			add contents to the parameters table
		'''
		self.ui.parameterWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Parameter'))
		self.ui.parameterWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Value'))
		self.ui.parameterWidget.verticalHeader().setVisible(False)
		self.ui.parameterWidget.horizontalHeader().setStretchLastSection(True)
		self.ui.parameterWidget.resizeColumnsToContents()
		self.ui.parameterWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
		return

	def addReadOnlyToClusteringResults(self):
		'''
			add constraints to the plain text edit
		'''
		#self.ui.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ui.clusteringResults.setReadOnly(True)

	def addActionToRunButton(self):
		'''
			add action to the run button
		'''
		self.ui.runButton.clicked.connect(self._run_algorithms)
		return

	def addActionToVisualButtom(self):
		'''
			add action to the visualizing button
		'''
		self.ui.visualButton.clicked.connect(self._visualization)
		return

	def addActionToSaveButton(self):
		'''
			add action to the save button
		'''
		self.ui.saveButton.clicked.connect(self._savedata)
		return

	def addActionToClearButton(self):
		'''
			add action to the clear button'
		'''
		self.ui.clearButton.clicked.connect(self._clearAll)
		return	

	def _setParameterTable(self):
		'''
			the action of changing parameter table contents according to the combobox
		'''
		if self.ui.algorithmBox.currentText() == 'K-means':
		 	'''
		 		Set up kmeans
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('K'))	

		elif self.ui.algorithmBox.currentText() == 'DBSCAN':
			'''
				set up DBSCAN
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('Eps'))
			self.ui.parameterWidget.setItem(2,0, QTableWidgetItem('minDist'))

		elif self.ui.algorithmBox.currentText() == 'Hierachical':
			'''
				set up hierachical clustering
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('n_cluster'))

		elif self.ui.algorithmBox.currentText() == 'Hierachical_2':
			'''
				set up hierachical cluster_2
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))

		elif self.ui.algorithmBox.currentText() == 'Spectral':
			'''
				set up spectral clustering
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('n_cluster'))

		elif self.ui.algorithmBox.currentText() == 'Affinity':
			'''
				set up affinity propagation
			'''
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('damping'))
			self.ui.parameterWidget.setItem(2,0, QTableWidgetItem('max_iter'))

	def _clearAll(self):
		'''
			the action of clear button
		'''
		self.ui.algorithmBox.setCurrentIndex(0)
		self.ui.parameterWidget.clearContents()
		self.ui.clusteringResults.clear()
		return

	def _visualization(self): 
		'''
			the action of visualizing button
		'''
		if self.ui.algorithmBox.currentText() != 'Hierachical_2':

			visualization.visualize(self.assignments)	
		else:
			visualization.drawDendrogram(self.linkMatrix)

		return

	def _savedata(self):
		'''
			the action of saving data
		'''
		filename = QFileDialog.getSaveFileName(self, 'Save File',os.path.expanduser('~'), 'plain text file (*.txt *.dat)')
		try:
			fname = open(filename[0], 'w')
			filedata = str(self.ui.clusteringResults.toPlainText())
			fname.write(filedata)
			fname.close()
		except:
			QMessageBox.information(self, 'Warning!', 'Data not saved!', QMessageBox.Ok)
		return


	def _run_algorithms(self):
		'''
			The action of run button
		'''
		if self.ui.algorithmBox.currentText() == 'K-means':
		 	# if running K-means algorithm

			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			K = int(self.ui.parameterWidget.item(1,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th) 
			logScore = 0
			standardKmeans = algorithms.Kmeans(starsNeedClustering, K)
			standardKmeans.randInitCentroid()
			standardKmeans.runStandardKmeansWithoutIter()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. '+ str(K)+ ' Clusters found!\n\n# Press "visualizing" to see the 3D results.\n\n# Clusters are shown below.\n')
			self.ui.clusteringResults.appendPlainText('# The overall cosine dissimilarity is ' + str(standardKmeans.getDissimilarity()))
			for i in range(K):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster '+str(i+1)+':\n')
				cluster = standardKmeans.getCluster(i)
				names = []
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightness] ' + str(cluster[idx]['brightness']))
					names.append(cluster[idx]['name'][-3:])
				if names != []:
					logScore += numpy.log(len(list(set(names))))
			self.ui.clusteringResults.appendPlainText('\nThe total log Score is '+str(logScore))
			self.assignments = standardKmeans.assignments

		elif self.ui.algorithmBox.currentText() == 'DBSCAN':
			# if running DBSCAN algorithm

			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			Eps = float(self.ui.parameterWidget.item(1,1).text())
			minDist = int(self.ui.parameterWidget.item(2,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			logScore = 0
			standardDBS = algorithms.densityBasedClustering(starsNeedClustering, Eps, minDist) 
			standardDBS.runDBA()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. '+ str(standardDBS.getNumOfClusters())+ ' Clusters found!\n\n# Press "visualizing" to see the 3D results.\n\n# Clusters are shown below.\n')
			noise = standardDBS.getNoise()
			self.ui.clusteringResults.appendPlainText('\n**************************************')
			self.ui.clusteringResults.appendPlainText('Stars that are detected as noises:\n')
			# output noise
			for idx in range(len(noise)):
				self.ui.clusteringResults.appendPlainText('[name] '+noise[idx]['name']+',   [Brightness] ' + str(noise[idx]['brightness']))
			# output clusters
			for i in range(standardDBS.numOfClusters):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster '+str(i+1)+':\n')
				cluster = standardDBS.getCluster(i)
				names = []
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightness] ' + str(cluster[idx]['brightness']))
					names.append(cluster[idx]['name'][-3:])
				if names != []:
					logScore += numpy.log(len(list(set(names))))
	#		self.ui.clusteringResults.appendPlainText('\nThe total log Score is '+str(logScore))
			self.assignments = standardDBS.assignments

		elif self.ui.algorithmBox.currentText() == 'Hierachical':
			# if running Hierarchical clustering

			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			n_cluster = int(self.ui.parameterWidget.item(1,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			logScore = 0
			standardHC = algorithms.aggolomerativeClustering(starsNeedClustering, n_cluster)
			standardHC.runHierachicalClustering()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. '+ str(n_cluster)+ ' Clusters found!\n\n# Press "visualizing" to see the 3D results.\n\n# Clusters are shown below.\n')
			for i in range(n_cluster):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster '+str(i+1)+':\n')
				cluster = standardHC.getCluster(i)
				names = []
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightness] ' + str(cluster[idx]['brightness']))
					names.append(cluster[idx]['name'][-3:])
				if names != []:
					logScore += numpy.log(len(list(set(names))))
			self.ui.clusteringResults.appendPlainText('\nThe total log Score is '+str(logScore))
			self.assignments = standardHC.assignments

		elif self.ui.algorithmBox.currentText() == 'Hierachical_2':
			# if running Hierarchical clustering_2	
			
			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			HC_2 = algorithms.hierarchicalClustering(starsNeedClustering)
			HC_2.runHC_Version_2()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. \n\n# Press "visualizing" to see the hierarchical trees.\n')
			self.linkMatrix = HC_2.linkMatrix;
				

		elif self.ui.algorithmBox.currentText() == 'Spectral':
			# if running spectral clustering

			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			n_cluster = int(self.ui.parameterWidget.item(1,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			logScore = 0
			standardSpectralClustering = algorithms.spectralClustering(starsNeedClustering, n_cluster)
			standardSpectralClustering.runSpectralClustering()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. '+ str(n_cluster)+ ' Clusters found!\n\n# Press "visualizing" to see the 3D results.\n\n# Clusters are shown below.\n')
			for i in range(n_cluster):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster '+str(i+1)+':\n')
				cluster = standardSpectralClustering.getCluster(i)
				names = []
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightness] ' + str(cluster[idx]['brightness']))
					names.append(cluster[idx]['name'][-3:])
				if names != []:
					logScore += numpy.log(len(list(set(names))))
			self.ui.clusteringResults.appendPlainText('\nThe total log Score is '+str(logScore))
			self.assignments = standardSpectralClustering.assignments

		elif self.ui.algorithmBox.currentText() == 'Affinity':
			# if running affinity propagation

			bright_th = float(self.ui.parameterWidget.item(0,1).text())
			damping = float(self.ui.parameterWidget.item(1,1).text())
			max_iter = int(self.ui.parameterWidget.item(2,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			logScore = 0
			standardAP = algorithms.affinityPropagation(starsNeedClustering, damping, max_iter)
			standardAP.runAffinityPropagation()
			self.ui.clusteringResults.setPlainText('# Algorithm finised. '+ str(standardAP.getNumOfClusters())+ ' Clusters found!\n\n# Press "visualizing" to see the 3D results.\n\n# Clusters are shown below.\n')
			self.ui.clusteringResults.appendPlainText('# The overall cosine dissimilarity is ' + str(standardAP.getDissimilarity()))
			centers = standardAP.getCenters()
			for i in range(standardAP.getNumOfClusters()):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster '+str(i+1)+':\n')
				self.ui.clusteringResults.appendPlainText('The center of this cluster: ' + str(centers[i]['name'])+'\n')
				cluster = standardAP.getCluster(i)
				names = []
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightness] ' + str(cluster[idx]['brightness']))
					names.append(cluster[idx]['name'][-3:])
				if names != []:
					logScore += numpy.log(len(list(set(names))))
		#	self.ui.clusteringResults.appendPlainText('\nThe total log Score is '+str(logScore))
			self.assignments = standardAP.assignments
			
			
		return

# create instances
app = QApplication(sys.argv)
interface = clusteringApplication()
interface.addItemToAlgorithmbox()
interface.addActionToRunButton()
interface.addContentsToParameterTable()
interface.addReadOnlyToClusteringResults()
interface.addActionToClearButton()
interface.addActionToSaveButton()
interface.addActionToVisualButtom()
interface.show()
sys.exit(app.exec_())
