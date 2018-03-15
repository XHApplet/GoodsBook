# -*- coding: utf-8 -*-

import os
import sys
import logging

from mytool import pubdefines
from ui import purchase_record_ui
from PyQt5 import QtCore, QtGui, QtWidgets

class CPurchaseRecordUI(QtWidgets.QWidget, purchase_record_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CPurchaseRecordUI, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()


    def InitUI(self):
        """初始化界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditBeginInputRecord.setDate(oCurData.addMonths(-1))
        self.dateEditEndInputRecord.setDate(oCurData)
        self.comboBoxInputRecord.clear()
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxInputRecord.addItems(lstGoods)
        self.comboBoxInputRecord.setCurrentIndex(-1)
        # self.labelNum.hide()
        # self.labelAmount.hide()


    def InitConnect(self):
        self.pushButtonQueryInputRecord.clicked.connect(self.QueryInputRecord)
        self.tableWidgetInputRecord.cellDoubleClicked.connect(self.CellDoubleClicked)

    def QueryInputRecord(self):
        """查询进货记录"""
        oBeginDate = self.dateEditBeginInputRecord.date()
        sBeginTime = oBeginDate.toString("yyyy-MM-dd 00:00:00")
        iBeginTime = pubdefines.str_to_time(sBeginTime)
        oEndDate = self.dateEditEndInputRecord.date()
        sEndTime = oEndDate.toString("yyyy-MM-dd 23:59:59")
        iEndTime = pubdefines.str_to_time(sEndTime)
        sGoods = self.comboBoxInputRecord.currentText()

        dbuyInfo = pubdefines.call_manager_func("purchasemgr", "GetBuyInfoRecord", iBeginTime, iEndTime, sGoods)
        lstHead = ["日期", "类型", "商品", "进价", "数量", "备注", "双击删除"]
        self.tableWidgetInputRecord.setColumnCount(len(lstHead))
        self.tableWidgetInputRecord.setRowCount(len(dbuyInfo))
        self.tableWidgetInputRecord.setHorizontalHeaderLabels(lstHead)
        self.tableWidgetInputRecord.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        iRow = iAllNum = fPrice = 0
        for iID, tBuyInfo in dbuyInfo.items():
            for iCol, xValue in enumerate(tBuyInfo):
                if iCol == 0:
                    xValue = pubdefines.time_to_str(tBuyInfo[iCol])
                item = QtWidgets.QTableWidgetItem(str(xValue))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetInputRecord.setItem(iRow, iCol, item)
            
            icon = QtGui.QIcon(QtGui.QPixmap("image/main.ico"))
            item = QtWidgets.QTableWidgetItem(icon, str(iID))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetInputRecord.setItem(iRow, iCol + 1, item)

            iRow += 1
            iAllNum += tBuyInfo[4]
            fPrice += tBuyInfo[3] * tBuyInfo[4]

        self.labelNum.setText("总进货数量: %s" % iAllNum)
        self.labelAmount.setText("总进货金额: %s" % fPrice)
        self.labelNum.show()
        self.labelAmount.show()


    def CellDoubleClicked(self, iRow, iCol):
        if iCol != 6:
            return
        item = self.tableWidgetInputRecord.item(iRow, iCol)
        iID = int(item.text())
        pubdefines.call_manager_func("purchasemgr", "DelPurchase4DB", iID)
        self.QueryInputRecord()
