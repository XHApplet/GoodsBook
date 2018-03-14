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


    def InitImport(self):
        self.comboBoxImportGoodsType.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllType")
        self.comboBoxImportGoodsType.addItems(lstGoodsType)


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





def InitMainWidget():
    app = QtWidgets.QApplication(sys.argv)
    love = CMyWindow()
    sys.exit(app.exec_())
