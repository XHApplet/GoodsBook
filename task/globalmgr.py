# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  
"""


from pubcode.pubfunc import pubmisc
from . import base


class CGlobalManager(base.COneBase):

    m_DBKey = "global"
    ColInfo = [
        ("Name", "text"),
        ("Data", "blob"),
    ]
    NameList = ["GoodsInfo", "Buyer", "GoodsType"]
    FilterInfo = {
        "（": "(",
        "）": ")",
        "\t": "",
        "\n": "",
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
        return [sGoods for sGoods in dGoodsInfo.keys()]

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


def InitGlobalManager():
    obj = CGlobalManager()
    pubmisc.SetManager("globalmgr", obj)
