# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 326)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_new.setFont(font)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_open.setFont(font)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setFont(font)
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_saveas.setFont(font)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_exit.setFont(font)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about.setFont(font)
        self.action_documentation = QAction(MainWindow)
        self.action_documentation.setObjectName(u"action_documentation")
        self.action_documentation.setFont(font)
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        self.action_import.setFont(font)
        self.action_exportcsv = QAction(MainWindow)
        self.action_exportcsv.setObjectName(u"action_exportcsv")
        self.action_exportcsv.setFont(font)
        self.action_exporttxt = QAction(MainWindow)
        self.action_exporttxt.setObjectName(u"action_exporttxt")
        self.action_exporttxt.setFont(font)
        self.action_info_all = QAction(MainWindow)
        self.action_info_all.setObjectName(u"action_info_all")
        self.action_info_all.setFont(font)
        self.action_info_capacitor = QAction(MainWindow)
        self.action_info_capacitor.setObjectName(u"action_info_capacitor")
        self.action_info_capacitor.setFont(font)
        self.action_info_inductor = QAction(MainWindow)
        self.action_info_inductor.setObjectName(u"action_info_inductor")
        self.action_info_inductor.setFont(font)
        self.action_info_resistor = QAction(MainWindow)
        self.action_info_resistor.setObjectName(u"action_info_resistor")
        self.action_info_resistor.setFont(font)
        self.action_run_epsa_calc = QAction(MainWindow)
        self.action_run_epsa_calc.setObjectName(u"action_run_epsa_calc")
        self.action_preferences = QAction(MainWindow)
        self.action_preferences.setObjectName(u"action_preferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 0)
        self.vframe_left = QFrame(self.centralwidget)
        self.vframe_left.setObjectName(u"vframe_left")
        self.vframe_left.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(10)
        self.vframe_left.setFont(font1)
        self.vframe_left.setAutoFillBackground(False)
        self.vframe_left.setStyleSheet(u"")
        self.vframe_left.setFrameShape(QFrame.WinPanel)
        self.vframe_left.setFrameShadow(QFrame.Sunken)
        self.vframe_left.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.vframe_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 7)
        self.lbl_comptree = QLabel(self.vframe_left)
        self.lbl_comptree.setObjectName(u"lbl_comptree")
        font2 = QFont()
        font2.setFamilies([u"Liberation Sans"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lbl_comptree.setFont(font2)
        self.lbl_comptree.setStyleSheet(u"")
        self.lbl_comptree.setTextFormat(Qt.RichText)
        self.lbl_comptree.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.lbl_comptree)

        self.comptree = QTreeWidget(self.vframe_left)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Ref Des");
        self.comptree.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.comptree)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.comptree)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.comptree)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.comptree.setObjectName(u"comptree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comptree.sizePolicy().hasHeightForWidth())
        self.comptree.setSizePolicy(sizePolicy1)
        self.comptree.setMinimumSize(QSize(150, 0))
        self.comptree.setMaximumSize(QSize(250, 16777215))
        self.comptree.setStyleSheet(u"")
        self.comptree.setFrameShape(QFrame.WinPanel)
        self.comptree.setFrameShadow(QFrame.Raised)
        self.comptree.setLineWidth(5)
        self.comptree.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.comptree.setTabKeyNavigation(True)
        self.comptree.setAlternatingRowColors(False)
        self.comptree.setIconSize(QSize(5, 5))
        self.comptree.setSortingEnabled(True)
        self.comptree.setAnimated(True)
        self.comptree.setAllColumnsShowFocus(False)
        self.comptree.setHeaderHidden(False)
        self.comptree.header().setVisible(True)
        self.comptree.header().setCascadingSectionResizes(True)
        self.comptree.header().setHighlightSections(False)
        self.comptree.header().setProperty("showSortIndicator", True)

        self.verticalLayout_2.addWidget(self.comptree)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_delcomp = QPushButton(self.vframe_left)
        self.btn_delcomp.setObjectName(u"btn_delcomp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_delcomp.sizePolicy().hasHeightForWidth())
        self.btn_delcomp.setSizePolicy(sizePolicy2)
        self.btn_delcomp.setMinimumSize(QSize(80, 20))
        self.btn_delcomp.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setFamilies([u"Liberation Sans"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.btn_delcomp.setFont(font3)
        self.btn_delcomp.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_delcomp)

        self.btn_newcomp = QPushButton(self.vframe_left)
        self.btn_newcomp.setObjectName(u"btn_newcomp")
        sizePolicy2.setHeightForWidth(self.btn_newcomp.sizePolicy().hasHeightForWidth())
        self.btn_newcomp.setSizePolicy(sizePolicy2)
        self.btn_newcomp.setMinimumSize(QSize(80, 20))
        self.btn_newcomp.setMaximumSize(QSize(100, 40))
        self.btn_newcomp.setFont(font3)
        self.btn_newcomp.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_newcomp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.vframe_left)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.vframe_right = QFrame(self.centralwidget)
        self.vframe_right.setObjectName(u"vframe_right")
        self.vframe_right.setMinimumSize(QSize(550, 0))
        self.vframe_right.setFont(font1)
        self.vframe_right.setStyleSheet(u"")
        self.vframe_right.setFrameShape(QFrame.WinPanel)
        self.vframe_right.setFrameShadow(QFrame.Sunken)
        self.vframe_right.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.vframe_right)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_compinfo = QFrame(self.vframe_right)
        self.frame_compinfo.setObjectName(u"frame_compinfo")
        sizePolicy2.setHeightForWidth(self.frame_compinfo.sizePolicy().hasHeightForWidth())
        self.frame_compinfo.setSizePolicy(sizePolicy2)
        self.frame_compinfo.setMinimumSize(QSize(300, 50))
        self.frame_compinfo.setMaximumSize(QSize(16777215, 80))
        self.frame_compinfo.setFrameShape(QFrame.StyledPanel)
        self.frame_compinfo.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame_compinfo)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.lbl_compinfo = QLabel(self.frame_compinfo)
        self.lbl_compinfo.setObjectName(u"lbl_compinfo")
        sizePolicy2.setHeightForWidth(self.lbl_compinfo.sizePolicy().hasHeightForWidth())
        self.lbl_compinfo.setSizePolicy(sizePolicy2)
        self.lbl_compinfo.setMinimumSize(QSize(30, 20))
        self.lbl_compinfo.setMaximumSize(QSize(16777215, 25))
        self.lbl_compinfo.setFont(font2)
        self.lbl_compinfo.setStyleSheet(u"")
        self.lbl_compinfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_compinfo)

        self.hspacer_compinfo = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hspacer_compinfo)

        self.btn_prevcomp = QPushButton(self.frame_compinfo)
        self.btn_prevcomp.setObjectName(u"btn_prevcomp")
        sizePolicy2.setHeightForWidth(self.btn_prevcomp.sizePolicy().hasHeightForWidth())
        self.btn_prevcomp.setSizePolicy(sizePolicy2)
        self.btn_prevcomp.setMinimumSize(QSize(100, 20))
        self.btn_prevcomp.setMaximumSize(QSize(125, 40))
        self.btn_prevcomp.setFont(font3)
        self.btn_prevcomp.setStyleSheet(u"")
        self.btn_prevcomp.setIconSize(QSize(12, 12))

        self.horizontalLayout.addWidget(self.btn_prevcomp)

        self.btn_nextcomp = QPushButton(self.frame_compinfo)
        self.btn_nextcomp.setObjectName(u"btn_nextcomp")
        sizePolicy2.setHeightForWidth(self.btn_nextcomp.sizePolicy().hasHeightForWidth())
        self.btn_nextcomp.setSizePolicy(sizePolicy2)
        self.btn_nextcomp.setMinimumSize(QSize(100, 20))
        self.btn_nextcomp.setMaximumSize(QSize(125, 40))
        self.btn_nextcomp.setFont(font3)
        self.btn_nextcomp.setLayoutDirection(Qt.RightToLeft)
        self.btn_nextcomp.setStyleSheet(u"")
        self.btn_nextcomp.setIconSize(QSize(12, 12))

        self.horizontalLayout.addWidget(self.btn_nextcomp)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_compdefault = QPushButton(self.frame_compinfo)
        self.btn_compdefault.setObjectName(u"btn_compdefault")
        sizePolicy2.setHeightForWidth(self.btn_compdefault.sizePolicy().hasHeightForWidth())
        self.btn_compdefault.setSizePolicy(sizePolicy2)
        self.btn_compdefault.setMinimumSize(QSize(100, 20))
        self.btn_compdefault.setMaximumSize(QSize(125, 40))
        self.btn_compdefault.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_compdefault)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_compinfo)

        self.vspacer_right_top = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.vspacer_right_top)

        self.main_frame = QFrame(self.vframe_right)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy3)
        self.main_frame.setMinimumSize(QSize(300, 200))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.main_frame)


        self.horizontalLayout_2.addWidget(self.vframe_right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 821, 17))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_exportas = QMenu(self.menu_file)
        self.menu_exportas.setObjectName(u"menu_exportas")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_calculate = QMenu(self.menubar)
        self.menu_calculate.setObjectName(u"menu_calculate")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_calculate.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_saveas)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_import)
        self.menu_file.addAction(self.menu_exportas.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_preferences)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_exportas.addAction(self.action_exportcsv)
        self.menu_exportas.addAction(self.action_exporttxt)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_documentation)
        self.menu_calculate.addAction(self.action_run_epsa_calc)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EPSA Wizard", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
