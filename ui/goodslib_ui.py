# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\GoodsBook\ui\goodslib.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 410)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetStock = QtWidgets.QTableWidget(Form)
        self.tableWidgetStock.setEnabled(True)
        self.tableWidgetStock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetStock.setAutoFillBackground(True)
        self.tableWidgetStock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidgetStock.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidgetStock.setLineWidth(1)
        self.tableWidgetStock.setMidLineWidth(0)
        self.tableWidgetStock.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetStock.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidgetStock.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetStock.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidgetStock.setRowCount(10)
        self.tableWidgetStock.setColumnCount(4)
        self.tableWidgetStock.setObjectName("tableWidgetStock")
        self.tableWidgetStock.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetStock.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetStock.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetStock)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidgetStock.setSortingEnabled(True)

