from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import *
from PyQt5.QtCore import*
from GUI import *
import sys
import dataProcessing
import algorithms
import visualization

class clusteringApplication(QWidget):
	def __init__(self):
		super(clusteringApplication, self).__init__()
		
		self.ui = Ui_Widget()
		self.ui.setupUi(self)
		self.algorithmList = ['','K-means','DBSCAN']
		self.database = dataProcessing.readJson()
		self.database = dataProcessing.transformCoordinate(self.database)
		self.starsWithName = dataProcessing.chooseStarWithName(self.database)	
		self.assignments = []

	def addItemToAlgorithmbox(self):
		self.ui.algorithmBox.addItems(self.algorithmList)
		self.ui.algorithmBox.activated.connect(self._setParameterTable)
		return

	def addContentsToParameterTable(self):
		self.ui.parameterWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Parameter'))
		self.ui.parameterWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Value'))
		self.ui.parameterWidget.verticalHeader().setVisible(False)
		self.ui.parameterWidget.horizontalHeader().setStretchLastSection(True)
		self.ui.parameterWidget.resizeColumnsToContents()
		self.ui.parameterWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
		return
	def addReadOnlyToClusteringResults(self):
		#self.ui.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.ui.clusteringResults.setReadOnly(True)

	def addActionToRunButton(self):
		self.ui.runButton.clicked.connect(self._run_algorithms)
		return

	def addActionToVisualButtom(self):
		self.ui.visualButton.clicked.connect(self._visualization)
		return

	def addActionToSaveButton(self):
		return

	def addActionToClearButton(self):
		self.ui.clearButton.clicked.connect(self._clearAll)
		return	

	def _setParameterTable(self):

		if self.ui.algorithmBox.currentText() == 'K-means':
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('K'))	

		elif self.ui.algorithmBox.currentText() == 'DBSCAN':
			self.ui.parameterWidget.clearContents()
			self.ui.clusteringResults.clear()
			self.ui.parameterWidget.setItem(0,0, QTableWidgetItem('Bright_th'))
			self.ui.parameterWidget.setItem(1,0, QTableWidgetItem('Eps'))
			self.ui.parameterWidget.setItem(2,0, QTableWidgetItem('minDist'))
		return

	def _clearAll(self):
		self.ui.algorithmBox.setCurrentIndex(0)
		self.ui.parameterWidget.clearContents()
		self.ui.clusteringResults.clear()

	def _visualization(self):
		visualization.visualize(self.assignments)	

	def _run_algorithms(self):
		if self.ui.algorithmBox.currentText() == 'K-means':
			bright_th = self.ui.parameterWidget.item(0,1).text()
			K = int(self.ui.parameterWidget.item(1,1).text())
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th) 
			standardKmeans = algorithms.Kmeans(starsNeedClustering, K)
			standardKmeans.randInitCentroid()
			standardKmeans.runStandardKmeansWithoutIter()
			self.ui.clusteringResults.setPlainText('Algorithm finised. '+ str(K)+ ' Clusters found!\n\nPress "visualizing" to see the 3D results.\n\nClusters are shown below.\n')
			for i in range(K):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				self.ui.clusteringResults.appendPlainText('Stars belong to cluster'+str(i+1)+':\n')
				cluster = standardKmeans.getCluster(i)
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightess] ' + str(cluster[idx]['brightness']))
			self.assignments = standardKmeans.assignments
#			visualization.visualize(standardKmeans.assignments)

		elif self.ui.algorithmBox.currentText() == 'DBSCAN':
			bright_th = self.ui.parameterWidget.item(0,1).text()
			Eps = self.ui.parameterWidget.item(1,1).text()
			minDist = int(self.ui.parameterWidget.item(2,1).text())
			#print Eps, minDist
			starsNeedClustering = dataProcessing.selectBrightness(self.starsWithName, bright_th)
			standardDBS = algorithms.densityBasedClustering(starsNeedClustering, Eps, minDist) 
			standardDBS.runDBA()
			self.ui.clusteringResults.setPlainText('Algorithm finised. '+ str(standardDBS.numOfClusters)+ ' Clusters found!\n\nPress "visualizing" to see the 3D results.\n\nClusters are shown below.\n')
			for i in range(standardDBS.numOfClusters):
				self.ui.clusteringResults.appendPlainText('\n**************************************')
				if i == 0:
					self.ui.clusteringResults.appendPlainText('Noised detected by DBSCAN are:\n')
				else:
					self.ui.clusteringResults.appendPlainText('Stars belong to cluster'+str(i+1)+':\n')
				cluster = standardDBS.getCluster(i)
				for idx in range(len(cluster)):
					self.ui.clusteringResults.appendPlainText('[name] '+cluster[idx]['name']+',   [Brightess] ' + str(cluster[idx]['brightness']))
#			visualization.visualize(standardDBS.assignments)
			self.assignments = standardDBS.assignments
			


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
