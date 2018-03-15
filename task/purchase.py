# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  进货相关
"""

import sys
import logging

from mytool import pubdefines
from PyQt5 import QtWidgets, QtCore, QtGui
from ui import purchase_ui
from . import base
from lib import pubui


class CPurchaseUI(QtWidgets.QWidget, purchase_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CPurchaseUI, self).__init__(parent)
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
        self.labelAmount.hide()


    def InitConnect(self):
        self.pushButtonInput.clicked.connect(self.OnPurchase)
        self.comboBoxInputGoods.MyFocusOutSignal.connect(self.FocusOutInputGoods)
        self.lineEditInputNum.editingFinished.connect(self.TipAmount)
        self.lineEditInputPrice.editingFinished.connect(self.TipAmount)


    def TipAmount(self):
        sPrice = self.lineEditInputPrice.text()
        sNum = self.lineEditInputNum.text()
        if sPrice and sNum:
            fPrice = float(sPrice)
            iNum = int(sNum)
            iAmount = fPrice * iNum
            self.labelAmount.setText("总价:" + str(iAmount))
            self.labelAmount.show()


    def ValidInput(self):
        """录入商品时控件判断"""
        if not self.lineEditInputPrice.text():
            pubui.slotInformation("价格不能为空")
            return False
        if not self.lineEditInputNum.text():
            pubui.slotInformation("数量不能为空")
            return False
        if not self.dateEditInput.dateTime():
            pubui.slotInformation("日期不能为空")
            return False
        if not self.comboBoxInputType.currentText():
            pubui.slotInformation("类别不能为空")
            return False
        if not self.comboBoxInputGoods.currentText():
            pubui.slotInformation("商品不能为空")
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
        pubdefines.write_to_file("xh/purchase", str(tInfo))

        pubdefines.call_manager_func("purchasemgr", "InputGoods", *tInfo)
        pubdefines.call_manager_func("goodsmgr", "InputGoods", sGoods, fPrice, iNum)

        pubdefines.call_manager_func("globalmgr", "AddGoods", sGoodsType, sGoods)
        pubdefines.write_to_file("xh/purchase", str(iTime))
        # pubui.slotInformation("进货成功")
        self.InitUI()


    def FocusOutInputGoods(self):
        """录入商品：当输入完商品之后自动填写类型+价格"""
        sGoods = self.comboBoxInputGoods.text()
        if not sGoods:
            return
        if not pubdefines.call_manager_func("globalmgr", "HasGoods", sGoods):
            self.InputTiplabel.show()
            return
        self.InputTiplabel.hide()
        fPrice = pubdefines.call_manager_func("goodsmgr", "GetGoodsBuyPrice", sGoods)
        self.lineEditInputPrice.setText(str(fPrice))    # 价格自动变
        sType = pubdefines.call_manager_func("globalmgr", "GetGoodsType", sGoods)
        if sType:
            self.comboBoxInputType.setCurrentText(sType)



TABLE_NAME = "tbl_purchase"

class CPurchase(base.CMulBase):

    m_TableName = TABLE_NAME
    m_KeyList = ["ID"]
    m_ColType = {
        "ID":       "integer",
        "Time":     "integer",
        "Type":     "text",
        "Goods":    "text",
        "Price":    "real",
        "Num":      "integer",
        "Remark":   "text",
    }


    def Init(self, *data):
        iTime, sType, sGoods, fPrice, iNum, sRemark = data
        self.m_Time = iTime
        self.m_Type = sType
        self.m_Goods = sGoods
        self.m_Price = fPrice
        self.m_Num = iNum
        self.m_Remark = sRemark



class CPurchaseManager(base.CBaseManager):

    def NewObj(self, key):
        obj = CPurchase(key)
        return obj
        

    def InputGoods(self, *data):
        """进货保存数据库"""
        ID = pubdefines.call_manager_func("globalmgr", "NewPurchaseID")
        self.NewItem(ID, *data)


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


    def DelPurchase4DB(self, iID):
        """从数据库中删除一条进货记录"""
        obj = self.GetItemBlock(iID)
        if not obj:
            return
        pubdefines.call_manager_func("goodsmgr", "AddGoodsNum", obj.m_Goods, -obj.m_Num)
        self.DelItemBlock(iID)



def InitPurchase():
    obj = CPurchaseManager()
    pubdefines.set_manager("purchasemgr", obj)

