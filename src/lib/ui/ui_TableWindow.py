# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_TableWindowSuHKSk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_TableExample(object):
    def setupUi(self, TableExample):
        if not TableExample.objectName():
            TableExample.setObjectName(u"TableExample")
        TableExample.resize(715, 393)
        TableExample.setMinimumSize(QSize(400, 0))
        self.wgt_table_example = QWidget(TableExample)
        self.wgt_table_example.setObjectName(u"wgt_table_example")
        self.wgt_table_example.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"")
        self.vlt_wgt_table_example = QVBoxLayout(self.wgt_table_example)
        self.vlt_wgt_table_example.setSpacing(9)
        self.vlt_wgt_table_example.setObjectName(u"vlt_wgt_table_example")
        self.vlt_wgt_table_example.setContentsMargins(9, 9, 9, 9)
        self.frm_table_example = QFrame(self.wgt_table_example)
        self.frm_table_example.setObjectName(u"frm_table_example")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_table_example.sizePolicy().hasHeightForWidth())
        self.frm_table_example.setSizePolicy(sizePolicy)
        self.frm_table_example.setMinimumSize(QSize(0, 0))
        self.frm_table_example.setMaximumSize(QSize(16777215, 10000000))
        self.frm_table_example.setStyleSheet(u"QFrame{\n"
"border-radius: 15px;\n"
"background-color: rgb(45, 49, 58);\n"
"}\n"
"\n"
"QFrame#frm_table_example{\n"
"border: 2px solid;\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-top-color: rgba(199,126,52,255);\n"
"}\n"
"")
        self.frm_table_example.setFrameShape(QFrame.NoFrame)
        self.frm_table_example.setFrameShadow(QFrame.Raised)
        self.vlt_frm_table_example = QVBoxLayout(self.frm_table_example)
        self.vlt_frm_table_example.setSpacing(5)
        self.vlt_frm_table_example.setObjectName(u"vlt_frm_table_example")
        self.vlt_frm_table_example.setContentsMargins(10, -1, 10, -1)
        self.frm_table = QFrame(self.frm_table_example)
        self.frm_table.setObjectName(u"frm_table")
        self.frm_table.setStyleSheet(u"background-color: rgb(48, 52, 63);\n"
"border-top-right-radius: 12px;\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"\n"
"\n"
"\n"
"")
        self.frm_table.setFrameShape(QFrame.StyledPanel)
        self.frm_table.setFrameShadow(QFrame.Raised)
        self.vlt_frm_table = QVBoxLayout(self.frm_table)
        self.vlt_frm_table.setObjectName(u"vlt_frm_table")
        self.tbl_example = QTableView(self.frm_table)
        self.tbl_example.setObjectName(u"tbl_example")
        self.tbl_example.setStyleSheet(u"QHeaderView::section {\n"
"                background-color: rgb(48, 52, 63);\n"
"                color: rgb(92, 101, 118);\n"
"                border: none;\n"
"                font-size: 9pt;\n"
"                }\n"
"\n"
"QTableView {\n"
"                \n"
"                gridline-color: rgb(48, 52, 63);\n"
"                font-size: 8pt;\n"
"	            }\n"
"\n"
"QTableView::item {\n"
"    	        color:  rgb(171, 178, 191);\n"
"				border-bottom: 1px solid rgba(92, 101, 118, 100);\n"
"	            }\n"
"                \n"
"\n"
"QTableView QTableCornerButton::section {\n"
"                background-color: rgb(48, 52, 63);\n"
"                border: 1px solid #fffff8;\n"
"                border: none;\n"
"                }\n"
"\n"
"QTableView{\n"
"                selection-background-color: rgb(40, 44, 52);\n"
"                selection-color: rgb(171, 178, 191);\n"
"                }\n"
"\n"
"QScrollBar:horizontal {\n"
"                border: none;\n"
"                background:   rgb(48, 52, 6"
                        "3);\n"
"                height: 18px;\n"
"                margin: 0 25px 0 25px;\n"
"                border-radius: 7px;\n"
"                }\n"
"QScrollBar::handle:horizontal {\n"
"                background: rgb(57, 62, 74);\n"
"                min-width: 25px;\n"
"                border-radius: 7px\n"
"                }\n"
"QScrollBar::handle:horizontal:hover {	\n"
"                background: rgb(0, 119, 160);\n"
"                min-width: 25px;\n"
"                border-radius: 7px\n"
"                }\n"
"QScrollBar::add-line:horizontal {\n"
"                border-left: 0px solid rgb(40, 44, 52);\n"
"                background:  rgb(57, 62, 74);\n"
"                width: 23px;\n"
"                padding: 0px;\n"
"                border-top-right-radius: 7px;\n"
"                border-top-left-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                border-bottom-right-radius: 7px;\n"
"                subcontrol-position: right;\n"
"                subcontrol-origin: ma"
                        "rgin;\n"
"                }\n"
"QScrollBar::sub-line:horizontal {\n"
"                border-right: 0px solid rgb(40, 44, 52);\n"
"                background:  rgb(57, 62, 74);\n"
"                width: 23px;\n"
"                padding: 0px;\n"
"                border-top-left-radius: 7px;\n"
"                border-top-right-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                border-bottom-right-radius: 7px;\n"
"                subcontrol-position: left;\n"
"                subcontrol-origin: margin;\n"
"}\n"
" QScrollBar::add-line:horizontal:hover,  QScrollBar::sub-line:horizontal:hover {\n"
"\n"
"	            background: rgb(0, 119, 160);\n"
"\n"
"                }\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"                background: none;\n"
"                }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"                background: none;\n"
"                }\n"
"QScrollBar:vertical {\n"
"               "
                        " border: none;\n"
"                background:   rgb(48, 52, 63);\n"
"                width: 18px;\n"
"                margin: 25px 0px 25px 0px;\n"
"                border-radius: 7px;\n"
"                }\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"                background: rgb(57, 62, 74);\n"
"                min-height: 25px;\n"
"                border-radius: 7px\n"
"                }\n"
"QScrollBar::handle:vertical:hover {	\n"
"                background: rgb(0, 119, 160);\n"
"                min-height: 25px;\n"
"                border-radius: 7px\n"
"                }\n"
" QScrollBar::add-line:vertical {\n"
"                border-top: 0px solid rgb(40, 44, 52);\n"
"                background:  rgb(57, 62, 74);\n"
"                height: 23px;\n"
"                padding: 0px;\n"
"                border-top-right-radius: 7px;\n"
"                border-top-left-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                border-bottom-right-radius: 7px;\n"
"                s"
                        "ubcontrol-position: bottom;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
" QScrollBar::add-line:vertical:hover,  QScrollBar::sub-line:vertical:hover {\n"
"\n"
"	            background: rgb(0, 119, 160);\n"
"\n"
"}\n"
" QScrollBar::sub-line:vertical {\n"
"                border-bottom: 0px solid rgb(40, 44, 52);\n"
"                background:  rgb(57, 62, 74);\n"
"                height: 23px;\n"
"                padding: 0px;\n"
"                border-top-left-radius: 7px;\n"
"                border-top-right-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                border-bottom-right-radius: 7px;\n"
"                subcontrol-position: top;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"                background: none;\n"
"                }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"   "
                        "             }")
        self.tbl_example.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tbl_example.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl_example.setProperty("showDropIndicator", False)
        self.tbl_example.setShowGrid(False)
        self.tbl_example.setCornerButtonEnabled(False)

        self.vlt_frm_table.addWidget(self.tbl_example)


        self.vlt_frm_table_example.addWidget(self.frm_table)

        self.le_add_entry = QLineEdit(self.frm_table_example)
        self.le_add_entry.setObjectName(u"le_add_entry")
        self.le_add_entry.setStyleSheet(u"QLineEdit{\n"
"                                background-color: rgb(33, 37, 43);\n"
"                                border-radius: 5px;\n"
"                                border: 2px solid rgb(33, 37, 43);\n"
"                                padding-left: 5px;\n"
"                                color:rgb(171, 178, 191);\n"
"                                }\n"
"\n"
"")

        self.vlt_frm_table_example.addWidget(self.le_add_entry)

        self.pb_delete_entry = QPushButton(self.frm_table_example)
        self.pb_delete_entry.setObjectName(u"pb_delete_entry")
        self.pb_delete_entry.setMinimumSize(QSize(80, 22))
        self.pb_delete_entry.setMaximumSize(QSize(80, 22))
        self.pb_delete_entry.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 119, 160);\n"
"border-bottom-right-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"border: 1px solid rgb(0,119,160);\n"
"color: rgb(171, 178, 191)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"background-color: rgb(0, 137, 183);\n"
"}")

        self.vlt_frm_table_example.addWidget(self.pb_delete_entry, 0, Qt.AlignRight)


        self.vlt_wgt_table_example.addWidget(self.frm_table_example)

        TableExample.setCentralWidget(self.wgt_table_example)

        self.retranslateUi(TableExample)

        QMetaObject.connectSlotsByName(TableExample)
    # setupUi

    def retranslateUi(self, TableExample):
        TableExample.setWindowTitle(QCoreApplication.translate("TableExample", u"MainWindow", None))
        self.pb_delete_entry.setText(QCoreApplication.translate("TableExample", u"Delete", None))
    # retranslateUi

