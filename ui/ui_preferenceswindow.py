# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(500, 422)
        MainWindow.setMaximumSize(QSize(700, 16777215))
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 400))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabwidget_preferences = QTabWidget(self.centralwidget)
        self.tabwidget_preferences.setObjectName(u"tabwidget_preferences")
        self.tabwidget_preferences.setFont(font)
        self.tabwidget_preferences.setTabPosition(QTabWidget.North)
        self.tabwidget_preferences.setTabShape(QTabWidget.Rounded)
        self.tabwidget_preferences.setMovable(False)
        self.tabwidget_preferences.setTabBarAutoHide(False)
        self.tab_application = QWidget()
        self.tab_application.setObjectName(u"tab_application")
        self.verticalLayout_7 = QVBoxLayout(self.tab_application)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollarea_application = QScrollArea(self.tab_application)
        self.scrollarea_application.setObjectName(u"scrollarea_application")
        self.scrollarea_application.setWidgetResizable(True)
        self.scrollwidget_application = QWidget()
        self.scrollwidget_application.setObjectName(u"scrollwidget_application")
        self.scrollwidget_application.setGeometry(QRect(0, 0, 455, 326))
        self.verticalLayout_5 = QVBoxLayout(self.scrollwidget_application)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.groupbox_units = QGroupBox(self.scrollwidget_application)
        self.groupbox_units.setObjectName(u"groupbox_units")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_units.sizePolicy().hasHeightForWidth())
        self.groupbox_units.setSizePolicy(sizePolicy)
        self.groupbox_units.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupbox_units)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_unitsystem = QLabel(self.groupbox_units)
        self.lbl_unitsystem.setObjectName(u"lbl_unitsystem")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_unitsystem.sizePolicy().hasHeightForWidth())
        self.lbl_unitsystem.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.lbl_unitsystem.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbl_unitsystem)

        self.lbl_unitsystem_desc = QLabel(self.groupbox_units)
        self.lbl_unitsystem_desc.setObjectName(u"lbl_unitsystem_desc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_unitsystem_desc.sizePolicy().hasHeightForWidth())
        self.lbl_unitsystem_desc.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Liberation Sans"])
        font2.setPointSize(8)
        font2.setItalic(True)
        self.lbl_unitsystem_desc.setFont(font2)

        self.verticalLayout_6.addWidget(self.lbl_unitsystem_desc)

        self.combo_unitsystem = QComboBox(self.groupbox_units)
        self.combo_unitsystem.addItem("")
        self.combo_unitsystem.addItem("")
        self.combo_unitsystem.addItem("")
        self.combo_unitsystem.setObjectName(u"combo_unitsystem")
        sizePolicy2.setHeightForWidth(self.combo_unitsystem.sizePolicy().hasHeightForWidth())
        self.combo_unitsystem.setSizePolicy(sizePolicy2)
        self.combo_unitsystem.setMaximumSize(QSize(200, 40))
        font3 = QFont()
        font3.setFamilies([u"Liberation Sans"])
        font3.setPointSize(10)
        self.combo_unitsystem.setFont(font3)
        self.combo_unitsystem.setFocusPolicy(Qt.StrongFocus)
        self.combo_unitsystem.setFrame(True)

        self.verticalLayout_6.addWidget(self.combo_unitsystem)

        self.lbl_lengthtype = QLabel(self.groupbox_units)
        self.lbl_lengthtype.setObjectName(u"lbl_lengthtype")
        sizePolicy1.setHeightForWidth(self.lbl_lengthtype.sizePolicy().hasHeightForWidth())
        self.lbl_lengthtype.setSizePolicy(sizePolicy1)
        self.lbl_lengthtype.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbl_lengthtype)

        self.combo_lengthtype = QComboBox(self.groupbox_units)
        self.combo_lengthtype.addItem("")
        self.combo_lengthtype.addItem("")
        self.combo_lengthtype.setObjectName(u"combo_lengthtype")
        sizePolicy2.setHeightForWidth(self.combo_lengthtype.sizePolicy().hasHeightForWidth())
        self.combo_lengthtype.setSizePolicy(sizePolicy2)
        self.combo_lengthtype.setMaximumSize(QSize(200, 40))
        self.combo_lengthtype.setFont(font3)
        self.combo_lengthtype.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_6.addWidget(self.combo_lengthtype)

        self.lbl_temptype = QLabel(self.groupbox_units)
        self.lbl_temptype.setObjectName(u"lbl_temptype")
        sizePolicy1.setHeightForWidth(self.lbl_temptype.sizePolicy().hasHeightForWidth())
        self.lbl_temptype.setSizePolicy(sizePolicy1)
        self.lbl_temptype.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbl_temptype)

        self.combo_temptype = QComboBox(self.groupbox_units)
        self.combo_temptype.addItem("")
        self.combo_temptype.addItem("")
        self.combo_temptype.addItem("")
        self.combo_temptype.setObjectName(u"combo_temptype")
        sizePolicy2.setHeightForWidth(self.combo_temptype.sizePolicy().hasHeightForWidth())
        self.combo_temptype.setSizePolicy(sizePolicy2)
        self.combo_temptype.setMaximumSize(QSize(200, 40))
        self.combo_temptype.setFont(font3)
        self.combo_temptype.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_6.addWidget(self.combo_temptype)

        self.lbl_masstype = QLabel(self.groupbox_units)
        self.lbl_masstype.setObjectName(u"lbl_masstype")
        sizePolicy1.setHeightForWidth(self.lbl_masstype.sizePolicy().hasHeightForWidth())
        self.lbl_masstype.setSizePolicy(sizePolicy1)
        self.lbl_masstype.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbl_masstype)

        self.combo_masstype = QComboBox(self.groupbox_units)
        self.combo_masstype.addItem("")
        self.combo_masstype.addItem("")
        self.combo_masstype.setObjectName(u"combo_masstype")
        sizePolicy2.setHeightForWidth(self.combo_masstype.sizePolicy().hasHeightForWidth())
        self.combo_masstype.setSizePolicy(sizePolicy2)
        self.combo_masstype.setMaximumSize(QSize(200, 40))
        self.combo_masstype.setFont(font3)
        self.combo_masstype.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_6.addWidget(self.combo_masstype)

        self.vspacer_units = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.vspacer_units)


        self.verticalLayout_5.addWidget(self.groupbox_units)

        self.groupbox_debug = QGroupBox(self.scrollwidget_application)
        self.groupbox_debug.setObjectName(u"groupbox_debug")
        self.groupbox_debug.setMaximumSize(QSize(380, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.groupbox_debug)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_debug_desc = QLabel(self.groupbox_debug)
        self.lbl_debug_desc.setObjectName(u"lbl_debug_desc")
        self.lbl_debug_desc.setFont(font2)

        self.verticalLayout_8.addWidget(self.lbl_debug_desc)

        self.checkbox_debug = QCheckBox(self.groupbox_debug)
        self.checkbox_debug.setObjectName(u"checkbox_debug")
        self.checkbox_debug.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkbox_debug)


        self.verticalLayout_5.addWidget(self.groupbox_debug)

        self.scrollarea_application.setWidget(self.scrollwidget_application)

        self.verticalLayout_7.addWidget(self.scrollarea_application)

        self.tabwidget_preferences.addTab(self.tab_application, "")
        self.tab_user = QWidget()
        self.tab_user.setObjectName(u"tab_user")
        self.verticalLayout_2 = QVBoxLayout(self.tab_user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollarea_user = QScrollArea(self.tab_user)
        self.scrollarea_user.setObjectName(u"scrollarea_user")
        self.scrollarea_user.setWidgetResizable(True)
        self.scrollwidget_user = QWidget()
        self.scrollwidget_user.setObjectName(u"scrollwidget_user")
        self.scrollwidget_user.setGeometry(QRect(0, 0, 466, 315))
        self.verticalLayout_3 = QVBoxLayout(self.scrollwidget_user)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_userinfo = QGroupBox(self.scrollwidget_user)
        self.group_userinfo.setObjectName(u"group_userinfo")
        sizePolicy.setHeightForWidth(self.group_userinfo.sizePolicy().hasHeightForWidth())
        self.group_userinfo.setSizePolicy(sizePolicy)
        self.group_userinfo.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.group_userinfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_info_desc = QLabel(self.group_userinfo)
        self.lbl_info_desc.setObjectName(u"lbl_info_desc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_info_desc.sizePolicy().hasHeightForWidth())
        self.lbl_info_desc.setSizePolicy(sizePolicy3)
        self.lbl_info_desc.setMinimumSize(QSize(0, 10))
        self.lbl_info_desc.setMaximumSize(QSize(16777215, 10))
        self.lbl_info_desc.setFont(font2)

        self.verticalLayout_4.addWidget(self.lbl_info_desc)

        self.lbl_username = QLabel(self.group_userinfo)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_username)

        self.input_username = QLineEdit(self.group_userinfo)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setMaximumSize(QSize(300, 20))
        self.input_username.setFont(font3)

        self.verticalLayout_4.addWidget(self.input_username)

        self.lbl_userorg = QLabel(self.group_userinfo)
        self.lbl_userorg.setObjectName(u"lbl_userorg")
        self.lbl_userorg.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_userorg)

        self.input_userorg = QLineEdit(self.group_userinfo)
        self.input_userorg.setObjectName(u"input_userorg")
        self.input_userorg.setMaximumSize(QSize(300, 20))
        self.input_userorg.setFont(font3)

        self.verticalLayout_4.addWidget(self.input_userorg)

        self.lbl_usertitle = QLabel(self.group_userinfo)
        self.lbl_usertitle.setObjectName(u"lbl_usertitle")
        self.lbl_usertitle.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_usertitle)

        self.input_usertitle = QLineEdit(self.group_userinfo)
        self.input_usertitle.setObjectName(u"input_usertitle")
        self.input_usertitle.setMaximumSize(QSize(300, 20))
        self.input_usertitle.setFont(font3)

        self.verticalLayout_4.addWidget(self.input_usertitle)

        self.vspacer_userinfo = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.vspacer_userinfo)


        self.verticalLayout_3.addWidget(self.group_userinfo)

        self.scrollarea_user.setWidget(self.scrollwidget_user)

        self.verticalLayout_2.addWidget(self.scrollarea_user)

        self.tabwidget_preferences.addTab(self.tab_user, "")

        self.verticalLayout.addWidget(self.tabwidget_preferences)

        self.btnbox_main = QDialogButtonBox(self.centralwidget)
        self.btnbox_main.setObjectName(u"btnbox_main")
        self.btnbox_main.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Close)
        self.btnbox_main.setCenterButtons(False)

        self.verticalLayout.addWidget(self.btnbox_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabwidget_preferences, self.scrollarea_application)
        QWidget.setTabOrder(self.scrollarea_application, self.combo_unitsystem)
        QWidget.setTabOrder(self.combo_unitsystem, self.combo_lengthtype)
        QWidget.setTabOrder(self.combo_lengthtype, self.combo_temptype)
        QWidget.setTabOrder(self.combo_temptype, self.combo_masstype)
        QWidget.setTabOrder(self.combo_masstype, self.scrollarea_user)
        QWidget.setTabOrder(self.scrollarea_user, self.input_username)
        QWidget.setTabOrder(self.input_username, self.input_userorg)
        QWidget.setTabOrder(self.input_userorg, self.input_usertitle)
        QWidget.setTabOrder(self.input_usertitle, self.checkbox_debug)

        self.retranslateUi(MainWindow)

        self.tabwidget_preferences.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EPSA Wizard Preferences", None))
        self.groupbox_units.setTitle(QCoreApplication.translate("MainWindow", u"Units", None))
        self.lbl_unitsystem.setText(QCoreApplication.translate("MainWindow", u"Unit System", None))
        self.lbl_unitsystem_desc.setText(QCoreApplication.translate("MainWindow", u"unit_system_description", None))
        self.combo_unitsystem.setItemText(0, QCoreApplication.translate("MainWindow", u"Metric", None))
        self.combo_unitsystem.setItemText(1, QCoreApplication.translate("MainWindow", u"Imperial", None))
        self.combo_unitsystem.setItemText(2, QCoreApplication.translate("MainWindow", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.combo_unitsystem.setToolTip(QCoreApplication.translate("MainWindow", u"Unit system", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_lengthtype.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.combo_lengthtype.setItemText(0, QCoreApplication.translate("MainWindow", u"meter (m, mm, etc.)", None))
        self.combo_lengthtype.setItemText(1, QCoreApplication.translate("MainWindow", u"foot (ft, in, thou)", None))

#if QT_CONFIG(tooltip)
        self.combo_lengthtype.setToolTip(QCoreApplication.translate("MainWindow", u"Length type", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_temptype.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.combo_temptype.setItemText(0, QCoreApplication.translate("MainWindow", u"degC", None))
        self.combo_temptype.setItemText(1, QCoreApplication.translate("MainWindow", u"degF", None))
        self.combo_temptype.setItemText(2, QCoreApplication.translate("MainWindow", u"degK", None))

#if QT_CONFIG(tooltip)
        self.combo_temptype.setToolTip(QCoreApplication.translate("MainWindow", u"Temperature type", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_masstype.setText(QCoreApplication.translate("MainWindow", u"Mass", None))
        self.combo_masstype.setItemText(0, QCoreApplication.translate("MainWindow", u"kilogram (kg, mg, etc.)", None))
        self.combo_masstype.setItemText(1, QCoreApplication.translate("MainWindow", u"pound (lb.)", None))

#if QT_CONFIG(tooltip)
        self.combo_masstype.setToolTip(QCoreApplication.translate("MainWindow", u"Mass type", None))
#endif // QT_CONFIG(tooltip)
        self.groupbox_debug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.lbl_debug_desc.setText(QCoreApplication.translate("MainWindow", u"Forces certain features and produces more verbose outputs.", None))
        self.checkbox_debug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.tabwidget_preferences.setTabText(self.tabwidget_preferences.indexOf(self.tab_application), QCoreApplication.translate("MainWindow", u"Application", None))
        self.group_userinfo.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.lbl_info_desc.setText(QCoreApplication.translate("MainWindow", u"Used in generated reports", None))
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"User's Name:", None))
        self.input_username.setText(QCoreApplication.translate("MainWindow", u"FirstName LastName", None))
        self.input_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Walter White", None))
        self.lbl_userorg.setText(QCoreApplication.translate("MainWindow", u"User's Company/Organization", None))
        self.input_userorg.setText(QCoreApplication.translate("MainWindow", u"Your Company/Org Here", None))
        self.lbl_usertitle.setText(QCoreApplication.translate("MainWindow", u"User's Title:", None))
        self.input_usertitle.setText(QCoreApplication.translate("MainWindow", u"Your Title Here", None))
        self.tabwidget_preferences.setTabText(self.tabwidget_preferences.indexOf(self.tab_user), QCoreApplication.translate("MainWindow", u"User", None))
    # retranslateUi

