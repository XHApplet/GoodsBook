#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
import xlwt

import mainwidget_ui

from PyQt5 import QtWidgets, QtGui, QtCore
from mytool import pubdefines


class CMyWindow(QtWidgets.QTabWidget, mainwidget_ui.Ui_MainWidget):

    def __init__(self, *args):
        super(CMyWindow, self).__init__(*args)
        self.setupUi(self)
        self.InitUI()


    def InitUI(self):
        self.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        self.InitImport()
        self.InitInputRecord()
        self.InitOutputRecord()

        self.InitControl()
        self.InitConnect()
        self.show()


    def Log(self, sMsg):
        pubdefines.write_to_file("xh/recode", sMsg)


    def TestQueryInput(self):
        pubdefines.call_manager_func("purchasemgr", "QueryAllInfo")


    def TestQueryOutput(self):
        pubdefines.call_manager_func("shippingmgr", "QueryAllInfo")


    def InitConnect(self):
        # self.pushButtonQueryInput.clicked.connect(self.TestQueryInput)
        # self.pushButtonQueryOutput.clicked.connect(self.TestQueryOutput)
        # self.pushButtonQueryInput.hide()
        # self.pushButtonQueryOutput.hide()

        
        self.pushButtonExport.clicked.connect(self.Export)

        self.pushButtonImportGoods.clicked.connect(self.ImportGoods)
        self.pushButtonImportBuyer.clicked.connect(self.ImportBuyer)

        self.pushButtonQueryInputRecord.clicked.connect(self.QueryInputRecord)
        self.pushButtonQueryOutputRecord.clicked.connect(self.QueryOutputRecord)



    def InitImport(self):
        self.comboBoxImportGoodsType.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllType")
        self.comboBoxImportGoodsType.addItems(lstGoodsType)


    def InitInputRecord(self):
        oCurData = QtCore.QDate.currentDate()
        self.dateEditBeginInputRecord.setDate(oCurData.addMonths(-1))
        self.dateEditEndInputRecord.setDate(oCurData)
        self.comboBoxInputRecord.clear()
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxInputRecord.addItems(lstGoods)
        self.comboBoxInputRecord.setCurrentIndex(-1)
        self.labelInputRecordNum.hide()


    def InitOutputRecord(self):
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
        # self.labelOutputRecordProfile.hide()


    def slotInformation(self, sMsg, sTitle="提示"):
        QtWidgets.QMessageBox.information(self, sTitle, self.tr(sMsg))  



    def Export(self):
        sFileName = QtWidgets.QFileDialog.getSaveFileName(self, "保存表格", "", ".xls(*.xls)")[0]
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", True)
        self.Write2Sheet(sheet)
        wbk.save(sFileName)


    def Write2Sheet(self, sheet):
        iRow = self.tableWidgetProfile.rowCount()
        iCol = self.tableWidgetProfile.columnCount()
        for col in range(iCol):
            oItem = self.tableWidgetProfile.horizontalHeaderItem(col)
            text = str(oItem.text())
            sheet.write(0, col, text)
        for row in range(iRow):
            for col in range(iCol):
                oItem = self.tableWidgetProfile.item(row, col)
                text = ""
                if oItem:
                    text = str(oItem.text())
                sheet.write(row + 1, col, text)


    def ImportGoods(self):
        """根据商品类型批量导入商品"""
        sGoodsType = self.comboBoxImportGoodsType.currentText()
        sTexts = self.textEditImport.toPlainText()
        lstText = sTexts.split("\n")
        for sGoods in lstText:
            if not sGoods:
                continue
            pubdefines.call_manager_func("globalmgr", "AddGoods", sGoodsType, sGoods)
        self.textEditImport.setText("")

    def ImportBuyer(self):
        """批量导入买家"""
        sTexts = self.textEditImport.toPlainText()
        lstText = sTexts.split("\n")
        for sBuyer in lstText:
            if not sBuyer:
                continue
            pubdefines.call_manager_func("globalmgr", "AddBuyer", sBuyer)
        self.textEditImport.setText("")


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
        lstHead = ["日期", "类型", "商品", "进价", "数量", "备注"]
        self.tableWidgetInputRecord.setColumnCount(len(lstHead))
        self.tableWidgetInputRecord.setRowCount(len(dbuyInfo))
        self.tableWidgetInputRecord.setHorizontalHeaderLabels(lstHead)
        self.tableWidgetInputRecord.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        iRow = 0
        for _, tBuyInfo in dbuyInfo.items():
            for iCol, xValue in enumerate(tBuyInfo):
                if iCol == 0:
                    xValue = pubdefines.time_to_str(tBuyInfo[iCol])
                item = QtWidgets.QTableWidgetItem(str(xValue))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetInputRecord.setItem(iRow, iCol, item)
            iRow += 1


    def QueryOutputRecord(self):
        """查询进货记录"""
        oBeginDate = self.dateEditBeginOutputRecord.date()
        sBeginTime = oBeginDate.toString("yyyy-MM-dd 00:00:00")
        iBeginTime = pubdefines.str_to_time(sBeginTime)
        oEndDate = self.dateEditEndOutputRecord.date()
        sEndTime = oEndDate.toString("yyyy-MM-dd 23:59:59")
        iEndTime = pubdefines.str_to_time(sEndTime)
        sGoods = self.comboBoxOutputRecordGoods.currentText()
        sBuyer = self.comboBoxOutputRecordBuyer.currentText()

        dSellInfo = pubdefines.call_manager_func("shippingmgr", "GetSellInfoRecord", iBeginTime, iEndTime, sGoods, sBuyer)
        lstHead = ["日期", "商品", "卖家", "售价", "数量", "备注", "利润"]
        self.tableWidgetOutputRecord.setColumnCount(len(lstHead))
        self.tableWidgetOutputRecord.setRowCount(len(dSellInfo))
        self.tableWidgetOutputRecord.setHorizontalHeaderLabels(lstHead)
        self.tableWidgetOutputRecord.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        iRow = fProfile = 0
        for _, tSellInfo in dSellInfo.items():
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
            iRow += 1
            fProfile += fCurProfile
        self.labelOutputRecordProfile.setText("总利润:%s" % fProfile)
        self.labelOutputRecordProfile.show()



def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
