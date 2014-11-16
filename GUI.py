# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sat Nov 15 22:10:59 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.setFixedSize(1113, 800)
        self.resultView = QtWidgets.QGraphicsView(Widget)
        self.resultView.setGeometry(QtCore.QRect(370, 60, 671, 611))
        self.resultView.setObjectName("resultView")
        self.algorithmBox = QtWidgets.QComboBox(Widget)
        self.algorithmBox.setGeometry(QtCore.QRect(90, 110, 191, 51))
        self.algorithmBox.setObjectName("algorithmBox")
        self.parametersView = QtWidgets.QTableView(Widget)
        self.parametersView.setGeometry(QtCore.QRect(30, 180, 301, 491))
        self.parametersView.setObjectName("parametersView")
        self.clearButton = QtWidgets.QPushButton(Widget)
        self.clearButton.setGeometry(QtCore.QRect(640, 700, 161, 41))
        self.clearButton.setObjectName("clearButton")
        self.viewButton = QtWidgets.QPushButton(Widget)
        self.viewButton.setGeometry(QtCore.QRect(870, 700, 161, 41))
        self.viewButton.setObjectName("viewButton")
        self.runButton = QtWidgets.QPushButton(Widget)
        self.runButton.setGeometry(QtCore.QRect(90, 700, 161, 41))
        self.runButton.setObjectName("runButton")
        self.saveButton = QtWidgets.QPushButton(Widget)
        self.saveButton.setGeometry(QtCore.QRect(410, 700, 161, 41))
        self.saveButton.setObjectName("saveButton")
        self.algorithmLabel = QtWidgets.QLabel(Widget)
        self.algorithmLabel.setGeometry(QtCore.QRect(120, 70, 121, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.algorithmLabel.setFont(font)
        self.algorithmLabel.setObjectName("algorithmLabel")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Constellation Clustering"))
        self.clearButton.setText(_translate("Widget", "Clear"))
        self.viewButton.setText(_translate("Widget", "View Clusters"))
        self.runButton.setText(_translate("Widget", "Run"))
        self.saveButton.setText(_translate("Widget", "Save"))
        self.algorithmLabel.setText(_translate("Widget", "Algorithms"))

