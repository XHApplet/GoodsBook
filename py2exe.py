#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

sCurPath = os.getcwd()
print(sCurPath)

sCmd = "pyinstaller -w \
--workpath D:/mycode/exe/build \
--distpath D:/mycode/exe/dist \
--specpath D:/mycode/exe \
-nGoodsBook \
-i %s/image/main.ico \
-p %s;\
%s/db;\
%s/image;\
%s/lib;\
%s/mytool;\
%s/task;\
%s/ui;\
C:/Python36/DLLs;\
C:/Python36/Lib \
%s/main.py"\
%(sCurPath, sCurPath, sCurPath, sCurPath, sCurPath, sCurPath, sCurPath, sCurPath, sCurPath)

os.system(sCmd)
