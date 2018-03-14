# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  利润相关
"""

import sys

from PyQt5 import QtWidgets
from ui import profile_ui

class CProfile(QtWidgets.QWidget, profile_ui.Ui_Form):
    def __init__(self, parent=None):
        super(CProfile, self).__init__(parent)
        self.setupUi(self)
        self.InitUI()
        self.InitConnect()


    def InitUI(self):
        """初始化利润界面"""
        oCurData = QtCore.QDate.currentDate()
        self.dateEditBegin.setDate(oCurData.addMonths(-1))
        self.dateEditEnd.setDate(oCurData)


    def InitConnect(self):
        self.pushButtonQuery.clicked.connect(self.QueryProfile)



    def GetProfileByDate(self, sGoods, sTimeKey):
        if not sGoods in self.ProfileInfo:
            return ""
        if not sTimeKey in self.ProfileInfo[sGoods]:
            return ""
        return self.ProfileInfo[sGoods][sTimeKey]


    def AddProfile(self, sGoods, sTimeKey, fProfile):
        if not sGoods in self.ProfileInfo:
            self.ProfileInfo[sGoods] = {}
        if not sTimeKey in self.ProfileInfo[sGoods]:
            self.ProfileInfo[sGoods][sTimeKey] = 0
        self.ProfileInfo[sGoods][sTimeKey] += fProfile


    def QueryProfile(self):
        """查询利润"""
        oBeginDate = self.dateEditBegin.date()
        sBeginTime = oBeginDate.toString("yyyy-MM-dd 00:00:00")
        iBeginTime = pubdefines.str_to_time(sBeginTime)
        oEndDate = self.dateEditEnd.date()
        sEndTime = oEndDate.toString("yyyy-MM-dd 23:59:59")
        iEndTime = pubdefines.str_to_time(sEndTime)
        self.MaxProfileCol = 0
        dSellInfo = pubdefines.call_manager_func("shippingmgr", "GetSellInfo", iBeginTime, iEndTime)
        self.ProfileInfo = {}
        for _, tSellInfo in dSellInfo.items():
            iTime = tSellInfo[0]
            sTime = pubdefines.time_to_str(iTime)
            sGoods = tSellInfo[1]
            fProfile = tSellInfo[6]
            
            sDayTime = sTime[:10]
            sMonthTime = sTime[:7]
            sYearTime = sTime[:4]
            self.AddProfile(sGoods, sDayTime, fProfile)
            self.AddProfile(sGoods, sMonthTime + "月", fProfile)
            self.AddProfile(sGoods, sYearTime + "年", fProfile)
            self.AddProfile(sGoods, "总利润", fProfile)

        iGoodsNum = len(self.ProfileInfo)
        self.tableWidgetProfile.setRowCount(iGoodsNum)
        
        lstTime = ["总利润",]
        sLastYear = ""
        while oBeginDate.toString("yyyy-MM") <= oEndDate.toString("yyyy-MM"):
            sCurYear = oBeginDate.toString("yyyy")
            if sLastYear != sCurYear:
                 lstTime.append(sCurYear + "年")
                 sLastYear = sCurYear
            lstTime.append(oBeginDate.toString("yyyy-MM") + "月")
            oBeginDate = oBeginDate.addMonths(1)

        self.tableWidgetProfile.setColumnCount(len(lstTime) + 1 )

        lstGoods = [ sGoods for sGoods in self.ProfileInfo ]

        lstTitle = lstTime[:]
        lstTitle.insert(0, "商品")
        self.tableWidgetProfile.setHorizontalHeaderLabels(lstTitle)
        # if len(lstTitle) < 14:
        #     self.tableWidgetProfile.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        for iRow, sGoods in enumerate(lstGoods):
            item = QtWidgets.QTableWidgetItem(sGoods)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetProfile.setItem(iRow, 0, item)
            for iCol, sTime in enumerate(lstTime):
                fProfile = self.GetProfileByDate(sGoods, sTime)
                item = QtWidgets.QTableWidgetItem(str(fProfile))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetProfile.setItem(iRow, iCol + 1, item)