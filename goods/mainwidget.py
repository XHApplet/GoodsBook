# -*- coding: utf-8 -*-

import os
import sys
import logging

from mytool import pubdefines
from ui import mainwidget_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from . import purchase, shipping, profile, goodslib


class CMainWidget(QtWidgets.QMainWindow, mainwidget_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CMainWidget, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.m_Purchase = purchase.CPurchase(self)
        self.m_Shipping = shipping.CShipping(self)
        self.m_Profile = profile.CProfile(self)
        self.m_GoodsLib = goodslib.CGoodsLib(self)
        
        self.tabWidget.addTab(self.m_Purchase, "进货")
        self.tabWidget.addTab(self.m_Shipping, "出货")
        self.tabWidget.addTab(self.m_Profile, "总利润")
        self.tabWidget.addTab(self.m_GoodsLib, "商品库")


    def InitConnect(self):
        self.tabWidget.currentChanged(self.OnTabChanged)


    def OnTabChanged(self, iIndex):
        if iIndex == 0: #进货
            self.m_Purchase.InitUI()
