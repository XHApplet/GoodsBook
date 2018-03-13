# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 15:07:48
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 15:07:48
@Desc:  
"""

from mytool import pubdefines
from . import dbmanager

def InitDB():
    obj = dbmanager.CDBManager()
    pubdefines.set_manager("dbmgr", obj)

