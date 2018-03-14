# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  商品库相关
"""

import sys

from PyQt5 import QtWidgets
from ui import goodslib_ui

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
        lstTitle = ["商品", "进价", "售价", "库存"]
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