# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\GoodsBook\ui\profile.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1055, 482)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.dateEditBegin = CCustomDateEdit(self.widget)
        self.dateEditBegin.setObjectName("dateEditBegin")
        self.gridLayout.addWidget(self.dateEditBegin, 1, 0, 1, 1)
        self.dateEditEnd = CCustomDateEdit(self.widget)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.gridLayout.addWidget(self.dateEditEnd, 1, 2, 1, 1)
        self.pushButtonQuery = QtWidgets.QPushButton(self.widget)
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.gridLayout.addWidget(self.pushButtonQuery, 1, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 3)
        self.gridLayout.setColumnStretch(3, 4)
        self.gridLayout.setColumnStretch(4, 5)
        self.gridLayout.setColumnStretch(5, 6)
        self.verticalLayout.addWidget(self.widget)
        self.tableWidgetProfile = QtWidgets.QTableWidget(Form)
        self.tableWidgetProfile.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetProfile.setRowCount(0)
        self.tableWidgetProfile.setColumnCount(0)
        self.tableWidgetProfile.setObjectName("tableWidgetProfile")
        self.tableWidgetProfile.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetProfile)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "结束日期:"))
        self.label_15.setText(_translate("Form", "开始日期:"))
        self.pushButtonQuery.setText(_translate("Form", "查询"))
        self.tableWidgetProfile.setSortingEnabled(True)

from lib.pubui import CCustomDateEdit
