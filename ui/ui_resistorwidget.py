# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resistor_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ResistorWidget(object):
    def setupUi(self, ResistorWidget):
        if not ResistorWidget.objectName():
            ResistorWidget.setObjectName(u"ResistorWidget")
        ResistorWidget.resize(606, 408)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResistorWidget.sizePolicy().hasHeightForWidth())
        ResistorWidget.setSizePolicy(sizePolicy)
        ResistorWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(ResistorWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupbox_pntype = QGroupBox(ResistorWidget)
        self.groupbox_pntype.setObjectName(u"groupbox_pntype")
        sizePolicy.setHeightForWidth(self.groupbox_pntype.sizePolicy().hasHeightForWidth())
        self.groupbox_pntype.setSizePolicy(sizePolicy)
        self.groupbox_pntype.setMinimumSize(QSize(450, 0))
        self.groupbox_pntype.setMaximumSize(QSize(16777215, 120))
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        self.groupbox_pntype.setFont(font)
        self.groupbox_pntype.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupbox_pntype.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupbox_pntype)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.hlayout_type = QHBoxLayout()
        self.hlayout_type.setObjectName(u"hlayout_type")
        self.lbl_type = QLabel(self.groupbox_pntype)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setMinimumSize(QSize(0, 25))
        self.lbl_type.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.lbl_type.setFont(font1)

        self.hlayout_type.addWidget(self.lbl_type)

        self.combo_type = QComboBox(self.groupbox_pntype)
        self.combo_type.addItem("")
        self.combo_type.setObjectName(u"combo_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_type.sizePolicy().hasHeightForWidth())
        self.combo_type.setSizePolicy(sizePolicy1)
        self.combo_type.setMinimumSize(QSize(120, 25))
        self.combo_type.setMaximumSize(QSize(200, 30))
        font2 = QFont()
        font2.setFamilies([u"Liberation Sans"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.combo_type.setFont(font2)

        self.hlayout_type.addWidget(self.combo_type)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.hlayout_type.addItem(self.horizontalSpacer)

        self.btn_type = QPushButton(self.groupbox_pntype)
        self.btn_type.setObjectName(u"btn_type")
        sizePolicy.setHeightForWidth(self.btn_type.sizePolicy().hasHeightForWidth())
        self.btn_type.setSizePolicy(sizePolicy)
        self.btn_type.setMinimumSize(QSize(20, 20))
        self.btn_type.setMaximumSize(QSize(25, 25))

        self.hlayout_type.addWidget(self.btn_type)

        self.hspacer_type_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayout_type.addItem(self.hspacer_type_right)


        self.verticalLayout_3.addLayout(self.hlayout_type)

        self.hlayout_pns = QHBoxLayout()
        self.hlayout_pns.setObjectName(u"hlayout_pns")
        self.lbl_mpn = QLabel(self.groupbox_pntype)
        self.lbl_mpn.setObjectName(u"lbl_mpn")
        self.lbl_mpn.setMinimumSize(QSize(0, 25))
        self.lbl_mpn.setMaximumSize(QSize(16777215, 30))
        self.lbl_mpn.setFont(font1)

        self.hlayout_pns.addWidget(self.lbl_mpn)

        self.input_mpn = QLineEdit(self.groupbox_pntype)
        self.input_mpn.setObjectName(u"input_mpn")
        sizePolicy1.setHeightForWidth(self.input_mpn.sizePolicy().hasHeightForWidth())
        self.input_mpn.setSizePolicy(sizePolicy1)
        self.input_mpn.setMinimumSize(QSize(120, 25))
        self.input_mpn.setMaximumSize(QSize(300, 30))
        self.input_mpn.setFont(font2)

        self.hlayout_pns.addWidget(self.input_mpn)

        self.hspacer_pn_middle = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.hlayout_pns.addItem(self.hspacer_pn_middle)

        self.lbl_apn = QLabel(self.groupbox_pntype)
        self.lbl_apn.setObjectName(u"lbl_apn")
        self.lbl_apn.setMinimumSize(QSize(0, 25))
        self.lbl_apn.setMaximumSize(QSize(16777215, 30))
        self.lbl_apn.setFont(font1)
        self.lbl_apn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.hlayout_pns.addWidget(self.lbl_apn)

        self.input_apn = QLineEdit(self.groupbox_pntype)
        self.input_apn.setObjectName(u"input_apn")
        sizePolicy1.setHeightForWidth(self.input_apn.sizePolicy().hasHeightForWidth())
        self.input_apn.setSizePolicy(sizePolicy1)
        self.input_apn.setMinimumSize(QSize(120, 25))
        self.input_apn.setMaximumSize(QSize(300, 30))
        self.input_apn.setFont(font2)

        self.hlayout_pns.addWidget(self.input_apn)

        self.hspacer_pn_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayout_pns.addItem(self.hspacer_pn_right)


        self.verticalLayout_3.addLayout(self.hlayout_pns)


        self.verticalLayout.addWidget(self.groupbox_pntype)

        self.vspacer_top = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.vspacer_top)

        self.val_gridgroupBox = QGroupBox(ResistorWidget)
        self.val_gridgroupBox.setObjectName(u"val_gridgroupBox")
        sizePolicy.setHeightForWidth(self.val_gridgroupBox.sizePolicy().hasHeightForWidth())
        self.val_gridgroupBox.setSizePolicy(sizePolicy)
        self.val_gridgroupBox.setMinimumSize(QSize(450, 0))
        self.val_gridgroupBox.setMaximumSize(QSize(16777215, 200))
        self.val_gridgroupBox.setFont(font)
        self.val_gridgroupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.val_gridgroupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.val_gridgroupBox)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.lbl_Vrated = QLabel(self.val_gridgroupBox)
        self.lbl_Vrated.setObjectName(u"lbl_Vrated")
        self.lbl_Vrated.setMinimumSize(QSize(0, 25))
        self.lbl_Vrated.setMaximumSize(QSize(120, 30))
        self.lbl_Vrated.setFont(font1)
        self.lbl_Vrated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_Vrated, 3, 4, 1, 1)

        self.lbl_R = QLabel(self.val_gridgroupBox)
        self.lbl_R.setObjectName(u"lbl_R")
        self.lbl_R.setMinimumSize(QSize(0, 25))
        self.lbl_R.setMaximumSize(QSize(120, 30))
        self.lbl_R.setFont(font1)
        self.lbl_R.setFrameShadow(QFrame.Raised)
        self.lbl_R.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_R, 2, 0, 1, 1)

        self.unitlbl_Trated = QLabel(self.val_gridgroupBox)
        self.unitlbl_Trated.setObjectName(u"unitlbl_Trated")
        self.unitlbl_Trated.setMinimumSize(QSize(0, 25))
        self.unitlbl_Trated.setMaximumSize(QSize(50, 30))
        self.unitlbl_Trated.setFont(font1)
        self.unitlbl_Trated.setMargin(0)

        self.gridLayout_2.addWidget(self.unitlbl_Trated, 5, 2, 1, 1)

        self.hspacer_row4_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row4_right, 5, 7, 1, 1)

        self.hspacer_row3_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row3_middle, 4, 3, 1, 1)

        self.lbl_ThetaR = QLabel(self.val_gridgroupBox)
        self.lbl_ThetaR.setObjectName(u"lbl_ThetaR")
        self.lbl_ThetaR.setMinimumSize(QSize(0, 25))
        self.lbl_ThetaR.setMaximumSize(QSize(120, 30))
        self.lbl_ThetaR.setFont(font1)
        self.lbl_ThetaR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_ThetaR, 4, 4, 1, 1)

        self.lbl_Trated = QLabel(self.val_gridgroupBox)
        self.lbl_Trated.setObjectName(u"lbl_Trated")
        self.lbl_Trated.setMinimumSize(QSize(0, 25))
        self.lbl_Trated.setMaximumSize(QSize(120, 30))
        self.lbl_Trated.setFont(font1)
        self.lbl_Trated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_Trated, 5, 0, 1, 1)

        self.hspacer_row1_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row1_right, 2, 7, 1, 1)

        self.lbl_Vmaxapplied = QLabel(self.val_gridgroupBox)
        self.lbl_Vmaxapplied.setObjectName(u"lbl_Vmaxapplied")
        self.lbl_Vmaxapplied.setMinimumSize(QSize(0, 25))
        self.lbl_Vmaxapplied.setMaximumSize(QSize(120, 30))
        self.lbl_Vmaxapplied.setFont(font1)
        self.lbl_Vmaxapplied.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_Vmaxapplied, 3, 0, 1, 1)

        self.unitlbl_R = QLabel(self.val_gridgroupBox)
        self.unitlbl_R.setObjectName(u"unitlbl_R")
        self.unitlbl_R.setMinimumSize(QSize(0, 25))
        self.unitlbl_R.setMaximumSize(QSize(50, 30))
        self.unitlbl_R.setFont(font1)
        self.unitlbl_R.setMargin(0)

        self.gridLayout_2.addWidget(self.unitlbl_R, 2, 2, 1, 1)

        self.unitlbl_ThetaR = QLabel(self.val_gridgroupBox)
        self.unitlbl_ThetaR.setObjectName(u"unitlbl_ThetaR")
        self.unitlbl_ThetaR.setMinimumSize(QSize(0, 25))
        self.unitlbl_ThetaR.setMaximumSize(QSize(50, 30))
        self.unitlbl_ThetaR.setFont(font1)

        self.gridLayout_2.addWidget(self.unitlbl_ThetaR, 4, 6, 1, 1)

        self.input_Tbase = QLineEdit(self.val_gridgroupBox)
        self.input_Tbase.setObjectName(u"input_Tbase")
        sizePolicy1.setHeightForWidth(self.input_Tbase.sizePolicy().hasHeightForWidth())
        self.input_Tbase.setSizePolicy(sizePolicy1)
        self.input_Tbase.setMinimumSize(QSize(0, 25))
        self.input_Tbase.setMaximumSize(QSize(200, 30))
        self.input_Tbase.setFont(font2)
        self.input_Tbase.setLayoutDirection(Qt.RightToLeft)
        self.input_Tbase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_Tbase.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_Tbase, 4, 1, 1, 1)

        self.hspacer_row4_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row4_middle, 5, 3, 1, 1)

        self.hspacer_row2_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row2_middle, 3, 3, 1, 1)

        self.lbl_Tbase = QLabel(self.val_gridgroupBox)
        self.lbl_Tbase.setObjectName(u"lbl_Tbase")
        self.lbl_Tbase.setMinimumSize(QSize(0, 25))
        self.lbl_Tbase.setMaximumSize(QSize(120, 30))
        self.lbl_Tbase.setFont(font1)
        self.lbl_Tbase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_Tbase, 4, 0, 1, 1)

        self.unitlbl_Vmaxapplied = QLabel(self.val_gridgroupBox)
        self.unitlbl_Vmaxapplied.setObjectName(u"unitlbl_Vmaxapplied")
        self.unitlbl_Vmaxapplied.setMinimumSize(QSize(0, 25))
        self.unitlbl_Vmaxapplied.setMaximumSize(QSize(50, 30))
        self.unitlbl_Vmaxapplied.setFont(font1)
        self.unitlbl_Vmaxapplied.setMargin(0)

        self.gridLayout_2.addWidget(self.unitlbl_Vmaxapplied, 3, 2, 1, 1)

        self.unitlbl_Prated = QLabel(self.val_gridgroupBox)
        self.unitlbl_Prated.setObjectName(u"unitlbl_Prated")
        self.unitlbl_Prated.setMinimumSize(QSize(0, 25))
        self.unitlbl_Prated.setMaximumSize(QSize(50, 30))
        self.unitlbl_Prated.setFont(font1)

        self.gridLayout_2.addWidget(self.unitlbl_Prated, 2, 6, 1, 1)

        self.hspacer_row1_middle = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row1_middle, 2, 3, 1, 1)

        self.unitlbl_T0 = QLabel(self.val_gridgroupBox)
        self.unitlbl_T0.setObjectName(u"unitlbl_T0")
        self.unitlbl_T0.setMinimumSize(QSize(0, 25))
        self.unitlbl_T0.setMaximumSize(QSize(50, 30))
        self.unitlbl_T0.setFont(font1)

        self.gridLayout_2.addWidget(self.unitlbl_T0, 5, 6, 1, 1)

        self.input_R = QLineEdit(self.val_gridgroupBox)
        self.input_R.setObjectName(u"input_R")
        self.input_R.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.input_R.sizePolicy().hasHeightForWidth())
        self.input_R.setSizePolicy(sizePolicy1)
        self.input_R.setMinimumSize(QSize(0, 25))
        self.input_R.setMaximumSize(QSize(200, 30))
        self.input_R.setFont(font2)
        self.input_R.setLayoutDirection(Qt.RightToLeft)
        self.input_R.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_R.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_R, 2, 1, 1, 1)

        self.hspacer_row3_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row3_right, 4, 7, 1, 1)

        self.unitlbl_Tbase = QLabel(self.val_gridgroupBox)
        self.unitlbl_Tbase.setObjectName(u"unitlbl_Tbase")
        self.unitlbl_Tbase.setMinimumSize(QSize(0, 25))
        self.unitlbl_Tbase.setMaximumSize(QSize(50, 30))
        self.unitlbl_Tbase.setFont(font1)
        self.unitlbl_Tbase.setMargin(0)

        self.gridLayout_2.addWidget(self.unitlbl_Tbase, 4, 2, 1, 1)

        self.input_T0 = QLineEdit(self.val_gridgroupBox)
        self.input_T0.setObjectName(u"input_T0")
        sizePolicy1.setHeightForWidth(self.input_T0.sizePolicy().hasHeightForWidth())
        self.input_T0.setSizePolicy(sizePolicy1)
        self.input_T0.setMinimumSize(QSize(0, 25))
        self.input_T0.setMaximumSize(QSize(200, 30))
        self.input_T0.setFont(font2)
        self.input_T0.setLayoutDirection(Qt.RightToLeft)
        self.input_T0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.input_T0, 5, 5, 1, 1)

        self.lbl_T0 = QLabel(self.val_gridgroupBox)
        self.lbl_T0.setObjectName(u"lbl_T0")
        self.lbl_T0.setMinimumSize(QSize(0, 25))
        self.lbl_T0.setMaximumSize(QSize(120, 30))
        self.lbl_T0.setFont(font1)
        self.lbl_T0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_T0, 5, 4, 1, 1)

        self.input_Vmaxapplied = QLineEdit(self.val_gridgroupBox)
        self.input_Vmaxapplied.setObjectName(u"input_Vmaxapplied")
        sizePolicy1.setHeightForWidth(self.input_Vmaxapplied.sizePolicy().hasHeightForWidth())
        self.input_Vmaxapplied.setSizePolicy(sizePolicy1)
        self.input_Vmaxapplied.setMinimumSize(QSize(0, 25))
        self.input_Vmaxapplied.setMaximumSize(QSize(200, 30))
        self.input_Vmaxapplied.setFont(font2)
        self.input_Vmaxapplied.setLayoutDirection(Qt.RightToLeft)
        self.input_Vmaxapplied.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_Vmaxapplied.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_Vmaxapplied, 3, 1, 1, 1)

        self.input_ThetaR = QLineEdit(self.val_gridgroupBox)
        self.input_ThetaR.setObjectName(u"input_ThetaR")
        sizePolicy1.setHeightForWidth(self.input_ThetaR.sizePolicy().hasHeightForWidth())
        self.input_ThetaR.setSizePolicy(sizePolicy1)
        self.input_ThetaR.setMinimumSize(QSize(0, 25))
        self.input_ThetaR.setMaximumSize(QSize(200, 30))
        self.input_ThetaR.setFont(font2)
        self.input_ThetaR.setLayoutDirection(Qt.RightToLeft)
        self.input_ThetaR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.input_ThetaR, 4, 5, 1, 1)

        self.input_Trated = QLineEdit(self.val_gridgroupBox)
        self.input_Trated.setObjectName(u"input_Trated")
        sizePolicy1.setHeightForWidth(self.input_Trated.sizePolicy().hasHeightForWidth())
        self.input_Trated.setSizePolicy(sizePolicy1)
        self.input_Trated.setMinimumSize(QSize(0, 25))
        self.input_Trated.setMaximumSize(QSize(200, 30))
        self.input_Trated.setFont(font2)
        self.input_Trated.setLayoutDirection(Qt.RightToLeft)
        self.input_Trated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_Trated.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_Trated, 5, 1, 1, 1)

        self.unitlbl_Vrated = QLabel(self.val_gridgroupBox)
        self.unitlbl_Vrated.setObjectName(u"unitlbl_Vrated")
        self.unitlbl_Vrated.setMinimumSize(QSize(0, 25))
        self.unitlbl_Vrated.setMaximumSize(QSize(50, 30))
        self.unitlbl_Vrated.setFont(font1)

        self.gridLayout_2.addWidget(self.unitlbl_Vrated, 3, 6, 1, 1)

        self.lbl_Prated = QLabel(self.val_gridgroupBox)
        self.lbl_Prated.setObjectName(u"lbl_Prated")
        self.lbl_Prated.setMinimumSize(QSize(0, 25))
        self.lbl_Prated.setMaximumSize(QSize(120, 30))
        self.lbl_Prated.setFont(font1)
        self.lbl_Prated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_Prated, 2, 4, 1, 1)

        self.hspacer_row2_right = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row2_right, 3, 7, 1, 1)

        self.input_Vrated = QLineEdit(self.val_gridgroupBox)
        self.input_Vrated.setObjectName(u"input_Vrated")
        sizePolicy1.setHeightForWidth(self.input_Vrated.sizePolicy().hasHeightForWidth())
        self.input_Vrated.setSizePolicy(sizePolicy1)
        self.input_Vrated.setMinimumSize(QSize(0, 25))
        self.input_Vrated.setMaximumSize(QSize(200, 30))
        self.input_Vrated.setFont(font2)
        self.input_Vrated.setLayoutDirection(Qt.RightToLeft)
        self.input_Vrated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.input_Vrated, 3, 5, 1, 1)

        self.input_Prated = QLineEdit(self.val_gridgroupBox)
        self.input_Prated.setObjectName(u"input_Prated")
        sizePolicy1.setHeightForWidth(self.input_Prated.sizePolicy().hasHeightForWidth())
        self.input_Prated.setSizePolicy(sizePolicy1)
        self.input_Prated.setMinimumSize(QSize(0, 25))
        self.input_Prated.setMaximumSize(QSize(200, 30))
        self.input_Prated.setFont(font2)
        self.input_Prated.setLayoutDirection(Qt.RightToLeft)
        self.input_Prated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.input_Prated, 2, 5, 1, 1)


        self.verticalLayout.addWidget(self.val_gridgroupBox)

        self.vspacer_bottom = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.vspacer_bottom)

        self.groupBox_notes = QGroupBox(ResistorWidget)
        self.groupBox_notes.setObjectName(u"groupBox_notes")
        sizePolicy.setHeightForWidth(self.groupBox_notes.sizePolicy().hasHeightForWidth())
        self.groupBox_notes.setSizePolicy(sizePolicy)
        self.groupBox_notes.setMinimumSize(QSize(450, 0))
        self.groupBox_notes.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_notes.setFont(font)
        self.groupBox_notes.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_notes.setFlat(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_notes)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.textedit_notes = QPlainTextEdit(self.groupBox_notes)
        self.textedit_notes.setObjectName(u"textedit_notes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textedit_notes.sizePolicy().hasHeightForWidth())
        self.textedit_notes.setSizePolicy(sizePolicy2)
        self.textedit_notes.setMinimumSize(QSize(0, 0))
        self.textedit_notes.setMaximumSize(QSize(1000, 16777215))
        self.textedit_notes.setFont(font2)
        self.textedit_notes.setTabChangesFocus(True)

        self.horizontalLayout_3.addWidget(self.textedit_notes)


        self.verticalLayout.addWidget(self.groupBox_notes)

        QWidget.setTabOrder(self.combo_type, self.btn_type)
        QWidget.setTabOrder(self.btn_type, self.input_mpn)
        QWidget.setTabOrder(self.input_mpn, self.input_apn)
        QWidget.setTabOrder(self.input_apn, self.input_R)
        QWidget.setTabOrder(self.input_R, self.input_Prated)
        QWidget.setTabOrder(self.input_Prated, self.input_Vmaxapplied)
        QWidget.setTabOrder(self.input_Vmaxapplied, self.input_Vrated)
        QWidget.setTabOrder(self.input_Vrated, self.input_Tbase)
        QWidget.setTabOrder(self.input_Tbase, self.input_ThetaR)
        QWidget.setTabOrder(self.input_ThetaR, self.input_Trated)
        QWidget.setTabOrder(self.input_Trated, self.input_T0)
        QWidget.setTabOrder(self.input_T0, self.textedit_notes)

        self.retranslateUi(ResistorWidget)

        QMetaObject.connectSlotsByName(ResistorWidget)
    # setupUi

    def retranslateUi(self, ResistorWidget):
        ResistorWidget.setWindowTitle(QCoreApplication.translate("ResistorWidget", u"Form", None))
        self.groupbox_pntype.setTitle(QCoreApplication.translate("ResistorWidget", u"PNs and Style", None))
        self.lbl_type.setText(QCoreApplication.translate("ResistorWidget", u"Style: ", None))
        self.combo_type.setItemText(0, QCoreApplication.translate("ResistorWidget", u"TEST", None))

#if QT_CONFIG(tooltip)
        self.combo_type.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor style", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_type.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor style selection help", None))
