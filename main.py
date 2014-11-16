from PyQt5.QtWidgets import QApplication, QWidget
from GUI import *
import sys

class clusteringApplication(QWidget):
	def __init__(self):
		super(clusteringApplication, self).__init__()
		
		self.ui = Ui_Widget()
		self.ui.setupUi(self)
		self.algorithmList = ['K-means','DBSCAN']
	def addItemToAlgorithmbox(self):
		self.ui.algorithmBox.addItems(self.algorithmList)
			
		return

	def addActionToRunButton(self):
		if str(self.ui.algorithmBox.currentText()) == 'K-means':
			self.ui.runButton.clicked.connect(self._run_Kmeans)
		elif str(self.ui.algorithmBox.currentText()) == 'DBSCAN':
			self.ui.runButton.clicked.connect(self._run_DBSCAN)
		return
	def addActionToSaveButton(self):

		return
	def addActionToClearButton(self):
		return

	def _run_Kmeans(self):
		print 'kmeans'
	def _run_DBSCAN(self):
		print 'DBSCAN'


app = QApplication(sys.argv)
interface = clusteringApplication()
interface.addItemToAlgorithmbox()
interface.addActionToRunButton()
interface.show()
sys.exit(app.exec_())
