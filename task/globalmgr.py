# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  
"""


import logging

from lib import misc
from mytool import pubdefines
from . import base


class CGlobalManager(base.COneBase):

    m_DBKey = "global"
    ColInfo = [
        ("Name", "text"),
        ("Data", "blob"),
    ]
    NameList = ["GoodsInfo", "Buyer", "GoodsType"]
    FilterInfo = {
        "（" :"(",
        "）" :")",
        "\t" :"",
        "\n" :"",
    }

    m_GoodInfoFlag = "goodsinfo"
    m_BuyerFlag = "buyer"


    def __init__(self):
        super(CGlobalManager, self).__init__()
        self.m_GoodsType = ["公司", "自制", "非公司"]
        if not self.m_GoodInfoFlag in self.m_Data:
            self.m_Data[self.m_GoodInfoFlag] = {}
        if not self.m_BuyerFlag in self.m_Data:
            self.m_Data[self.m_BuyerFlag] = []


    def NewIDByFlag(self, sFlag):
        xid = self.m_Data.get(sFlag, 0)
        xid += 1
        self.m_Data[sFlag] = xid
        self.Save()
        return xid


    def NewPurchaseID(self):
        sFlag = "purchaseid"
        xid = self.NewIDByFlag(sFlag)
        return xid

    def NewShippingID(self):
        sFlag = "shippingid"
        xid = self.NewIDByFlag(sFlag)
        return xid

    def GetAllType(self):
        return self.m_GoodsType


    def GetAllGoodsList(self):
        dGoodsInfo = self.m_Data[self.m_GoodInfoFlag]
        return [ sGoods for sGoods in dGoodsInfo.keys() ]


    def HasGoods(self, sGoods):
        dGoodsInfo = self.m_Data[self.m_GoodInfoFlag]
        if sGoods in dGoodsInfo:
            return True
        return False


    def AddGoods(self, sGoodsType, sGoods):
        dGoodsInfo = self.m_Data[self.m_GoodInfoFlag]
        if sGoods in dGoodsInfo:
            return
        dGoodsInfo[sGoods] = sGoodsType
        self.Save()


    def GetGoodsType(self, sGoods):
        dGoodsInfo = self.m_Data[self.m_GoodInfoFlag]
        return dGoodsInfo.get(sGoods, "")


    def AddBuyer(self, sBuyer):
        if sBuyer in self.m_Data[self.m_BuyerFlag]:
            return
        self.m_Data[self.m_BuyerFlag].append(sBuyer)
        self.Save()


    def GetAllBuyer(self):
        return self.m_Data[self.m_BuyerFlag]


    # def __init__(self):
    #     super(CGlobalManager, self).__init__()
    #     self.GoodsInfo = {}
    #     self.GoodsType = set({"公司", "自制", "非公司"})
    #     self.Buyer = set()
    #     self.LoadFromDB()
    #     # self.LoadFromConfig()


    # def FilterGoods(self, sGoods):
    #     for old, new in self.FilterInfo.items():
    #         sGoods = sGoods.replace(old, new)
    #     return sGoods


    # def LoadFromDB(self):
    #     for sAttr in self.NameList:
    #         sql = "select * from %s where Name='%s'" % (TABLE_NAME, sAttr)
    #         result = pubdefines.call_manager_func("dbmgr", "Query", sql, True)
    #         if not result:
    #             self.FirstInsertData(sAttr)
    #             continue
    #         assert len(result) == 2
    #         _, sData = result
    #         value = misc.get_result_data(sData, "blob")
    #         setattr(self, sAttr, value)


    # def FirstInsertData(self, sAttr):
    #     value = getattr(self, sAttr, None)
    #     assert value is not None
    #     value = misc.get_insert_value(value, "blob")
    #     sql = "insert into %s values('%s', %s)" % (TABLE_NAME, sAttr, value)
    #     pubdefines.call_manager_func("dbmgr", "Excute", sql)


    # def LoadFromConfig(self):
    #     tGoodsList = set()
    #     with open("config/goods.txt", "r+", encoding="utf8") as fg:
    #         lstGoods = fg.readlines()
    #         for sGoods in lstGoods:
    #             sGoods = self.FilterGoods(sGoods)
    #             self.GoodsInfo.add(sGoods)
    #     with open("config/output.txt", "r+", encoding="utf8") as fo:
    #         lstOutput = fo.readlines()
    #         for sOutput in lstOutput:
    #             sOutput = self.FilterGoods(sOutput)
    #             self.GoodsOutput.add(sOutput)
    #     self.UpdateAll()


    # def UpdateAll(self, sAttr):
    #     value = getattr(self, sAttr, None)
    #     assert value is not None
    #     value = misc.get_insert_value(value, "blob")
    #     sql = "update %s set Data=%s where Name='%s'" % (TABLE_NAME, value, sAttr)
    #     pubdefines.call_manager_func("dbmgr", "Excute", sql)


    # def GetAllGoodsList(self):
    #     return [ sGoods for sGoods in self.GoodsInfo ]


    # def GetAllType(self):
    #     return self.GoodsType


    # def GetAllBuyer(self):
    #     return self.Buyer


    # def GetGoodsType(self, sGoods):
    #     sType = self.GoodsInfo.get(sGoods, None)
    #     return sType


    # def HasGoods(self, sGoods):
    #     if sGoods in self.GoodsInfo:
    #         return True
    #     return False


    # def AddGoods(self, sGoodsType, sGoods):
    #     """添加商品以及类型"""
    #     # if self.HasGoods(sGoods):
    #     #     return
    #     self.GoodsInfo[sGoods] = sGoodsType
    #     self.UpdateAll("GoodsInfo")


    # def HasBuyer(self, sBuyer):
    #     if sBuyer in self.Buyer:
    #         return True
    #     return False


    # def AddBuyer(self, sBuyer):
    #     """添加买家方向"""
    #     if self.HasBuyer(sBuyer):
    #         return
    #     self.Buyer.add(sBuyer)
    #     self.UpdateAll("Buyer")




def InitGlobalManager():
    obj = CGlobalManager()
    pubdefines.set_manager("globalmgr", obj)
