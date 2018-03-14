# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\GoodsBook\ui\purchase_record.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1049, 453)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)
        self.comboBoxInputRecord = ExtendedComboBox(self.widget_2)
        self.comboBoxInputRecord.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxInputRecord.setFont(font)
        self.comboBoxInputRecord.setObjectName("comboBoxInputRecord")
        self.gridLayout_5.addWidget(self.comboBoxInputRecord, 1, 5, 1, 1)
        self.dateEditBeginInputRecord = CCustomDateEdit(self.widget_2)
        self.dateEditBeginInputRecord.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEditBeginInputRecord.setMaximumSize(QtCore.QSize(123, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditBeginInputRecord.setFont(font)
        self.dateEditBeginInputRecord.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditBeginInputRecord.setObjectName("dateEditBeginInputRecord")
        self.gridLayout_5.addWidget(self.dateEditBeginInputRecord, 1, 0, 1, 1)
        self.dateEditEndInputRecord = CCustomDateEdit(self.widget_2)
        self.dateEditEndInputRecord.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEditEndInputRecord.setMaximumSize(QtCore.QSize(123, 123))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditEndInputRecord.setFont(font)
        self.dateEditEndInputRecord.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditEndInputRecord.setObjectName("dateEditEndInputRecord")
        self.gridLayout_5.addWidget(self.dateEditEndInputRecord, 1, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 2, 1, 1)
        self.labelNum = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelNum.setFont(font)
        self.labelNum.setStyleSheet("color:rgb(0, 0, 255)")
        self.labelNum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNum.setObjectName("labelNum")
        self.gridLayout_5.addWidget(self.labelNum, 0, 7, 1, 1)
        self.pushButtonQueryInputRecord = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonQueryInputRecord.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButtonQueryInputRecord.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonQueryInputRecord.setFont(font)
        self.pushButtonQueryInputRecord.setObjectName("pushButtonQueryInputRecord")
        self.gridLayout_5.addWidget(self.pushButtonQueryInputRecord, 1, 6, 1, 1)
        self.labelAmount = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelAmount.setFont(font)
        self.labelAmount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelAmount.setStyleSheet("color:rgb(255, 0, 0)")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setObjectName("labelAmount")
        self.gridLayout_5.addWidget(self.labelAmount, 1, 7, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.tableWidgetInputRecord = QtWidgets.QTableWidget(Form)
        self.tableWidgetInputRecord.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetInputRecord.setRowCount(0)
        self.tableWidgetInputRecord.setColumnCount(0)
        self.tableWidgetInputRecord.setObjectName("tableWidgetInputRecord")
        self.tableWidgetInputRecord.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetInputRecord)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_14.setText(_translate("Form", "商品"))
        self.label_17.setText(_translate("Form", "开始日期"))
        self.label_18.setText(_translate("Form", "结束日期"))
        self.labelNum.setText(_translate("Form", "总进货数量:"))
        self.pushButtonQueryInputRecord.setText(_translate("Form", "查询"))
        self.labelAmount.setText(_translate("Form", "总进货金额:"))
        self.tableWidgetInputRecord.setSortingEnabled(True)

from lib.pubui import CCustomDateEdit, ExtendedComboBox