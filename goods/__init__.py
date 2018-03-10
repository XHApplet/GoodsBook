# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  
"""

import sys

from PyQt5 import QtWidgets
from . import mainwidget
from . import purchase

g_Obj = None

def InitGoods():
    globalmgr.InitGlobalManager()
    buy.InitBuy()
    sell.InitSell()

def Show():
    app = QtWidgets.QApplication(sys.argv)
    g_Obj = mainwidget.CMainWidget()
    g_Obj.show()
    sys.exit(app.exec_())
