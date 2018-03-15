# -*- coding: utf-8 -*-

import os
import sys
import logging

from mytool import pubdefines
from ui import shipping_record_ui
from PyQt5 import QtCore, QtGui, QtWidgets

class CShippingRecordUI(QtWidgets.QWidget, shipping_record_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CShippingRecordUI, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()


    def InitUI(self):
        """初始化界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditBeginOutputRecord.setDate(oCurData.addMonths(-1))
        self.dateEditEndOutputRecord.setDate(oCurData)
        self.comboBoxOutputRecordGoods.clear()
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxOutputRecordGoods.addItems(lstGoods)
        self.comboBoxOutputRecordGoods.setCurrentIndex(-1)
        self.comboBoxOutputRecordBuyer.clear()
        lstBuyer = pubdefines.call_manager_func("globalmgr", "GetAllBuyer")
        self.comboBoxOutputRecordBuyer.addItems(lstBuyer)
        self.comboBoxOutputRecordBuyer.setCurrentIndex(-1)
        # self.labelProfile.hide()


    def InitConnect(self):
        self.pushButtonQueryOutputRecord.clicked.connect(self.QueryOutputRecord)
        self.tableWidgetOutputRecord.cellDoubleClicked.connect(self.CellDoubleClicked)


    def QueryOutputRecord(self):
        """查询出货记录"""
        oBeginDate = self.dateEditBeginOutputRecord.date()
        sBeginTime = oBeginDate.toString("yyyy-MM-dd 00:00:00")
        iBeginTime = pubdefines.str_to_time(sBeginTime)
        oEndDate = self.dateEditEndOutputRecord.date()
        sEndTime = oEndDate.toString("yyyy-MM-dd 23:59:59")
        iEndTime = pubdefines.str_to_time(sEndTime)
        sGoods = self.comboBoxOutputRecordGoods.currentText()
        sBuyer = self.comboBoxOutputRecordBuyer.currentText()

        dSellInfo = pubdefines.call_manager_func("shippingmgr", "GetSellInfoRecord", iBeginTime, iEndTime, sGoods, sBuyer)
        lstHead = ["日期", "商品", "卖家", "售价", "数量", "备注", "利润", "双击删除"]
        self.tableWidgetOutputRecord.setColumnCount(len(lstHead))
        self.tableWidgetOutputRecord.setRowCount(len(dSellInfo))
        self.tableWidgetOutputRecord.setHorizontalHeaderLabels(lstHead)
        self.tableWidgetOutputRecord.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        iRow = iAllNum = fPrice = fProfile = 0
        for iID, tSellInfo in dSellInfo.items():
            iTime, sGoods, sSeller, fSellPrice, iNum, sRemark = tSellInfo
            for iCol, xValue in enumerate(tSellInfo):
                if iCol == 0:
                    xValue = pubdefines.time_to_str(xValue)
                item = QtWidgets.QTableWidgetItem(str(xValue))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetOutputRecord.setItem(iRow, iCol, item)
            
            fBuyPrice = pubdefines.call_manager_func("goodsmgr", "GetGoodsBuyPrice", sGoods)
            fCurProfile = (fSellPrice - fBuyPrice) * iNum
            item = QtWidgets.QTableWidgetItem(str(fCurProfile))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetOutputRecord.setItem(iRow, iCol + 1, item)

            icon = QtGui.QIcon(QtGui.QPixmap("image/main.ico"))
            item = QtWidgets.QTableWidgetItem(icon, str(iID))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetOutputRecord.setItem(iRow, iCol + 2, item)

            iRow += 1
            fProfile += fCurProfile
            iAllNum += tSellInfo[4]
            fPrice += tSellInfo[3] * tSellInfo[4]
        
        self.labelNum.setText("总售货数量:%s" % iAllNum)
        self.labelAmount.setText("总售货金额:%s" % fPrice)
        self.labelProfile.setText("总利润:%s" % fProfile)
        self.labelNum.show()
        self.labelAmount.show()
        self.labelProfile.show()


    def CellDoubleClicked(self, iRow, iCol):
        if iCol != 7:
            return
        item = self.tableWidgetOutputRecord.item(iRow, iCol)
        iID = int(item.text())
        pubdefines.call_manager_func("shippingmgr", "DelShipping4DB", iID)
        self.QueryOutputRecord()
