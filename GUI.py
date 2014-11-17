# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Nov 16 22:44:38 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.setFixedSize(1113, 800)
        self.algorithmBox = QtWidgets.QComboBox(Widget)
        self.algorithmBox.setGeometry(QtCore.QRect(90, 110, 191, 51))
        self.algorithmBox.setObjectName("algorithmBox")
        self.clearButton = QtWidgets.QPushButton(Widget)
        self.clearButton.setGeometry(QtCore.QRect(860, 700, 161, 41))
        self.clearButton.setObjectName("clearButton")
        self.runButton = QtWidgets.QPushButton(Widget)
        self.runButton.setGeometry(QtCore.QRect(110, 700, 161, 41))
        self.runButton.setObjectName("runButton")
        self.saveButton = QtWidgets.QPushButton(Widget)
        self.saveButton.setGeometry(QtCore.QRect(650, 700, 161, 41))
        self.saveButton.setObjectName("saveButton")
        self.algorithmLabel = QtWidgets.QLabel(Widget)
        self.algorithmLabel.setGeometry(QtCore.QRect(120, 70, 121, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.algorithmLabel.setFont(font)
        self.algorithmLabel.setObjectName("algorithmLabel")
        self.parameterWidget = QtWidgets.QTableWidget(Widget)
        self.parameterWidget.setGeometry(QtCore.QRect(50, 190, 256, 481))
        self.parameterWidget.setObjectName("parameterWidget")
        self.parameterWidget.setColumnCount(2)
        self.parameterWidget.setRowCount(10)
        self.scrollArea = QtWidgets.QScrollArea(Widget)
        self.scrollArea.setGeometry(QtCore.QRect(400, 80, 631, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.clusteringResults = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.clusteringResults.setGeometry(QtCore.QRect(0, 0, 629, 579))
        self.clusteringResults.setObjectName("clusteringResults")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
	#self.scrollArea.setViewport(self.scrollAreaWidgetContents)
        self.visualButton = QtWidgets.QPushButton(Widget)
        self.visualButton.setGeometry(QtCore.QRect(420, 700, 161, 41))
        self.visualButton.setObjectName("visualButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Constellation Clustering"))
        self.clearButton.setText(_translate("Widget", "Clear"))
        self.runButton.setText(_translate("Widget", "Run"))
        self.saveButton.setText(_translate("Widget", "Save"))
        self.algorithmLabel.setText(_translate("Widget", "Algorithms"))
        self.visualButton.setText(_translate("Widget", "visualizing"))