#if QT_CONFIG(tooltip)
        self.action_new.setToolTip(QCoreApplication.translate("MainWindow", u"Create a new EPSA file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(tooltip)
        self.action_open.setToolTip(QCoreApplication.translate("MainWindow", u"Open an EPSA file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.action_save.setToolTip(QCoreApplication.translate("MainWindow", u"Save the current EPSA file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(tooltip)
        self.action_saveas.setToolTip(QCoreApplication.translate("MainWindow", u"Save the current EPSA file as...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_saveas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_documentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
#if QT_CONFIG(shortcut)
        self.action_documentation.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+/", None))
#endif // QT_CONFIG(shortcut)
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"Import...", None))
        self.action_exportcsv.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.action_exporttxt.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.action_info_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.action_info_capacitor.setText(QCoreApplication.translate("MainWindow", u"Capacitors", None))
        self.action_info_inductor.setText(QCoreApplication.translate("MainWindow", u"Inductors", None))
        self.action_info_resistor.setText(QCoreApplication.translate("MainWindow", u"Resistors", None))
        self.action_run_epsa_calc.setText(QCoreApplication.translate("MainWindow", u"Run EPSA Calculation", None))
#if QT_CONFIG(shortcut)
        self.action_run_epsa_calc.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_preferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.lbl_comptree.setText(QCoreApplication.translate("MainWindow", u"Component Tree", None))
        ___qtreewidgetitem = self.comptree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"MPN", None));

        __sortingEnabled = self.comptree.isSortingEnabled()
        self.comptree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.comptree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Resistors", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"R9", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"R7", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"R5", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"R4", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"R3", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"R2", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem1.child(6)
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"R17", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem1.child(7)
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"R10", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem1.child(8)
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"R1", None));
        ___qtreewidgetitem11 = self.comptree.topLevelItem(1)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Inductors", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"L3", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"L16", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem11.child(2)
        ___qtreewidgetitem14.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"L15", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem11.child(3)
        ___qtreewidgetitem15.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"L1", None));
        ___qtreewidgetitem16 = self.comptree.topLevelItem(2)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Capacitors", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"C6", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem16.child(1)
        ___qtreewidgetitem18.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"C5", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem16.child(2)
        ___qtreewidgetitem19.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"C4", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem16.child(3)
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"C3", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem16.child(4)
        ___qtreewidgetitem21.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"C2", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem16.child(5)
        ___qtreewidgetitem22.setText(1, QCoreApplication.translate("MainWindow", u"xxxxxx", None));
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"C1", None));
        self.comptree.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.btn_delcomp.setToolTip(QCoreApplication.translate("MainWindow", u"Delete the current component", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delcomp.setText(QCoreApplication.translate("MainWindow", u"  Delete", None))
#if QT_CONFIG(shortcut)
        self.btn_delcomp.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_newcomp.setToolTip(QCoreApplication.translate("MainWindow", u"Create a new component", None))
#endif // QT_CONFIG(tooltip)
        self.btn_newcomp.setText(QCoreApplication.translate("MainWindow", u"  New", None))
#if QT_CONFIG(shortcut)
        self.btn_newcomp.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.frame_compinfo.setStyleSheet("")
        self.lbl_compinfo.setText(QCoreApplication.translate("MainWindow", u"Component Information", None))
        self.btn_prevcomp.setText(QCoreApplication.translate("MainWindow", u"  Prev", None))
        self.btn_nextcomp.setText(QCoreApplication.translate("MainWindow", u"Next  ", None))
        self.btn_compdefault.setText(QCoreApplication.translate("MainWindow", u"  Defaults", None))
        self.main_frame.setStyleSheet("")
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_exportas.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_calculate.setTitle(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi

