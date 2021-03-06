# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  出货相关
"""

import logging

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import shipping_ui
from lib import pubui
from . import base

from pubcode.pubfunc import pubmisc


class CShippingUI(QtWidgets.QWidget, shipping_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CShippingUI, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()

    def InitConnect(self):
        self.pushButtonOutput.clicked.connect(self.OutputGoods)
        self.comboBoxOutputGoods.MyFocusOutSignal.connect(self.FocusOutOutputGoods)
        self.lineEditOutputNum.editingFinished.connect(self.TipAmount)
        self.lineEditOutputPrice.editingFinished.connect(self.TipAmount)

    def TipAmount(self):
        sPrice = self.lineEditOutputPrice.text()
        sNum = self.lineEditOutputNum.text()
        if sPrice and sNum:
            fPrice = float(sPrice)
            iNum = int(sNum)
            iAmount = fPrice * iNum
            self.labelAmount.setText("总价:" + str(iAmount))
            self.labelAmount.show()

    def FocusOutOutputGoods(self):
        """卖出商品：当输入完商品之后自动填写价格"""
        sGoods = self.comboBoxOutputGoods.text()
        if not sGoods:
            return
        if not pubmisc.CallManagerFunc("globalmgr", "HasGoods", sGoods):
            # pubui.slotInformation("库存中无商品记录")
            return
        fPrice = pubmisc.CallManagerFunc("goodsmgr", "GetGoodsSellPrice", sGoods)
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
        lstGoods = pubmisc.CallManagerFunc("globalmgr", "GetAllGoodsList")
        self.comboBoxOutputGoods.addItems(lstGoods)
        lstBuyer = pubmisc.CallManagerFunc("globalmgr", "GetAllBuyer")
        self.comboBoxOutputBuyer.addItems(lstBuyer)
        self.comboBoxOutputGoods.setCurrentIndex(-1)
        self.comboBoxOutputBuyer.setCurrentIndex(-1)
        self.lineEditOutputNum.setText("")
        self.lineEditOutputPrice.setText("")
        self.lineEditOutputRemark.setText("")
        self.labelAmount.hide()

    def ValidOutput(self):
        """卖出商品时控件判断"""
        if not self.lineEditOutputPrice.text():
            pubui.slotInformation("价格不能为空")
            return False
        if not self.lineEditOutputNum.text():
            pubui.slotInformation("数量不能为空")
            return False
        if not self.dateEditOutput.dateTime():
            pubui.slotInformation("日期不能为空")
            return False
        if not self.comboBoxOutputBuyer.currentText():
            pubui.slotInformation("买家不能为空")
            return False
        if not self.comboBoxOutputGoods.currentText():
            pubui.slotInformation("商品不能为空")
            return False
        sGoods = self.comboBoxOutputGoods.text()
        if not pubmisc.CallManagerFunc("globalmgr", "HasGoods", sGoods):
            pubui.slotInformation("库存中无商品记录")
            return False
        # iStock = pubmisc.CallManagerFunc("goodsmgr", "GetGoodsNum", sGoods)
        # iNum = int(self.lineEditOutputNum.text())
        # if iStock < iNum:
        #     pubui.slotInformation("没有足够的库存,当前库存%s" % iStock)
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
        pubmisc.Write2File("xh/shipping", str(tInfo))

        # 计算本次卖出的利润为多少
        pubmisc.CallManagerFunc("shippingmgr", "OutputGoods", *tInfo)
        pubmisc.CallManagerFunc("goodsmgr", "OutputGoods", sGoods, fPrice, iNum)

        pubmisc.CallManagerFunc("globalmgr", "AddBuyer", sBuyer)
        pubmisc.Write2File("xh/shipping", str(iTime))
        # pubui.slotInformation("出货成功")
        self.InitUI()


TABLE_NAME = "tbl_shipping"


class CShipping(base.CMulBase):

    m_TableName = TABLE_NAME
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
        ID = pubmisc.CallManagerFunc("globalmgr", "NewShippingID")
        self.NewItem(ID, *data)

    # def QueryAllInfo(self):
    #     """查询所有的进货信息"""
    #     sql = "select * from %s" % TABLE_NAME
    #     result = pubmisc.CallManagerFunc("dbmgr", "Query", sql)
    #     for ID, *tData in result:
    #         logging.debug("sell query:%s %s" % (ID, tData))
    #         self.SellInfo[ID] = tData

    def GetSellInfo(self, iBegin, iEnd):
        """查询iBegin-iEnd时间段的出货信息"""
        dSellInfo = {}
        sql = "select * from %s where Time>=%s and Time<=%s" % (TABLE_NAME, iBegin, iEnd)
        result = pubmisc.CallManagerFunc("dbmgr", "Query", sql)
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
        result = pubmisc.CallManagerFunc("dbmgr", "Query", sql)
        for ID, *tData in result:
            logging.debug("sell record:%s %s" % (ID, tData))
            dSellInfo[ID] = tData
        return dSellInfo

    def DelShipping4DB(self, iID):
        """从数据库中删除一条出货记录"""
        obj = self.GetItemBlock(iID)
        if not obj:
            return
        pubmisc.CallManagerFunc("goodsmgr", "AddGoodsNum", obj.m_Goods, obj.m_Num)
        self.DelItemBlock(iID)


def InitShipping():
    obj = CShippingManager()
    pubmisc.SetManager("shippingmgr", obj)
