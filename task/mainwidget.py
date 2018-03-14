# -*- coding: utf-8 -*-

import os
import sys
import logging

from mytool import pubdefines
from ui import mainwidget_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from . import purchase, shipping, profile, goods, purchaserecord, shippingrecord


class CMainWidget(QtWidgets.QMainWindow, mainwidget_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CMainWidget, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()


    def InitUI(self):
        self.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        self.m_Purchase = purchase.CPurchaseUI(self)
        self.m_Shipping = shipping.CShippingUI(self)
        self.m_GoodsLib = goods.CGoodsLib(self)
        self.m_Profile = profile.CProfileUI(self)
        self.m_PurchaseRecord = purchaserecord.CPurchaseRecordUI(self)
        self.m_ShippingRecord = shippingrecord.CShippingRecordUI(self)
        
        self.tabWidget.addTab(self.m_Purchase, "进货")
        self.tabWidget.addTab(self.m_Shipping, "出货")
        self.tabWidget.addTab(self.m_GoodsLib, "商品库")
        self.tabWidget.addTab(self.m_Profile, "总利润")
        self.tabWidget.addTab(self.m_PurchaseRecord, "进货记录")
        self.tabWidget.addTab(self.m_ShippingRecord, "出货记录")


    def InitConnect(self):
        self.tabWidget.currentChanged.connect(self.OnTabChanged)


    def OnTabChanged(self, iIndex):
        if iIndex == 0: #进货
            self.m_Purchase.InitUI()
        elif iIndex == 1: #出货
            self.m_Shipping.InitUI()
        elif iIndex == 2: #商品库
            self.m_GoodsLib.ShowStock()
        elif iIndex == 4: #商品库
            self.m_PurchaseRecord.InitUI()
        elif iIndex == 5: #商品库
            self.m_ShippingRecord.InitUI()
