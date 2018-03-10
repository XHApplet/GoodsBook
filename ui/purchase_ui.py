# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\mycode\GoodsBook\ui\purchase.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1056, 506)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(30, 20, 30, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonInput = QtWidgets.QPushButton(Form)
        self.pushButtonInput.setEnabled(True)
        self.pushButtonInput.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.gridLayout.addWidget(self.pushButtonInput, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEditInputPrice = QtWidgets.QLineEdit(Form)
        self.lineEditInputPrice.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputPrice.setInputMask("")
        self.lineEditInputPrice.setMaxLength(15)
        self.lineEditInputPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputPrice.setObjectName("lineEditInputPrice")
        self.gridLayout.addWidget(self.lineEditInputPrice, 2, 3, 1, 1)
        self.lineEditInputNum = QtWidgets.QLineEdit(Form)
        self.lineEditInputNum.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputNum.setMaxLength(10)
        self.lineEditInputNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInputNum.setObjectName("lineEditInputNum")
        self.gridLayout.addWidget(self.lineEditInputNum, 2, 4, 1, 1)
        self.dateEditInput = CCustomDateEdit(Form)
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
        self.comboBoxInputGoods = ExtendedComboBox(Form)
        self.comboBoxInputGoods.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputGoods.setFont(font)
        self.comboBoxInputGoods.setObjectName("comboBoxInputGoods")
        self.gridLayout.addWidget(self.comboBoxInputGoods, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditInputRemark = QtWidgets.QLineEdit(Form)
        self.lineEditInputRemark.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditInputRemark.setObjectName("lineEditInputRemark")
        self.gridLayout.addWidget(self.lineEditInputRemark, 2, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.comboBoxInputType = ExtendedComboBox(Form)
        self.comboBoxInputType.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBoxInputType.setFont(font)
        self.comboBoxInputType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxInputType.setObjectName("comboBoxInputType")
        self.gridLayout.addWidget(self.comboBoxInputType, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.InputTiplabel = QtWidgets.QLabel(Form)
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
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonInput.setText(_translate("Form", "确认进货"))
        self.dateEditInput.setDisplayFormat(_translate("Form", "yyyy/M/d"))
        self.label_3.setText(_translate("Form", "价格"))
        self.label.setText(_translate("Form", "日期"))
        self.label_5.setText(_translate("Form", "备注"))
        self.label_2.setText(_translate("Form", "商品"))
        self.label_13.setText(_translate("Form", "类别"))
        self.label_4.setText(_translate("Form", "数量"))
        self.InputTiplabel.setText(_translate("Form", "注意:新商品录入"))

from lib.pubui import CCustomDateEdit, ExtendedComboBox
