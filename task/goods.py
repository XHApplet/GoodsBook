# -*- coding: utf-8 -*-

import logging

from lib import misc
from mytool import pubdefines
from . import base

TABLE_NAME="tbl_goods"
TABLE_KEY_INFO = [("Goods", "text")]
TABLE_COL_INFO = [
    ("BuyPrice", "integer"),
    ("SellPrice", "integer"),
    ("Num", "integer"),
    ("Alert", "integer"),
]
TABLE_ALL_INFO = TABLE_KEY_INFO.extend

TABLE_CREAT_SQL="""
create table %s
(
    Goods text PRIMARY KEY not null,
    BuyPrice integer not null,
    SellPrice integer not null,
    Num integer not null,
    Alert integer not null
)
""" % TABLE_NAME


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


    def InputGoods(self, sGoods, fBuyPrice, iNum):
        """进货"""
        obj = self.GetItemBlock(sGoods)
        if obj:
            obj.Purchase(fBuyPrice, iNum)
            return
        self.CreateItem(sGoods, fBuyPrice, 0, iNum, self.m_DefaultAlert)
        

    # def GetGoodsInfo(self):
    #     return self.GoodsInfo


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


    def Purchase(self, fBuyPrice, iNum):
        self.m_BuyPrice = fBuyPrice
        self.m_Num += iNum
        self.Save(*("BuyPrice", "Num"))



def InitGoods():
    oGoodsMgr = CGoodsManager()
    pubdefines.set_manager("goodsmgr", oGoodsMgr)
