# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Fri Nov 14 23:48:47 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1113, 800)
        self.resultView = QtWidgets.QGraphicsView(Widget)
        self.resultView.setGeometry(QtCore.QRect(370, 60, 671, 611))
        self.resultView.setObjectName("resultView")
        self.algorithmBox = QtWidgets.QComboBox(Widget)
        self.algorithmBox.setGeometry(QtCore.QRect(90, 110, 191, 51))
        self.algorithmBox.setObjectName("algorithmBox")
        self.parametersView = QtWidgets.QTableView(Widget)
        self.parametersView.setGeometry(QtCore.QRect(30, 180, 301, 491))
        self.parametersView.setObjectName("parametersView")
        self.clearBotton = QtWidgets.QPushButton(Widget)
        self.clearBotton.setGeometry(QtCore.QRect(640, 700, 161, 41))
        self.clearBotton.setObjectName("clearBotton")
        self.viewBotton = QtWidgets.QPushButton(Widget)
        self.viewBotton.setGeometry(QtCore.QRect(870, 700, 161, 41))
        self.viewBotton.setObjectName("viewBotton")
        self.runBotton = QtWidgets.QPushButton(Widget)
        self.runBotton.setGeometry(QtCore.QRect(90, 700, 161, 41))
        self.runBotton.setObjectName("runBotton")
        self.saveBotton = QtWidgets.QPushButton(Widget)
        self.saveBotton.setGeometry(QtCore.QRect(410, 700, 161, 41))
        self.saveBotton.setObjectName("saveBotton")
        self.algorithmLabel = QtWidgets.QLabel(Widget)
        self.algorithmLabel.setGeometry(QtCore.QRect(120, 70, 121, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.algorithmLabel.setFont(font)
        self.algorithmLabel.setObjectName("algorithmLabel")
        self.exitBotton = QtWidgets.QToolButton(Widget)
        self.exitBotton.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.exitBotton.setObjectName("exitBotton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.clearBotton.setText(_translate("Widget", "Clear"))
        self.viewBotton.setText(_translate("Widget", "View Clusters"))
        self.runBotton.setText(_translate("Widget", "Run"))
        self.saveBotton.setText(_translate("Widget", "Save"))
        self.algorithmLabel.setText(_translate("Widget", "Algorithms"))
        self.exitBotton.setText(_translate("Widget", "Exit"))

