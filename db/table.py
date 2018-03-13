# -*- coding: utf-8 -*-


TABLE_SQL_GLOBAL="""
create table tbl_global
(
    Name text not null PRIMARY KEY,
    Data blob not null
)
"""


TABLE_SQL_GOODS="""
create table tbl_goods
(
    Goods text PRIMARY KEY not null,
    BuyPrice integer not null,
    SellPrice integer not null,
    Num integer not null,
    Alert integer not null
)
"""

TABLE_SQL_PURCHASE="""
create table tbl_purchase
(
    ID integer PRIMARY KEY autoincrement,
    Time datetime not null,
    Type text not null,
    Goods text not null,
    Price real not null,
    Num integer not null,
    Remark text
)
"""


ALL_TABLES = [
    TABLE_SQL_GLOBAL,
    TABLE_SQL_GOODS,
    TABLE_SQL_PURCHASE,
]
