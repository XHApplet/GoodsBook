# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\GoodsBook\my\mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1027, 474)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWidget.setWindowIcon(icon)
        MainWidget.setToolTip("")
        self.InputWidget = QtWidgets.QWidget()
        self.InputWidget.setEnabled(True)
        self.InputWidget.setObjectName("InputWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.InputWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(30, 20, 30, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonInput = QtWidgets.QPushButton(self.InputWidget)
        self.pushButtonInput.setEnabled(True)
        self.pushButtonInput.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.gridLayout.addWidget(self.pushButtonInput, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEditInputPrice = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputPrice.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputPrice.setInputMask("")
        self.lineEditInputPrice.setMaxLength(15)
        self.lineEditInputPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputPrice.setObjectName("lineEditInputPrice")
        self.gridLayout.addWidget(self.lineEditInputPrice, 2, 3, 1, 1)
        self.lineEditInputNum = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputNum.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputNum.setMaxLength(10)
        self.lineEditInputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputNum.setObjectName("lineEditInputNum")
        self.gridLayout.addWidget(self.lineEditInputNum, 2, 4, 1, 1)
        self.dateEditInput = CCustomDateEdit(self.InputWidget)
        self.dateEditInput.setMinimumSize(QtCore.QSize(0, 50))
        self.dateEditInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEditInput.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditInput.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEditInput.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditInput.setTime(QtCore.QTime(0, 0, 0))
        self.dateEditInput.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEditInput.setCalendarPopup(True)
        self.dateEditInput.setObjectName("dateEditInput")
        self.gridLayout.addWidget(self.dateEditInput, 2, 0, 1, 1)
        self.comboBoxInputGoods = ExtendedComboBox(self.InputWidget)
        self.comboBoxInputGoods.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputGoods.setFont(font)
        self.comboBoxInputGoods.setObjectName("comboBoxInputGoods")
        self.gridLayout.addWidget(self.comboBoxInputGoods, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditInputRemark = QtWidgets.QLineEdit(self.InputWidget)
        self.lineEditInputRemark.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputRemark.setObjectName("lineEditInputRemark")
        self.gridLayout.addWidget(self.lineEditInputRemark, 2, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.comboBoxInputType = ExtendedComboBox(self.InputWidget)
        self.comboBoxInputType.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputType.setFont(font)
        self.comboBoxInputType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxInputType.setObjectName("comboBoxInputType")
        self.gridLayout.addWidget(self.comboBoxInputType, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.InputTiplabel = QtWidgets.QLabel(self.InputWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InputTiplabel.setFont(font)
        self.InputTiplabel.setStyleSheet("color:rgb(255, 0, 0)")
        self.InputTiplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputTiplabel.setObjectName("InputTiplabel")
        self.gridLayout.addWidget(self.InputTiplabel, 0, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 2)
        self.gridLayout.setColumnMinimumWidth(2, 3)
        self.gridLayout.setColumnMinimumWidth(3, 4)
        self.gridLayout.setColumnMinimumWidth(4, 5)
        self.gridLayout.setColumnMinimumWidth(5, 6)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 2)
        self.gridLayout.setRowMinimumHeight(2, 3)
        self.gridLayout.setRowMinimumHeight(3, 4)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 6)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 3)
        self.gridLayout.setRowStretch(3, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWidget.addTab(self.InputWidget, "")
        self.OutputWidget = QtWidgets.QWidget()
        self.OutputWidget.setObjectName("OutputWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.OutputWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.comboBoxOutputBuyer = ExtendedComboBox(self.OutputWidget)
        self.comboBoxOutputBuyer.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBoxOutputBuyer.setObjectName("comboBoxOutputBuyer")
        self.gridLayout_2.addWidget(self.comboBoxOutputBuyer, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.comboBoxOutputGoods = ExtendedComboBox(self.OutputWidget)
        self.comboBoxOutputGoods.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBoxOutputGoods.setObjectName("comboBoxOutputGoods")
        self.gridLayout_2.addWidget(self.comboBoxOutputGoods, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 5, 1, 1)
        self.lineEditOutputRemark = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputRemark.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputRemark.setObjectName("lineEditOutputRemark")
        self.gridLayout_2.addWidget(self.lineEditOutputRemark, 2, 5, 1, 1)
        self.dateEditOutput = CCustomDateEdit(self.OutputWidget)
        self.dateEditOutput.setMinimumSize(QtCore.QSize(0, 50))
        self.dateEditOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditOutput.setCalendarPopup(True)
        self.dateEditOutput.setObjectName("dateEditOutput")
        self.gridLayout_2.addWidget(self.dateEditOutput, 2, 0, 1, 1)
        self.pushButtonOutput = QtWidgets.QPushButton(self.OutputWidget)
        self.pushButtonOutput.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonOutput.setObjectName("pushButtonOutput")
        self.gridLayout_2.addWidget(self.pushButtonOutput, 3, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 4, 1, 1)
        self.lineEditOutputNum = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputNum.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditOutputNum.setObjectName("lineEditOutputNum")
        self.gridLayout_2.addWidget(self.lineEditOutputNum, 2, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.OutputWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        self.lineEditOutputPrice = QtWidgets.QLineEdit(self.OutputWidget)
        self.lineEditOutputPrice.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOutputPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditOutputPrice.setObjectName("lineEditOutputPrice")
        self.gridLayout_2.addWidget(self.lineEditOutputPrice, 2, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 4)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnStretch(4, 2)
        self.gridLayout_2.setColumnStretch(5, 6)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWidget.addTab(self.OutputWidget, "")
        self.StockWidget = QtWidgets.QWidget()
        self.StockWidget.setObjectName("StockWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.StockWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetStock = QtWidgets.QTableWidget(self.StockWidget)
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
        self.verticalLayout_2.addWidget(self.tableWidgetStock)
        MainWidget.addTab(self.StockWidget, "")
        self.ProfitWidget = QtWidgets.QWidget()
        self.ProfitWidget.setObjectName("ProfitWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ProfitWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.ProfitWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonExport = QtWidgets.QPushButton(self.widget)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.horizontalLayout.addWidget(self.pushButtonExport)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.dateEditBegin = CCustomDateEdit(self.widget)
        self.dateEditBegin.setObjectName("dateEditBegin")
        self.horizontalLayout.addWidget(self.dateEditBegin)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.dateEditEnd = CCustomDateEdit(self.widget)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.horizontalLayout.addWidget(self.dateEditEnd)
        self.pushButtonQuery = QtWidgets.QPushButton(self.widget)
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.horizontalLayout.addWidget(self.pushButtonQuery)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 1)
        self.verticalLayout_3.addWidget(self.widget)
        self.tableWidgetProfile = QtWidgets.QTableWidget(self.ProfitWidget)
        self.tableWidgetProfile.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetProfile.setRowCount(0)
        self.tableWidgetProfile.setColumnCount(0)
        self.tableWidgetProfile.setObjectName("tableWidgetProfile")
        self.tableWidgetProfile.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidgetProfile)
        MainWidget.addTab(self.ProfitWidget, "")
        self.Import = QtWidgets.QWidget()
        self.Import.setObjectName("Import")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Import)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.Import)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBoxImportGoodsType = QtWidgets.QComboBox(self.frame)
        self.comboBoxImportGoodsType.setObjectName("comboBoxImportGoodsType")
        self.horizontalLayout_2.addWidget(self.comboBoxImportGoodsType)
        self.pushButtonImportGoods = QtWidgets.QPushButton(self.frame)
        self.pushButtonImportGoods.setStatusTip("")
        self.pushButtonImportGoods.setWhatsThis("")
        self.pushButtonImportGoods.setObjectName("pushButtonImportGoods")
        self.horizontalLayout_2.addWidget(self.pushButtonImportGoods)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButtonImportBuyer = QtWidgets.QPushButton(self.frame)
        self.pushButtonImportBuyer.setObjectName("pushButtonImportBuyer")
        self.horizontalLayout_2.addWidget(self.pushButtonImportBuyer)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.verticalLayout_4.addWidget(self.frame)
        self.textEditImport = QtWidgets.QTextEdit(self.Import)
        self.textEditImport.setObjectName("textEditImport")
        self.verticalLayout_4.addWidget(self.textEditImport)
        MainWidget.addTab(self.Import, "")
        self.InputRecord = QtWidgets.QWidget()
        self.InputRecord.setObjectName("InputRecord")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.InputRecord)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.InputRecord)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBoxInputRecord = ExtendedComboBox(self.widget_2)
        self.comboBoxInputRecord.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxInputRecord.setObjectName("comboBoxInputRecord")
        self.gridLayout_5.addWidget(self.comboBoxInputRecord, 1, 5, 1, 1)
        self.pushButtonExportInputRecord = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonExportInputRecord.setObjectName("pushButtonExportInputRecord")
        self.gridLayout_5.addWidget(self.pushButtonExportInputRecord, 0, 8, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 1, 7, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 5, 1, 1)
        self.labelInputRecordNum = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelInputRecordNum.setFont(font)
        self.labelInputRecordNum.setStyleSheet("color:rgb(255, 0, 0)")
        self.labelInputRecordNum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInputRecordNum.setObjectName("labelInputRecordNum")
        self.gridLayout_5.addWidget(self.labelInputRecordNum, 0, 7, 1, 1)
        self.dateEditEndInputRecord = CCustomDateEdit(self.widget_2)
        self.dateEditEndInputRecord.setMaximumSize(QtCore.QSize(123, 123))
        self.dateEditEndInputRecord.setObjectName("dateEditEndInputRecord")
        self.gridLayout_5.addWidget(self.dateEditEndInputRecord, 1, 2, 1, 1)
        self.dateEditBeginInputRecord = CCustomDateEdit(self.widget_2)
        self.dateEditBeginInputRecord.setMaximumSize(QtCore.QSize(123, 16777215))
        self.dateEditBeginInputRecord.setObjectName("dateEditBeginInputRecord")
        self.gridLayout_5.addWidget(self.dateEditBeginInputRecord, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 2, 1, 1)
        self.pushButtonQueryInputRecord = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonQueryInputRecord.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonQueryInputRecord.setObjectName("pushButtonQueryInputRecord")
        self.gridLayout_5.addWidget(self.pushButtonQueryInputRecord, 1, 6, 1, 1)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.tableWidgetInputRecord = QtWidgets.QTableWidget(self.InputRecord)
        self.tableWidgetInputRecord.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetInputRecord.setRowCount(0)
        self.tableWidgetInputRecord.setColumnCount(0)
        self.tableWidgetInputRecord.setObjectName("tableWidgetInputRecord")
        self.tableWidgetInputRecord.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableWidgetInputRecord)
        MainWidget.addTab(self.InputRecord, "")
        self.outputRecord = QtWidgets.QWidget()
        self.outputRecord.setObjectName("outputRecord")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.outputRecord)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.outputRecord)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonQueryOutputRecord = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonQueryOutputRecord.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonQueryOutputRecord.setObjectName("pushButtonQueryOutputRecord")
        self.gridLayout_6.addWidget(self.pushButtonQueryOutputRecord, 1, 7, 1, 1)
        self.dateEditBeginOutputRecord = CCustomDateEdit(self.widget_3)
        self.dateEditBeginOutputRecord.setMaximumSize(QtCore.QSize(123, 16777215))
        self.dateEditBeginOutputRecord.setObjectName("dateEditBeginOutputRecord")
        self.gridLayout_6.addWidget(self.dateEditBeginOutputRecord, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_3)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_3)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 0, 2, 1, 1)
        self.comboBoxOutputRecordGoods = ExtendedComboBox(self.widget_3)
        self.comboBoxOutputRecordGoods.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxOutputRecordGoods.setObjectName("comboBoxOutputRecordGoods")
        self.gridLayout_6.addWidget(self.comboBoxOutputRecordGoods, 1, 5, 1, 1)
        self.dateEditEndOutputRecord = CCustomDateEdit(self.widget_3)
        self.dateEditEndOutputRecord.setMaximumSize(QtCore.QSize(123, 123))
        self.dateEditEndOutputRecord.setObjectName("dateEditEndOutputRecord")
        self.gridLayout_6.addWidget(self.dateEditEndOutputRecord, 1, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_3)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 0, 5, 1, 1)
        self.comboBoxOutputRecordBuyer = ExtendedComboBox(self.widget_3)
        self.comboBoxOutputRecordBuyer.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxOutputRecordBuyer.setObjectName("comboBoxOutputRecordBuyer")
        self.gridLayout_6.addWidget(self.comboBoxOutputRecordBuyer, 1, 6, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget_3)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 0, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 8, 1, 1)
        self.labelOutputRecordProfile = QtWidgets.QLabel(self.widget_3)
        self.labelOutputRecordProfile.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelOutputRecordProfile.setFont(font)
        self.labelOutputRecordProfile.setAcceptDrops(False)
        self.labelOutputRecordProfile.setStyleSheet("color:rgb(255, 0, 0)")
        self.labelOutputRecordProfile.setText("")
        self.labelOutputRecordProfile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutputRecordProfile.setObjectName("labelOutputRecordProfile")
        self.gridLayout_6.addWidget(self.labelOutputRecordProfile, 1, 8, 1, 1)
        self.pushButtonExportOutputRecord = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonExportOutputRecord.setObjectName("pushButtonExportOutputRecord")
        self.gridLayout_6.addWidget(self.pushButtonExportOutputRecord, 1, 9, 1, 1)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.tableWidgetOutputRecord = QtWidgets.QTableWidget(self.outputRecord)
        self.tableWidgetOutputRecord.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetOutputRecord.setRowCount(0)
        self.tableWidgetOutputRecord.setColumnCount(0)
        self.tableWidgetOutputRecord.setObjectName("tableWidgetOutputRecord")
        self.tableWidgetOutputRecord.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tableWidgetOutputRecord)
        MainWidget.addTab(self.outputRecord, "")
        self.InfoWidget = QtWidgets.QWidget()
        self.InfoWidget.setObjectName("InfoWidget")
        self.textEdit = QtWidgets.QTextEdit(self.InfoWidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 120, 451, 251))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButtonQueryOutput = QtWidgets.QPushButton(self.InfoWidget)
        self.pushButtonQueryOutput.setGeometry(QtCore.QRect(420, 60, 151, 41))
        self.pushButtonQueryOutput.setObjectName("pushButtonQueryOutput")
        self.pushButtonQueryInput = QtWidgets.QPushButton(self.InfoWidget)
        self.pushButtonQueryInput.setGeometry(QtCore.QRect(180, 60, 161, 41))
        self.pushButtonQueryInput.setObjectName("pushButtonQueryInput")
        MainWidget.addTab(self.InfoWidget, "")

        self.retranslateUi(MainWidget)
        MainWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)
        MainWidget.setTabOrder(self.comboBoxOutputGoods, self.comboBoxOutputBuyer)
        MainWidget.setTabOrder(self.comboBoxOutputBuyer, self.lineEditOutputPrice)
        MainWidget.setTabOrder(self.lineEditOutputPrice, self.lineEditOutputNum)
        MainWidget.setTabOrder(self.lineEditOutputNum, self.lineEditOutputRemark)
        MainWidget.setTabOrder(self.lineEditOutputRemark, self.pushButtonOutput)
        MainWidget.setTabOrder(self.pushButtonOutput, self.dateEditOutput)
        MainWidget.setTabOrder(self.dateEditOutput, self.comboBoxInputType)
        MainWidget.setTabOrder(self.comboBoxInputType, self.comboBoxInputGoods)
        MainWidget.setTabOrder(self.comboBoxInputGoods, self.lineEditInputPrice)
        MainWidget.setTabOrder(self.lineEditInputPrice, self.lineEditInputNum)
        MainWidget.setTabOrder(self.lineEditInputNum, self.lineEditInputRemark)
        MainWidget.setTabOrder(self.lineEditInputRemark, self.pushButtonInput)
        MainWidget.setTabOrder(self.pushButtonInput, self.dateEditInput)
        MainWidget.setTabOrder(self.dateEditInput, self.tableWidgetStock)
        MainWidget.setTabOrder(self.tableWidgetStock, self.dateEditBegin)
        MainWidget.setTabOrder(self.dateEditBegin, self.dateEditEnd)
        MainWidget.setTabOrder(self.dateEditEnd, self.pushButtonQuery)
        MainWidget.setTabOrder(self.pushButtonQuery, self.tableWidgetProfile)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "商品出入统计--肖豪"))
        self.pushButtonInput.setText(_translate("MainWidget", "确认进货"))
        self.dateEditInput.setDisplayFormat(_translate("MainWidget", "yyyy/M/d"))
        self.label_3.setText(_translate("MainWidget", "价格"))
        self.label.setText(_translate("MainWidget", "日期"))
        self.label_5.setText(_translate("MainWidget", "备注"))
        self.label_2.setText(_translate("MainWidget", "商品"))
        self.label_13.setText(_translate("MainWidget", "类别"))
        self.label_4.setText(_translate("MainWidget", "数量"))
        self.InputTiplabel.setText(_translate("MainWidget", "注意:新商品录入"))
        MainWidget.setTabText(MainWidget.indexOf(self.InputWidget), _translate("MainWidget", "进货"))
        self.label_6.setText(_translate("MainWidget", "日期"))
        self.label_8.setText(_translate("MainWidget", "买家"))
        self.label_7.setText(_translate("MainWidget", "商品"))
        self.label_11.setText(_translate("MainWidget", "备注"))
        self.pushButtonOutput.setText(_translate("MainWidget", "确认出货"))
        self.label_9.setText(_translate("MainWidget", "数量"))
        self.label_10.setText(_translate("MainWidget", "价格"))
        MainWidget.setTabText(MainWidget.indexOf(self.OutputWidget), _translate("MainWidget", "出货"))
        self.tableWidgetStock.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.StockWidget), _translate("MainWidget", "库存"))
        self.pushButtonExport.setText(_translate("MainWidget", "导出到表格"))
        self.label_15.setText(_translate("MainWidget", "开始日期:"))
        self.label_16.setText(_translate("MainWidget", "结束日期:"))
        self.pushButtonQuery.setText(_translate("MainWidget", "查询"))
        self.tableWidgetProfile.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.ProfitWidget), _translate("MainWidget", "总利润"))
        self.pushButtonImportGoods.setToolTip(_translate("MainWidget", "选择某类商品，批量导入"))
        self.pushButtonImportGoods.setText(_translate("MainWidget", "批量导入商品"))
        self.pushButtonImportBuyer.setText(_translate("MainWidget", "批量导入买家"))
        self.label_12.setText(_translate("MainWidget", "说明：批量导入数据，每行为一条数据"))
        MainWidget.setTabText(MainWidget.indexOf(self.Import), _translate("MainWidget", "导入"))
        self.pushButtonExportInputRecord.setText(_translate("MainWidget", "导出到表格"))
        self.label_17.setText(_translate("MainWidget", "开始日期"))
        self.label_14.setText(_translate("MainWidget", "商品"))
        self.labelInputRecordNum.setText(_translate("MainWidget", "总进货数:"))
        self.label_18.setText(_translate("MainWidget", "结束日期"))
        self.pushButtonQueryInputRecord.setText(_translate("MainWidget", "查询"))
        self.tableWidgetInputRecord.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.InputRecord), _translate("MainWidget", "进货记录"))
        self.pushButtonQueryOutputRecord.setText(_translate("MainWidget", "查询"))
        self.label_22.setText(_translate("MainWidget", "开始日期"))
        self.label_23.setText(_translate("MainWidget", "结束日期"))
        self.label_24.setText(_translate("MainWidget", "商品"))
        self.label_26.setText(_translate("MainWidget", "买家"))
        self.pushButtonExportOutputRecord.setText(_translate("MainWidget", "导出到表格"))
        self.tableWidgetOutputRecord.setSortingEnabled(True)
        MainWidget.setTabText(MainWidget.indexOf(self.outputRecord), _translate("MainWidget", "出货记录"))
        self.textEdit.setHtml(_translate("MainWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本：1.0.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">作者：肖豪</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">日期：2018.2.10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">说明：用于管理日常进出货</p></body></html>"))
        self.pushButtonQueryOutput.setText(_translate("MainWidget", "查看出货记录"))
        self.pushButtonQueryInput.setText(_translate("MainWidget", "查看进货记录"))
        MainWidget.setTabText(MainWidget.indexOf(self.InfoWidget), _translate("MainWidget", "说明"))

from lib.pubui import CCustomDateEdit, ExtendedComboBox