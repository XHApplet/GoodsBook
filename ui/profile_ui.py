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
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEditBegin = CCustomDateEdit(self.widget)
        self.dateEditBegin.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditBegin.setFont(font)
        self.dateEditBegin.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditBegin.setObjectName("dateEditBegin")
        self.gridLayout.addWidget(self.dateEditBegin, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.dateEditEnd = CCustomDateEdit(self.widget)
        self.dateEditEnd.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditEnd.setFont(font)
        self.dateEditEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.gridLayout.addWidget(self.dateEditEnd, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)
        self.pushButtonQuery = QtWidgets.QPushButton(self.widget)
        self.pushButtonQuery.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonQuery.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonQuery.setFont(font)
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.gridLayout.addWidget(self.pushButtonQuery, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
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
        self.label_15.setText(_translate("Form", "开始日期:"))
        self.label_16.setText(_translate("Form", "结束日期:"))
        self.pushButtonQuery.setText(_translate("Form", "查询"))
        self.tableWidgetProfile.setSortingEnabled(True)

from lib.pubui import CCustomDateEdit
