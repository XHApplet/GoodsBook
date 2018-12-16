# -*- coding: utf-8 -*-

from pubcode.pubfunc import pubdb
from pubcode.pubfunc import pubmisc


class CBaseManager(object):
    def __init__(self, *_, **__):
        self.m_ItemDict = {}

    def GetItem(self, key, default=None):
        """从内存中获取数据"""
        obj = self.m_ItemDict.get(key, default)
        return obj

    def GetItemBlock(self, key):
        """内存中获取不到数据，就从数据库中读取"""
        obj = self.GetItem(key)
        if not obj:
            obj = self.LoadItem(key)
        return obj

    def DelItem(self, key):
        """从内存中删除数据"""
        obj = self.GetItem(key)
        if not obj:
            return
        if hasattr(obj, "Release"):
            obj.Release()
        del self.m_ItemDict[key]

    def DelItemBlock(self, key):
        """从数据库、内存中删除数据"""
        obj = self.GetItemBlock(key)
        if not obj:
            return
        if hasattr(obj, "Release"):
            obj.Release()
        obj.Delete()
        del self.m_ItemDict[key]

    def LoadItem(self, key):
        """从数据库中加载数据"""
        obj = self.NewObj(key)
        if not hasattr(obj, "Load"):
            raise Exception("%s 未定义Load函数" % obj)
        bRet = obj.Load()
        if not bRet:
            return None
        self.m_ItemDict[key] = obj
        return obj

    def NewObj(self, _):
        """各模块自行实现new一个对象"""
        raise Exception("未定义NewObj函数")

    def CreateItem(self, key, *args, **kwargs):
        """智能创建一个对象，如果数据库中存在则直接退出（不知道数据库是否有该条数据）"""
        obj = self.NewObj(key)
        if hasattr(obj, "Create"):
            obj.Create(*args, **kwargs)
        self.m_ItemDict[key] = obj
        return obj

    def NewItem(self, key, *args, **kwargs):
        """创建一个对象（已明确数据库中无此数据）"""
        obj = self.NewObj(key)
        if hasattr(obj, "New"):
            obj.New(*args, **kwargs)
        self.m_ItemDict[key] = obj
        return obj


class CMulBase(object):

    """多列对象基础类"""

    m_TableName = "tbl_goods"
    m_KeyList = ["Goods"]
    m_ColType = {
        "Goods":        "text",
        "BuyPrice":     "integer",
        "SellPrice":    "integer",
        "Num":          "integer",
        "Alert":        "integer",
    }

    def __init__(self, key):
        self.m_ColList = [sKey for sKey in self.m_ColType.keys()]
        iCount = len(self.m_KeyList)
        if not isinstance(key, tuple):
            key = (key,)
        if len(key) != iCount:
            raise Exception("参数不对!")
        for i in range(iCount):
            attr = self.m_KeyList[i]
            val = key[i]
            setattr(self, "m_" + attr, val)
        for sCol, sType in self.m_ColType.items():
            if sCol in self.m_KeyList:
                continue
            val = pubdb.GetDefaultData(sType)
            setattr(self, "m_" + sCol, val)

    def GetCreateSQL(self):
        """获取创建一条SQL的语句"""
        colList = []
        valList = []
        for sCol, sType in self.m_ColType.items():
            colList.append(sCol)
            value = getattr(self, "m_" + sCol)
            sValue = pubdb.GetInsertValue(value, sType)
            valList.append(sValue)
        names = ",".join(colList)
        vals = ",".join(valList)
        sql = "insert into %s(%s) values(%s)" % (self.m_TableName, names, vals)
        return sql

    def GetWhereSQL(self):
        whereList = []
        for sKey in self.m_KeyList:
            sType = self.m_ColType[sKey]
            value = getattr(self, "m_" + sKey)
            sValue = pubdb.GetInsertValue(value, sType)
            tmp = "%s=%s" % (sKey, sValue)
            whereList.append(tmp)
        wheres = " and ".join(whereList)
        return wheres

    def GetUpdateSQL(self, *colList):
        """获取更新一条SQL的语句"""
        setList = []
        for sCol in colList:
            sType = self.m_ColType[sCol]
            value = getattr(self, "m_" + sCol)
            sValue = pubdb.GetInsertValue(value, sType)
            tmp = "%s=%s" % (sCol, sValue)
            setList.append(tmp)
        sets = ",".join(setList)
        wheres = self.GetWhereSQL()
        sql = "update %s set %s where %s" % (self.m_TableName, sets, wheres)
        return sql

    def GetQuerySQL(self):
        """获取通过key查询一条数据的sql语句"""
        wheres = self.GetWhereSQL()
        sql = "select * from %s where %s" % (self.m_TableName, wheres)
        return sql

    def GetDeleteSQL(self):
        """获取通过key删除一条数据的语句"""
        wheres = self.GetWhereSQL()
        sql = "delete from %s where %s" % (self.m_TableName, wheres)
        return sql

    def New(self, *args, **kwargs):
        """创建一个对象"""
        self.Init(*args, **kwargs)
        self.New2DB()

    def Create(self, *args, **kwargs):
        """智能创建一个对象，如果数据库中存在则直接退出"""
        self.Init(*args, **kwargs)
        bRet = self.Load()
        if bRet:
            return
        self.New2DB()

    def New2DB(self):
        sql = self.GetCreateSQL()
        pubmisc.CallManagerFunc("dbmgr", "Excute", sql)

    def Load(self):
        sql = self.GetQuerySQL()
        result = pubmisc.CallManagerFunc("dbmgr", "Query", sql, True)
        if not result:
            return False
        for iIndex, sCol in enumerate(self.m_ColList):
            if sCol in self.m_KeyList:
                continue
            sType = self.m_ColType[sCol]
            sValue = result[iIndex]
            value = pubdb.GetResultData(sValue, sType)
            setattr(self, "m_" + sCol, value)
        return True

    def Init(self, *args, **kwargs):
        pass

    def Save(self, *colList):
        sql = self.GetUpdateSQL(*colList)
        pubmisc.CallManagerFunc("dbmgr", "Excute", sql)

    def SaveAll(self):
        self.Save(*self.m_ColList)

    def Delete(self):
        sql = self.GetDeleteSQL()
        pubmisc.CallManagerFunc("dbmgr", "Excute", sql)


class COneBase(object):
    """单列对象基础类"""
    m_TableName = "tbl_global"
    m_KeyName = "Name"
    m_DataName = "Data"
    m_DBKey = ""

    def __init__(self):
        self.m_Data = {}
        self.Init()

    def Init(self):
        if self.Load():
            return
        self.New()

    def Load(self):
        sql = "select %s from %s where %s='%s'" % (self.m_DataName, self.m_TableName, self.m_KeyName, self.m_DBKey)
        result = pubmisc.CallManagerFunc("dbmgr", "Query", sql, True)
        if not result:
            return False
        self.m_Data = pubdb.GetResultData(result[0], "blob")

    def New(self):
        sData = pubdb.GetInsertValue(self.m_Data, "blob")
        sql = "insert into %s values('%s', %s)" % (self.m_TableName, self.m_DBKey, sData)
        pubmisc.CallManagerFunc("dbmgr", "Excute", sql)

    def Save(self):
        sData = pubdb.GetInsertValue(self.m_Data, "blob")
        sql = "update %s set %s=%s where %s='%s'" % (self.m_TableName, self.m_DataName, sData, self.m_KeyName, self.m_DBKey)
        pubmisc.CallManagerFunc("dbmgr", "Excute", sql)
