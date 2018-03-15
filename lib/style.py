# -*- coding: utf-8 -*-

QSS = """
    QWidget {
        background-color:$background1;
        background-origin:content;
        font-family: "微软雅黑";
        font-size: 12px;
        color:$foreground2;
    }
    QTableWidget {
        border-style:none;
        background-color:$background4;
        selection-color:$foreground3;
        selection-background-color:$background2;
    }
    QTabWidget::tab-bar {
    }
    QPushButton {
        background-color:$background2;
        border-style:none;
        color:$foreground1;
        padding:3px 15px 3px 15px;
    }
    QLineEdit {
        color:$foreground2;
        background: $background4;
    }
    QLabel {
        color:$foreground1;
        background: $background1;
    }
    QComboBox {
        color:$foreground2;
        background: $background4;
    }
    QDateEdit {
        color:$foreground2;
        background: $background4;
    }
"""


COLOR = {
    "$background1"  :   "#3A5FBC",
    "$background2"  :   "#3D7FDD",
    "$background3"  :   "#80B7F4",
    "$background4"  :   "#F5FAFE",
    "$background5"  :   "#80B7F4",
    "$background6"  :   "#FFFFFF",
    "$foreground1"  :   "#F5FAFE",
    "$foreground2"  :   "#111111",
    "$foreground3"  :   "#EdF5FE",
}

def GetSytle():
    qss = QSS
    for sFlag, sColor in COLOR.items():
        qss = qss.replace(sFlag, sColor)
    return qss
