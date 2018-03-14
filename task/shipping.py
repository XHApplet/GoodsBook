# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  出货相关
"""

import sys
import logging

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import shipping_ui
from lib import misc
from mytool import pubdefines
from . import base

class CShippingUI(QtWidgets.QWidget, shipping_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CShippingUI, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()


    def InitConnect(self):
        self.pushButtonOutput.clicked.connect(self.OutputGoods)
        self.comboBoxOutputGoods.MyFocusOutSignal.connect(self.FocusOutOutputGoods)


    def FocusOutOutputGoods(self):
        """卖出商品：当输入完商品之后自动填写价格"""
        sGoods = self.comboBoxOutputGoods.text()
        if not sGoods:
            return
        if not pubdefines.call_manager_func("globalmgr", "HasGoods", sGoods):
            # self.slotInformation("库存中无商品记录")
            return
        fPrice = pubdefines.call_manager_func("goodsmgr", "GetGoodsSellPrice", sGoods)
        if abs(fPrice) > 1e-6:
            self.lineEditOutputPrice.setText(str(fPrice))    # 价格自动变


    def InitControl(self):
        """初始化控件+限制"""
        tRegExp = QtCore.QRegExp("^(-?\d+)(\.\d+)?$")
        self.ValidatorPrice = QtGui.QRegExpValidator(tRegExp)
        self.ValidatorNum = QtGui.QIntValidator(1, 999999)

        self.lineEditOutputPrice.setValidator(self.ValidatorPrice)
        self.lineEditOutputNum.setValidator(self.ValidatorNum)


    def InitUI(self):
        """初始化卖出商品界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditOutput.setDate(oCurData)
        self.comboBoxOutputGoods.clear()
        self.comboBoxOutputBuyer.clear()
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")
        self.comboBoxOutputGoods.addItems(lstGoods)
        lstBuyer = pubdefines.call_manager_func("globalmgr", "GetAllBuyer")
        self.comboBoxOutputBuyer.addItems(lstBuyer)
        self.comboBoxOutputGoods.setCurrentIndex(-1)
        self.comboBoxOutputBuyer.setCurrentIndex(-1)
        self.lineEditOutputNum.setText("")
        self.lineEditOutputPrice.setText("")
        self.lineEditOutputRemark.setText("")


    def ValidOutput(self):
        """卖出商品时控件判断"""
        if not self.lineEditOutputPrice.text():
            self.slotInformation("价格不能为空")
            return False
        if not self.lineEditOutputNum.text():
            self.slotInformation("数量不能为空")
            return False
        if not self.dateEditOutput.dateTime():
            self.slotInformation("日期不能为空")
            return False
        if not self.comboBoxOutputBuyer.currentText():
            self.slotInformation("买家不能为空")
            return False
        if not self.comboBoxOutputGoods.currentText():
            self.slotInformation("商品不能为空")
            return False
        sGoods = self.comboBoxOutputGoods.text()
        if not pubdefines.call_manager_func("globalmgr", "HasGoods", sGoods):
            self.slotInformation("库存中无商品记录")
            return False
        # iStock = pubdefines.call_manager_func("goodsmgr", "GetGoodsNum", sGoods)
        # iNum = int(self.lineEditOutputNum.text())
        # if iStock < iNum:
        #     self.slotInformation("没有足够的库存,当前库存%s" % iStock)
        #     return False
        return True


    def OutputGoods(self):
        if not self.ValidOutput():
            return
        self.dateEditOutput.setTime(QtCore.QTime.currentTime())
        oDataTime = self.dateEditOutput.dateTime()
        iTime = oDataTime.toTime_t()
        sGoods = self.comboBoxOutputGoods.currentText()
        sBuyer = self.comboBoxOutputBuyer.currentText()
        fPrice = float(self.lineEditOutputPrice.text())
        iNum = int(self.lineEditOutputNum.text())
        sRemark = self.lineEditOutputRemark.text()

        tInfo = [iTime, sGoods, sBuyer, fPrice, iNum, sRemark]
        logging.info("OutputGoods:%s" % (tInfo,))
        pubdefines.write_to_file("xh/shipping", str(tInfo))

        # 计算本次卖出的利润为多少
        pubdefines.call_manager_func("shippingmgr", "OutputGoods", *tInfo)
        pubdefines.call_manager_func("goodsmgr", "OutputGoods", sGoods, fPrice, iNum)

        pubdefines.call_manager_func("globalmgr", "AddBuyer", sBuyer)
        pubdefines.write_to_file("xh/shipping", str(iTime))
        # self.slotInformation("出货成功")
        self.InitUI()




class CShipping(base.CMulBase):
    m_TableName = "tbl_shipping"
    m_KeyList = ["ID"]
    m_ColType = {
        "ID":       "integer",
        "Time":     "integer",
        "Goods":    "text",
        "Seller":   "text",
        "Price":    "real",
        "Num":      "integer",
        "Remark":   "text",
    }

    def Init(self, *data):
        iTime, sGoods, sSeller, fPrice, iNum, sRemark = data
        self.m_Time = iTime
        self.m_Goods = sGoods
        self.m_Seller = sSeller
        self.m_Price = fPrice
        self.m_Num = iNum
        self.m_Remark = sRemark


class CShippingManager(base.CBaseManager):
    
    def NewObj(self, key):
        obj = CShipping(key)
        return obj


    def OutputGoods(self, *data):
        """出货保存数据库"""
        ID = pubdefines.call_manager_func("globalmgr", "NewShippingID")
        self.NewItem(ID, *data)


    def QueryAllInfo(self):
        """查询所有的进货信息"""
        sql = "select * from %s" % TABLE_NAME
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell query:%s %s" % (ID, tData))
            self.SellInfo[ID] = tData


    def GetSellInfo(self, iBegin, iEnd):
        dSellInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell info:%s %s" % (ID, tData))
            dSellInfo[ID] = tData
        return dSellInfo


    def GetSellInfoRecord(self, iBegin, iEnd, sGoods, sBuyer):
        dSellInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        if sGoods:
            sql = sql + " and Goods like '%%%s%%'" % sGoods
        if sBuyer:
            sql = sql + " and Seller like '%%%s%%'" % sBuyer
        sql += " ORDER BY Time"
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell record:%s %s" % (ID, tData))
            dSellInfo[ID] = tData
        return dSellInfo



def InitShipping():
    obj = CShippingManager()
    pubdefines.set_manager("shippingmgr", obj)
