# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoselection_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_InfoSelectionDialog(object):
    def setupUi(self, InfoSelectionDialog):
        if not InfoSelectionDialog.objectName():
            InfoSelectionDialog.setObjectName(u"InfoSelectionDialog")
        InfoSelectionDialog.resize(454, 376)
        InfoSelectionDialog.setMinimumSize(QSize(0, 250))
        InfoSelectionDialog.setMaximumSize(QSize(750, 500))
        self.verticalLayout = QVBoxLayout(InfoSelectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_infoselection_main = QFrame(InfoSelectionDialog)
        self.frame_infoselection_main.setObjectName(u"frame_infoselection_main")
        self.horizontalLayout = QHBoxLayout(self.frame_infoselection_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_infoselection_list = QFrame(self.frame_infoselection_main)
        self.frame_infoselection_list.setObjectName(u"frame_infoselection_list")
        self.verticalLayout_2 = QVBoxLayout(self.frame_infoselection_list)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, -1, -1, -1)
        self.lbl_list = QLabel(self.frame_infoselection_list)
        self.lbl_list.setObjectName(u"lbl_list")
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_list.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_list)

        self.listwidget_infoselection = QListWidget(self.frame_infoselection_list)
        QListWidgetItem(self.listwidget_infoselection)
        QListWidgetItem(self.listwidget_infoselection)
        QListWidgetItem(self.listwidget_infoselection)
        self.listwidget_infoselection.setObjectName(u"listwidget_infoselection")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listwidget_infoselection.sizePolicy().hasHeightForWidth())
        self.listwidget_infoselection.setSizePolicy(sizePolicy)
        self.listwidget_infoselection.setMinimumSize(QSize(200, 0))
        self.listwidget_infoselection.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(10)
        self.listwidget_infoselection.setFont(font1)
        self.listwidget_infoselection.setProperty("showDropIndicator", False)
        self.listwidget_infoselection.setViewMode(QListView.ListMode)
        self.listwidget_infoselection.setSortingEnabled(False)

        self.verticalLayout_2.addWidget(self.listwidget_infoselection)


        self.horizontalLayout.addWidget(self.frame_infoselection_list)

        self.frame_infoselection_desc = QFrame(self.frame_infoselection_main)
        self.frame_infoselection_desc.setObjectName(u"frame_infoselection_desc")
        self.verticalLayout_3 = QVBoxLayout(self.frame_infoselection_desc)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_desc = QLabel(self.frame_infoselection_desc)
        self.lbl_desc.setObjectName(u"lbl_desc")
        self.lbl_desc.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_desc)

        self.textbrowser_desc = QTextBrowser(self.frame_infoselection_desc)
        self.textbrowser_desc.setObjectName(u"textbrowser_desc")
        self.textbrowser_desc.setMinimumSize(QSize(300, 0))
        self.textbrowser_desc.setFont(font1)
        self.textbrowser_desc.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.textbrowser_desc.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.textbrowser_desc)


        self.horizontalLayout.addWidget(self.frame_infoselection_desc)


        self.verticalLayout.addWidget(self.frame_infoselection_main)

        self.frame_infoselection_btns = QFrame(InfoSelectionDialog)
        self.frame_infoselection_btns.setObjectName(u"frame_infoselection_btns")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_infoselection_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hspacer_btns = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.hspacer_btns)

        self.btn_apply = QPushButton(self.frame_infoselection_btns)
        self.btn_apply.setObjectName(u"btn_apply")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy1)
        self.btn_apply.setMinimumSize(QSize(140, 30))
        self.btn_apply.setFont(font)
        self.btn_apply.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.btn_apply)

        self.btn_cancel = QPushButton(self.frame_infoselection_btns)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
        self.btn_cancel.setMinimumSize(QSize(90, 30))
        self.btn_cancel.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_cancel)


        self.verticalLayout.addWidget(self.frame_infoselection_btns)


        self.retranslateUi(InfoSelectionDialog)

        self.listwidget_infoselection.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(InfoSelectionDialog)
    # setupUi

    def retranslateUi(self, InfoSelectionDialog):
        InfoSelectionDialog.setWindowTitle(QCoreApplication.translate("InfoSelectionDialog", u"EPSA_InfoDialog[TEST]", None))
        self.lbl_list.setText(QCoreApplication.translate("InfoSelectionDialog", u"TEST List Description", None))

        __sortingEnabled = self.listwidget_infoselection.isSortingEnabled()
        self.listwidget_infoselection.setSortingEnabled(False)
        ___qlistwidgetitem = self.listwidget_infoselection.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("InfoSelectionDialog", u"TEST ITEM 1", None));
        ___qlistwidgetitem1 = self.listwidget_infoselection.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("InfoSelectionDialog", u"TEST ITEM 2", None));
        ___qlistwidgetitem2 = self.listwidget_infoselection.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("InfoSelectionDialog", u"TEST ITEM 3", None));
        self.listwidget_infoselection.setSortingEnabled(__sortingEnabled)

        self.lbl_desc.setText(QCoreApplication.translate("InfoSelectionDialog", u"TEST Item Description", None))
        self.textbrowser_desc.setHtml(QCoreApplication.translate("InfoSelectionDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Liberation Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt;\">This is a test description. The idea is that the user can choose an item on the left (such as resistor types) and this text will display a more informative description.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_apply.setToolTip(QCoreApplication.translate("InfoSelectionDialog", u"Use the selected item and close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_apply.setText(QCoreApplication.translate("InfoSelectionDialog", u" Apply and Close", None))
#if QT_CONFIG(tooltip)
        self.btn_cancel.setToolTip(QCoreApplication.translate("InfoSelectionDialog", u"Cancel without choosing an item", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancel.setText(QCoreApplication.translate("InfoSelectionDialog", u" Cancel", None))
    # retranslateUi

