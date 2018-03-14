# -*- coding: utf-8 -*-

import logging

from PyQt5 import QtWidgets, QtCore, QtGui
from lib import misc
from mytool import pubdefines
from ui import goodslib_ui
from . import base



class CGoodsLib(QtWidgets.QWidget, goodslib_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CGoodsLib, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()

    def InitUI(self):
        pass

    def InitConnect(self):
        pass


    def ShowStock(self):
        lstTitle = ["商品", "进价", "售价", "库存", "预警值"]
        lstGoods = pubdefines.call_manager_func("globalmgr", "GetAllGoodsList")

        self.tableWidgetStock.setColumnCount(len(lstTitle))
        self.tableWidgetStock.setRowCount(len(lstGoods))
        self.tableWidgetStock.setHorizontalHeaderLabels(lstTitle)
        self.tableWidgetStock.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        for iRow, sGoods in enumerate(lstGoods):
            lstGoodsInfo = pubdefines.call_manager_func("goodsmgr", "GetGoodsInfo", sGoods)
            for iCol, value in enumerate(lstGoodsInfo):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetStock.setItem(iRow, iCol, item)


    def ShowStock2(self):
        lstTitle = ["商品", "进价", "售价", "库存", "预警值"]
        self.tableWidgetStock.setHorizontalHeaderLabels(lstTitle)
        dGoodsInfo = pubdefines.call_manager_func("goodsmgr", "GetGoodsInfo")
        iGoodsNum = len(dGoodsInfo)
        self.tableWidgetStock.setRowCount(iGoodsNum)

        self.tableWidgetStock.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置每列自适应
        # self.tableWidgetStock.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        iIndex = 0
        for sGoods, tInfo in dGoodsInfo.items():
            item = QtWidgets.QTableWidgetItem(str(sGoods))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetStock.setItem(iIndex, 0, item)
            for y in range(len(tInfo) - 1):
                # TODO 其他类型怎么判断,字符串价格排序有问题
                xTmp = tInfo[y]
                item = QtWidgets.QTableWidgetItem(str(xTmp))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetStock.setItem(iIndex, y + 1, item)
            iIndex += 1


class CGoodsManager(base.CBaseManager):
   
    m_DefaultAlert = 10

    def NewObj(self, key):
        obj = CGoods(key)
        return obj


    def GetGoodsBuyPrice(self, sGoods):
        obj = self.GetItemBlock(sGoods)
        if obj:
            return obj.GetBuyPrice()
        return 0


    def GetGoodsSellPrice(self, sGoods):
        obj = self.GetItemBlock(sGoods)
        if obj:
            return obj.GetSellPrice()
        return 0


    def InputGoods(self, sGoods, fBuyPrice, iNum):
        """进货"""
        obj = self.GetItemBlock(sGoods)
        if obj:
            obj.Purchase(fBuyPrice, iNum)
            return
        self.CreateItem(sGoods, fBuyPrice, 0, iNum, self.m_DefaultAlert)
        

    def OutputGoods(self, sGoods, fSellPrice, iNum):
        """出货"""
        obj = self.GetItemBlock(sGoods)
        if obj:
            obj.Shipping(fSellPrice, iNum)
            return
        self.CreateItem(sGoods, 0, fSellPrice, iNum, self.m_DefaultAlert)
        

    def GetGoodsInfo(self, sGoods):
        obj = self.GetItemBlock(sGoods)
        if obj:
            return obj.GetGoodsInfo()


    # def GetGoodsNum(self, sGoods):
    #     tInfo = self.GoodsInfo.get(sGoods, None)
    #     assert tInfo is not None
    #     return tInfo[2]


    # def GetGoodsBuyPrice(self, sGoods):
    #     tInfo = self.GoodsInfo.get(sGoods, None)
    #     assert tInfo is not None
    #     return tInfo[0]


    # def GetGoodsSellPrice(self, sGoods):
    #     tInfo = self.GoodsInfo.get(sGoods, None)
    #     assert tInfo is not None
    #     return tInfo[1]


    # def InputGoods(self, sGoods, fBuyPrice, iNum):
    #     if not sGoods in self.GoodsInfo:
    #         self.NewGoodsInfo(sGoods) 
    #     tInfo = self.GoodsInfo[sGoods]
    #     tInfo[0] = fBuyPrice
    #     tInfo[2] += iNum
    #     self.Update(sGoods, tInfo)


    # def OutputGoods(self, sGoods, fSellPrice, iNum):
    #     if not sGoods in self.GoodsInfo:
    #         self.NewGoodsInfo(sGoods)
    #     tInfo = self.GoodsInfo[sGoods]
    #     tInfo[1] = fSellPrice
    #     tInfo[2] -= iNum
    #     self.Update(sGoods, tInfo)


    # def NewGoodsInfo(self, sGoods):
    #     self.GoodsInfo[sGoods] = [0, 0, 0]
    #     sql = misc.get_insert_sql(TABLE_NAME, [sGoods, *self.GoodsInfo[sGoods]], self.ColInfo)
    #     pubdefines.call_manager_func("dbmgr", "Excute", sql)


    # def Update(self, sGoods, tInfo):
    #     lstSet = []
    #     for iIndex, value in enumerate(tInfo):
    #         sColName, sType = self.ColInfo[iIndex + self.KeyNum]
    #         value = misc.get_insert_value(value, sType)
    #         lstSet.append("%s=%s" % (sColName, value))
    #     sSet = ",".join(lstSet)
    #     sql = "update %s set %s where Goods='%s'" % (TABLE_NAME, sSet, sGoods)
    #     pubdefines.call_manager_func("dbmgr", "Excute", sql)


    # def Load(self):
    #     logging.info("%s load" % TABLE_NAME)
    #     sql = "select * from %s" % TABLE_NAME
    #     result = pubdefines.call_manager_func("dbmgr", "Query", sql)
    #     for sGoods, *tInfo in result:
    #         self.GoodsInfo[sGoods] = tInfo
    #         logging.debug("load: %s %s" % (sGoods, tInfo))
    #     logging.info("    load finish %s" % len(result))



class CGoods(base.CMulBase):

    m_TableName = "tbl_goods"
    m_KeyList = ["Goods"]
    ColInfo = {
        "Goods":        "text",
        "BuyPrice":     "integer",
        "SellPrice":    "integer",
        "Num":          "integer",
        "Alert":        "integer",
    }


    def Init(self, fBuyPrice, fSellPrice, iNum, iAlert):
        self.m_BuyPrice = fBuyPrice
        self.m_SellPrice = fSellPrice
        self.m_Num = iNum
        self.m_Alert = iAlert


    def GetBuyPrice(self):
        return self.m_BuyPrice

    def GetSellPrice(self):
        return self.m_SellPrice

    def Purchase(self, fBuyPrice, iNum):
        self.m_BuyPrice = fBuyPrice
        self.m_Num += iNum
        self.Save(*("BuyPrice", "Num"))

    def Shipping(self, fSellPrice, iNum):
        self.m_SellPrice = fSellPrice
        self.m_Num -= iNum
        self.Save(*("SellPrice", "Num"))


    def GetGoodsInfo(self):
        return [self.m_Goods, self.m_BuyPrice, self.m_SellPrice, self.m_Num, self.m_Alert]


def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
