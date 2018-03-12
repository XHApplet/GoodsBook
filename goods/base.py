# -*- coding: utf-8 -*-

from lib import misc

import copy

class CBaseManager(object):
    m_TableName = ""
    m_KeyInfo = []
    m_ColInfo = []
    m_SQL = ""
    
    def __init__(self, *args, **kwargs):
        self.m_AllInfo = copy.deepcopy(self.m_KeyInfo)
        self.m_AllInfo.extend(self.m_ColInfo)
        if len(self.m_KeyInfo) == 1:
            self.m_Key = self.m_KeyInfo[0][0]
        else:
            lstKey = [ sKey for sKey, _ in self.m_ColInfo ]
            self.m_Key = tuple(lstKey)
        self.m_ItemInfo = {}

    def InitSQL(self):
        self.m_SQL += "create table %s\r\n" % self.m_TableName
        self.m_SQL += "(\r\n"
        for sKey, sType in self.m_KeyInfo:
            self.m_SQL += "\t%s %s PRIMARY KEY not null,\r\n" % (sKey, sType)
        for sKey, sType in self.m_ColInfo:
            self.m_SQL += "\t%s %s not null,\r\n" % (sKey, sType)
        self.m_SQL = self.m_SQL[:-3]
        self.m_SQL += "\r\n)\r\n"


    def Load(self):
        sql = "select * from %s" % self.m_TableName
        result = pubdefines.call_manager_func("dbmgr", "Query", sql)
        for lstInfo in result:
            lstKey = lstInfo[:len(self.m_KeyInfo)]
            lstValue = lstInfo[len(self.m_KeyInfo):]
            sKey = self._GetKey(lstKey)
            self.m_ColInfo[sKey] = CBase(lstValue, self.m_ColInfo)


    def _GetKey(self, lstKey):
        if len(lstKey) == 1:
            return lstKey[0]
        return tuple(lstKey)


class CBase(object):
    def __init__(self, lstValue, colInfo):
        for iIndex, value in enumerate(lstValue):
            sCol, sType = colInfo[iIndex]
            xValue = misc.get_value_by_data(value, sType)
            setattr(self, sCol, xValue)