#endif // QT_CONFIG(tooltip)
        self.btn_type.setText("")
        self.lbl_mpn.setText(QCoreApplication.translate("ResistorWidget", u"MPN:", None))
#if QT_CONFIG(tooltip)
        self.input_mpn.setToolTip(QCoreApplication.translate("ResistorWidget", u"Manufacturer part number", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_apn.setText(QCoreApplication.translate("ResistorWidget", u"APN:", None))
#if QT_CONFIG(tooltip)
        self.input_apn.setToolTip(QCoreApplication.translate("ResistorWidget", u"Alternate part number", None))
#endif // QT_CONFIG(tooltip)
        self.val_gridgroupBox.setTitle(QCoreApplication.translate("ResistorWidget", u"Component Values", None))
        self.lbl_Vrated.setText(QCoreApplication.translate("ResistorWidget", u"Vmax_Rated: ", None))
        self.lbl_R.setText(QCoreApplication.translate("ResistorWidget", u"R: ", None))
        self.unitlbl_Trated.setText(QCoreApplication.translate("ResistorWidget", u"degC", None))
        self.lbl_ThetaR.setText(QCoreApplication.translate("ResistorWidget", u"Theta_R: ", None))
        self.lbl_Trated.setText(QCoreApplication.translate("ResistorWidget", u"T_Rated: ", None))
        self.lbl_Vmaxapplied.setText(QCoreApplication.translate("ResistorWidget", u"DV_Max: ", None))
        self.unitlbl_R.setText(QCoreApplication.translate("ResistorWidget", u"Ohm", None))
        self.unitlbl_ThetaR.setText(QCoreApplication.translate("ResistorWidget", u"degC/W", None))
#if QT_CONFIG(tooltip)
        self.input_Tbase.setToolTip(QCoreApplication.translate("ResistorWidget", u"Baseplate temperature, in degC, with SI prefixes (i.e., 68)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_Tbase.setText(QCoreApplication.translate("ResistorWidget", u"T_Baseplate: ", None))
        self.unitlbl_Vmaxapplied.setText(QCoreApplication.translate("ResistorWidget", u"V", None))
        self.unitlbl_Prated.setText(QCoreApplication.translate("ResistorWidget", u"W", None))
        self.unitlbl_T0.setText(QCoreApplication.translate("ResistorWidget", u"degC", None))
#if QT_CONFIG(tooltip)
        self.input_R.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistance, in omega, with SI prefixes (i.e., 10k)", None))
#endif // QT_CONFIG(tooltip)
        self.unitlbl_Tbase.setText(QCoreApplication.translate("ResistorWidget", u"degC", None))
#if QT_CONFIG(tooltip)
        self.input_T0.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor's zero-power T, in degC, with SI prefixes (i.e., 68)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_T0.setText(QCoreApplication.translate("ResistorWidget", u"T0: ", None))
#if QT_CONFIG(tooltip)
        self.input_Vmaxapplied.setToolTip(QCoreApplication.translate("ResistorWidget", u"Max V across the resistor, in volts, with SI prefixes (i.e., 25m)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input_ThetaR.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor's thermal resistance, in degC/W, with SI prefixes (i.e., 2.3)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input_Trated.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor's rated T, in degC, with SI prefixes (i.e., 150)", None))
#endif // QT_CONFIG(tooltip)
        self.unitlbl_Vrated.setText(QCoreApplication.translate("ResistorWidget", u"V", None))
        self.lbl_Prated.setText(QCoreApplication.translate("ResistorWidget", u"P_Rated: ", None))
#if QT_CONFIG(tooltip)
        self.input_Vrated.setToolTip(QCoreApplication.translate("ResistorWidget", u"Resistor's max rated V, in volts, with SI prefixes (i.e., 200)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input_Prated.setToolTip(QCoreApplication.translate("ResistorWidget", u"Power rating, in watts, with SI prefixes (i.e., 63m)", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_notes.setTitle(QCoreApplication.translate("ResistorWidget", u"User Notes", None))
#if QT_CONFIG(tooltip)
        self.textedit_notes.setToolTip(QCoreApplication.translate("ResistorWidget", u"User notes, can be anything. Separate each note by a linebreak.", None))
#endif // QT_CONFIG(tooltip)
        self.textedit_notes.setDocumentTitle("")
    # retranslateUi

