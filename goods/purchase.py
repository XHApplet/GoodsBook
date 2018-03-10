# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  进货相关
"""

import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import purchase_ui

class CPurchase(QtWidgets.QWidget, purchase_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CPurchase, self).__init__(parent)
        self.setupUi(self)
        self.InitControl()
        self.InitUI()
        self.InitConnect()


    def InitControl(self):
        """初始化控件+限制"""
        tRegExp = QtCore.QRegExp("^(-?\d+)(\.\d+)?$")
        self.ValidatorPrice = QtGui.QRegExpValidator(tRegExp)
        self.ValidatorNum = QtGui.QIntValidator(1, 999999)
        self.lineEditInputPrice.setValidator(self.ValidatorPrice)
        self.lineEditInputNum.setValidator(self.ValidatorNum)


    def InitUI(self):
        """初始化录入商品界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditInput.setDate(oCurData)
        self.comboBoxInputType.clear()
        self.comboBoxInputGoods.clear()
        lstGoodsType = pubdefines.call_manager_func("globalmgr", "GetAllType")
        self.comboBoxInputType.addItems(lstGoodsType)
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxInputGoods.addItems(lstGoods)
        self.comboBoxInputType.setCurrentIndex(0)
        self.comboBoxInputGoods.setCurrentIndex(-1)
        self.InputTiplabel.hide()
        self.lineEditInputNum.setText("")
        self.lineEditInputPrice.setText("")
        self.lineEditInputRemark.setText("")


    def InitConnect(self):
        self.pushButtonInput.clicked.connect(self.OnPurchase)
        self.comboBoxInputGoods.MyFocusOutSignal.connect(self.FocusOutInputGoods)


    def ValidInput(self):
        """录入商品时控件判断"""
        if not self.lineEditInputPrice.text():
            self.slotInformation("价格不能为空")
            return False
        if not self.lineEditInputNum.text():
            self.slotInformation("数量不能为空")
            return False
        if not self.dateEditInput.dateTime():
            self.slotInformation("日期不能为空")
            return False
        if not self.comboBoxInputType.currentText():
            self.slotInformation("类别不能为空")
            return False
        if not self.comboBoxInputGoods.currentText():
            self.slotInformation("商品不能为空")
            return False
        return True


    def OnPurchase(self):
        """点击录入商品调用"""
        if not self.ValidInput():
            return
        self.dateEditInput.setTime(QtCore.QTime.currentTime())
        oDataTime = self.dateEditInput.dateTime()
        iTime = oDataTime.toTime_t()
        sGoodsType = self.comboBoxInputType.currentText()
        sGoods = self.comboBoxInputGoods.currentText()
        fPrice = float(self.lineEditInputPrice.text())
        iNum = int(self.lineEditInputNum.text())
        sRemark = self.lineEditInputRemark.text()

        # TODO 判断是否已经有了.增加商品、价格判断
        tInfo = [iTime, sGoodsType, sGoods, fPrice, iNum, sRemark]
        logging.info("InputGoods:%s" % (tInfo,))
        self.Log("Input %s" % (tInfo,))
        pubdefines.call_manager_func("buymgr", "InputGoods", tInfo)
        pubdefines.call_manager_func("goodsmgr", "InputGoods", sGoods, fPrice, iNum)

        if not pubdefines.call_manager_func("globalmgr", "HasGoods", sGoods):
            pubdefines.call_manager_func("globalmgr", "AddGoods", sGoodsType, sGoods)
        self.Log("InputDone %s" % iTime)
        # self.slotInformation("进货成功")
        self.InitUI()


    def FocusOutInputGoods(self):
        """录入商品：当输入完商品之后自动填写类型+价格"""
        sGoods = self.comboBoxInputGoods.text()
        if not sGoods:
            return
        if not pubdefines.call_manager_func("goodsmgr", "HasGoods", sGoods):
            self.InputTiplabel.show()
            return
        self.InputTiplabel.hide()
        fPrice = pubdefines.call_manager_func("goodsmgr", "GetGoodsBuyPrice", sGoods)
        self.lineEditInputPrice.setText(str(fPrice))    # 价格自动变
        sType = pubdefines.call_manager_func("globalmgr", "GetGoodsType", sGoods)
        if sType:
            self.comboBoxInputType.setCurrentText(sType)


#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import mydefines

from mytool import pubdefines

TABLE_NAME="tbl_buy"
TABLE_CREAT_SQL="""
create table %s
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Type text not null,
    Goods text not null,
    Price real not null,
    Num integer not null,
    Remark text
)
""" % TABLE_NAME


class CBuyManager(object):

    ColInfo = [
        ("Time", "integer"),
        ("Type", "text"),
        ("Goods", "text"),
        ("Price", "real"),
        ("Num", "integer"),
        ("Remark", "text"),
    ]

    def __init__(self):
        self.BuyInfo = {}

    def InputGoods(self, tData):
        """进货保存数据库"""
        sql = mydefines.get_insert_sql(TABLE_NAME, tData, self.ColInfo)
        pubdefines.call_manager_func("dbmgr", "Excute", sql)

    def QueryAllInfo(self):
        """查询所有的进货信息"""
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy query:%s %s" % (ID, tData))
            self.BuyInfo[ID] = tData


    def GetBuyInfo(self, iBegin, iEnd):
        dBuyInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy info:%s %s" % (ID, tData))
            dBuyInfo[ID] = tData
        return dBuyInfo


    def GetBuyInfoRecord(self, iBegin, iEnd, sGoods):
        dBuyInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        if sGoods:
            sql = sql + " and Goods like '%%%s%%'" % sGoods
        sql += " ORDER BY Time"
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("buy record:%s %s" % (ID, tData))
            dBuyInfo[ID] = tData
        return dBuyInfo


def InitBuy():
    oBugMgr = CBuyManager()
    pubdefines.set_manager("buymgr", oBugMgr)

