from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


from utilities._program_consts import *
from utilities._settings_consts import *
from utilities.epsa_logging import epsa_logger

from src.component_defs.resistors import EPSA_Resistor, resistor_style_dict
from utilities.epsa_units import ureg, UnitQuantity

epsa_logger.debug("Imported resistor_widget.py")

_DefaultResistor = EPSA_Resistor(
    refdes="R??",
    mpn="",
    apn="",
    value=ureg("4.99kΩ"),
    power_rating=ureg("1W"),
    ΔVmax_applied=ureg("300mV"),
    T_baseplate=UnitQuantity(68.0, ureg.degC),
    θ_R=UnitQuantity(1.0e-3, ureg.degC/ureg.W),
    Vrated_max=ureg("100V"),
    T_rated=UnitQuantity(180.0, ureg.degC),
    T_zero=UnitQuantity(80.0, ureg.degC),
    user_notes=[],
    calc_notes=[],
    style=resistor_style_dict["RZ"]
)


class ResistorWidget(QWidget):
    def __init__(self, *args):
        epsa_logger.debug("Initializing ResistorWidget")
        super().__init__(*args)
        # self.setupUi()

        self._setup_ui()

    def _setup_ui(self):
        epsa_logger.info("Setting up ResistorWidget UI")
        self.resize(395, 305)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        # self.setLayout(self.verticalLayout)
        self.frame_refdes = QFrame()
        self.frame_refdes.setObjectName(u"frame_refdes")
        self.frame_refdes.setMinimumSize(QSize(0, 35))
        self.frame_refdes.setMaximumSize(QSize(16777215, 50))
        self.frame_refdes.setFrameShape(QFrame.Box)
        self.frame_refdes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_refdes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_refdes = QLabel(self.frame_refdes)
        self.label_refdes.setObjectName(u"label_refdes")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_refdes.sizePolicy().hasHeightForWidth())
        self.label_refdes.setSizePolicy(sizePolicy)
        self.label_refdes.setMinimumSize(QSize(40, 0))
        self.label_refdes.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        self.label_refdes.setFont(font)
        self.label_refdes.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_refdes)

        self.input_refdes = QLineEdit(self.frame_refdes)
        self.input_refdes.setObjectName(u"input_refdes")
        self.input_refdes.setEnabled(False)
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.input_refdes.sizePolicy().hasHeightForWidth())
        self.input_refdes.setSizePolicy(sizePolicy1)
        self.input_refdes.setMinimumSize(QSize(80, 0))
        self.input_refdes.setMaximumSize(QSize(120, 16777215))
        self.input_refdes.setFont(font)
        self.input_refdes.setMaxLength(40)
        self.input_refdes.setFrame(True)
        self.input_refdes.setDragEnabled(False)

        self.horizontalLayout.addWidget(self.input_refdes)

        self.hspacer_refdes_middle = QSpacerItem(
            10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hspacer_refdes_middle)

        self.label_resistor_style = QLabel(self.frame_refdes)
        self.label_resistor_style.setObjectName(u"label_resistor_style")
        sizePolicy.setHeightForWidth(
            self.label_resistor_style.sizePolicy().hasHeightForWidth())
        self.label_resistor_style.setSizePolicy(sizePolicy)
        self.label_resistor_style.setMinimumSize(QSize(70, 0))
        self.label_resistor_style.setMaximumSize(QSize(100, 16777215))
        self.label_resistor_style.setFont(font)
        self.label_resistor_style.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_resistor_style)

        self.btn_info_resistor_style = QPushButton(self.frame_refdes)
        self.btn_info_resistor_style.setObjectName(u"btn_info_resistor_style")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.btn_info_resistor_style.sizePolicy().hasHeightForWidth())
        self.btn_info_resistor_style.setSizePolicy(sizePolicy2)
        self.btn_info_resistor_style.setMinimumSize(QSize(20, 0))
        self.btn_info_resistor_style.setMaximumSize(QSize(20, 16777215))
        icon = QIcon()
        icon.addFile(u"./images/info_circle.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info_resistor_style.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_info_resistor_style)

        self.combo_resistor_style = QComboBox(self.frame_refdes)
        self.combo_resistor_style.addItem("")
        self.combo_resistor_style.addItem("")
        self.combo_resistor_style.setObjectName(u"combo_resistor_style")
        self.combo_resistor_style.setMinimumSize(QSize(60, 0))
        self.combo_resistor_style.setMaximumSize(QSize(80, 16777215))
        self.combo_resistor_style.setFont(font)

        self.horizontalLayout.addWidget(self.combo_resistor_style)

        self.horizontalSpacer_2 = QSpacerItem(
            5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.line = QFrame(self.frame_refdes)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(
            5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_defaults = QPushButton(self.frame_refdes)
        self.btn_defaults.setObjectName(u"btn_defaults")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.btn_defaults.sizePolicy().hasHeightForWidth())
        self.btn_defaults.setSizePolicy(sizePolicy3)
        self.btn_defaults.setMinimumSize(QSize(20, 0))
        self.btn_defaults.setMaximumSize(QSize(25, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(127, 127, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(63, 63, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 0, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 127, 127))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
        brush10 = QBrush(QColor(76, 76, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush10)
        self.btn_defaults.setPalette(palette)
        self.btn_defaults.setFont(font)
        self.btn_defaults.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./images/rotate.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_defaults.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_defaults)

        self.hspacer_refdes_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hspacer_refdes_right)

        self.verticalLayout.addWidget(self.frame_refdes)

        self.frame_pn = QFrame()
        self.frame_pn.setObjectName(u"frame_pn")
        self.frame_pn.setMinimumSize(QSize(0, 35))
        self.frame_pn.setMaximumSize(QSize(16777215, 50))
        self.frame_pn.setFrameShape(QFrame.Box)
        self.frame_pn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_pn)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_mpn = QLabel(self.frame_pn)
        self.label_mpn.setObjectName(u"label_mpn")
        self.label_mpn.setMinimumSize(QSize(30, 0))
        self.label_mpn.setMaximumSize(QSize(50, 16777215))
        self.label_mpn.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_mpn)

        self.input_mpn = QLineEdit(self.frame_pn)
        self.input_mpn.setObjectName(u"input_mpn")
        sizePolicy3.setHeightForWidth(
            self.input_mpn.sizePolicy().hasHeightForWidth())
        self.input_mpn.setSizePolicy(sizePolicy3)
        self.input_mpn.setMinimumSize(QSize(120, 0))
        self.input_mpn.setMaximumSize(QSize(150, 16777215))
        self.input_mpn.setFont(font)

        self.horizontalLayout_2.addWidget(self.input_mpn)

        self.hspacer_pn_middle = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.hspacer_pn_middle)

        self.label_apn = QLabel(self.frame_pn)
        self.label_apn.setObjectName(u"label_apn")
        self.label_apn.setMinimumSize(QSize(30, 0))
        self.label_apn.setMaximumSize(QSize(50, 16777215))
        self.label_apn.setFont(font)
        self.label_apn.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_apn)

        self.input_apn = QLineEdit(self.frame_pn)
        self.input_apn.setObjectName(u"input_apn")
        sizePolicy3.setHeightForWidth(
            self.input_apn.sizePolicy().hasHeightForWidth())
        self.input_apn.setSizePolicy(sizePolicy3)
        self.input_apn.setMinimumSize(QSize(120, 0))
        self.input_apn.setMaximumSize(QSize(150, 16777215))
        self.input_apn.setFont(font)

        self.horizontalLayout_2.addWidget(self.input_apn)

        self.hspacer_pn_right = QSpacerItem(
            80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.hspacer_pn_right)

        self.verticalLayout.addWidget(self.frame_pn)

        self.val_gridframe = QFrame()
        self.val_gridframe.setObjectName(u"val_gridframe")
        self.val_gridframe.setMinimumSize(QSize(0, 100))
        self.val_gridframe.setMaximumSize(QSize(16777215, 150))
        self.val_gridframe.setFrameShape(QFrame.Box)
        self.val_gridframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.val_gridframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_degC_trated = QLabel(self.val_gridframe)
        self.label_degC_trated.setObjectName(u"label_degC_trated")
        self.label_degC_trated.setMinimumSize(QSize(30, 0))
        self.label_degC_trated.setMaximumSize(QSize(50, 16777215))
        self.label_degC_trated.setFont(font)
        self.label_degC_trated.setMargin(0)

        self.gridLayout_2.addWidget(self.label_degC_trated, 5, 2, 1, 1)

        self.label_V_Vmaxapplied = QLabel(self.val_gridframe)
        self.label_V_Vmaxapplied.setObjectName(u"label_V_Vmaxapplied")
        self.label_V_Vmaxapplied.setMinimumSize(QSize(30, 0))
        self.label_V_Vmaxapplied.setMaximumSize(QSize(50, 16777215))
        self.label_V_Vmaxapplied.setFont(font)
        self.label_V_Vmaxapplied.setMargin(0)

        self.gridLayout_2.addWidget(self.label_V_Vmaxapplied, 3, 2, 1, 1)

        self.input_tbaseplate = QLineEdit(self.val_gridframe)
        self.input_tbaseplate.setObjectName(u"input_tbaseplate")
        sizePolicy3.setHeightForWidth(
            self.input_tbaseplate.sizePolicy().hasHeightForWidth())
        self.input_tbaseplate.setSizePolicy(sizePolicy3)
        self.input_tbaseplate.setMinimumSize(QSize(50, 0))
        self.input_tbaseplate.setMaximumSize(QSize(100, 16777215))
        self.input_tbaseplate.setFont(font)
        self.input_tbaseplate.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_tbaseplate.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_tbaseplate, 4, 1, 1, 1)

        self.input_tzero = QLineEdit(self.val_gridframe)
        self.input_tzero.setObjectName(u"input_tzero")
        sizePolicy3.setHeightForWidth(
            self.input_tzero.sizePolicy().hasHeightForWidth())
        self.input_tzero.setSizePolicy(sizePolicy3)
        self.input_tzero.setMinimumSize(QSize(50, 0))
        self.input_tzero.setMaximumSize(QSize(100, 16777215))
        self.input_tzero.setFont(font)

        self.gridLayout_2.addWidget(self.input_tzero, 5, 5, 1, 1)

        self.label_Ohm_resistance = QLabel(self.val_gridframe)
        self.label_Ohm_resistance.setObjectName(u"label_Ohm_resistance")
        self.label_Ohm_resistance.setMinimumSize(QSize(30, 0))
        self.label_Ohm_resistance.setMaximumSize(QSize(50, 16777215))
        self.label_Ohm_resistance.setFont(font)
        self.label_Ohm_resistance.setMargin(0)

        self.gridLayout_2.addWidget(self.label_Ohm_resistance, 2, 2, 1, 1)

        self.label_Vmaxapplied = QLabel(self.val_gridframe)
        self.label_Vmaxapplied.setObjectName(u"label_Vmaxapplied")
        self.label_Vmaxapplied.setMinimumSize(QSize(80, 0))
        self.label_Vmaxapplied.setMaximumSize(QSize(100, 16777215))
        self.label_Vmaxapplied.setFont(font)
        self.label_Vmaxapplied.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_Vmaxapplied, 3, 0, 1, 1)

        self.label_powerrating = QLabel(self.val_gridframe)
        self.label_powerrating.setObjectName(u"label_powerrating")
        self.label_powerrating.setMinimumSize(QSize(80, 0))
        self.label_powerrating.setMaximumSize(QSize(100, 16777215))
        self.label_powerrating.setFont(font)
        self.label_powerrating.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_powerrating, 2, 4, 1, 1)

        self.input_vratedmax = QLineEdit(self.val_gridframe)
        self.input_vratedmax.setObjectName(u"input_vratedmax")
        sizePolicy3.setHeightForWidth(
            self.input_vratedmax.sizePolicy().hasHeightForWidth())
        self.input_vratedmax.setSizePolicy(sizePolicy3)
        self.input_vratedmax.setMinimumSize(QSize(50, 0))
        self.input_vratedmax.setMaximumSize(QSize(100, 16777215))
        self.input_vratedmax.setFont(font)

        self.gridLayout_2.addWidget(self.input_vratedmax, 3, 5, 1, 1)

        self.label_trated = QLabel(self.val_gridframe)
        self.label_trated.setObjectName(u"label_trated")
        self.label_trated.setMinimumSize(QSize(80, 0))
        self.label_trated.setMaximumSize(QSize(100, 16777215))
        self.label_trated.setFont(font)
        self.label_trated.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_trated, 5, 0, 1, 1)

        self.input_vmaxapplied = QLineEdit(self.val_gridframe)
        self.input_vmaxapplied.setObjectName(u"input_vmaxapplied")
        sizePolicy3.setHeightForWidth(
            self.input_vmaxapplied.sizePolicy().hasHeightForWidth())
        self.input_vmaxapplied.setSizePolicy(sizePolicy3)
        self.input_vmaxapplied.setMinimumSize(QSize(50, 0))
        self.input_vmaxapplied.setMaximumSize(QSize(100, 16777215))
        self.input_vmaxapplied.setFont(font)
        self.input_vmaxapplied.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_vmaxapplied.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_vmaxapplied, 3, 1, 1, 1)

        self.label_degC_tbaseplate = QLabel(self.val_gridframe)
        self.label_degC_tbaseplate.setObjectName(u"label_degC_tbaseplate")
        self.label_degC_tbaseplate.setMinimumSize(QSize(30, 0))
        self.label_degC_tbaseplate.setMaximumSize(QSize(50, 16777215))
        self.label_degC_tbaseplate.setFont(font)
        self.label_degC_tbaseplate.setMargin(0)

        self.gridLayout_2.addWidget(self.label_degC_tbaseplate, 4, 2, 1, 1)

        self.label_theta_R = QLabel(self.val_gridframe)
        self.label_theta_R.setObjectName(u"label_theta_R")
        self.label_theta_R.setMinimumSize(QSize(80, 0))
        self.label_theta_R.setMaximumSize(QSize(100, 16777215))
        self.label_theta_R.setFont(font)
        self.label_theta_R.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_theta_R, 4, 4, 1, 1)

        self.input_powerrating = QLineEdit(self.val_gridframe)
        self.input_powerrating.setObjectName(u"input_powerrating")
        sizePolicy3.setHeightForWidth(
            self.input_powerrating.sizePolicy().hasHeightForWidth())
        self.input_powerrating.setSizePolicy(sizePolicy3)
        self.input_powerrating.setMinimumSize(QSize(50, 0))
        self.input_powerrating.setMaximumSize(QSize(100, 16777215))
        self.input_powerrating.setFont(font)

        self.gridLayout_2.addWidget(self.input_powerrating, 2, 5, 1, 1)

        self.input_thetaR = QLineEdit(self.val_gridframe)
        self.input_thetaR.setObjectName(u"input_thetaR")
        sizePolicy3.setHeightForWidth(
            self.input_thetaR.sizePolicy().hasHeightForWidth())
        self.input_thetaR.setSizePolicy(sizePolicy3)
        self.input_thetaR.setMinimumSize(QSize(50, 0))
        self.input_thetaR.setMaximumSize(QSize(100, 16777215))
        self.input_thetaR.setFont(font)

        self.gridLayout_2.addWidget(self.input_thetaR, 4, 5, 1, 1)

        self.label_vratedmax = QLabel(self.val_gridframe)
        self.label_vratedmax.setObjectName(u"label_vratedmax")
        self.label_vratedmax.setMinimumSize(QSize(80, 0))
        self.label_vratedmax.setMaximumSize(QSize(100, 16777215))
        self.label_vratedmax.setFont(font)
        self.label_vratedmax.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_vratedmax, 3, 4, 1, 1)

        self.label_degC_tzero = QLabel(self.val_gridframe)
        self.label_degC_tzero.setObjectName(u"label_degC_tzero")
        self.label_degC_tzero.setMinimumSize(QSize(30, 0))
        self.label_degC_tzero.setMaximumSize(QSize(50, 16777215))
        self.label_degC_tzero.setFont(font)

        self.gridLayout_2.addWidget(self.label_degC_tzero, 5, 6, 1, 1)

        self.hspacer_row4_middle = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row4_middle, 5, 3, 1, 1)

        self.input_resistance = QLineEdit(self.val_gridframe)
        self.input_resistance.setObjectName(u"input_resistance")
        self.input_resistance.setEnabled(True)
        sizePolicy3.setHeightForWidth(
            self.input_resistance.sizePolicy().hasHeightForWidth())
        self.input_resistance.setSizePolicy(sizePolicy3)
        self.input_resistance.setMinimumSize(QSize(50, 0))
        self.input_resistance.setMaximumSize(QSize(100, 16777215))
        self.input_resistance.setFont(font)
        self.input_resistance.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_resistance.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_resistance, 2, 1, 1, 1)

        self.hspacer_row3_middle = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row3_middle, 4, 3, 1, 1)

        self.label_tzero = QLabel(self.val_gridframe)
        self.label_tzero.setObjectName(u"label_tzero")
        self.label_tzero.setMinimumSize(QSize(80, 0))
        self.label_tzero.setMaximumSize(QSize(100, 16777215))
        self.label_tzero.setFont(font)
        self.label_tzero.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_tzero, 5, 4, 1, 1)

        self.input_trated = QLineEdit(self.val_gridframe)
        self.input_trated.setObjectName(u"input_trated")
        sizePolicy3.setHeightForWidth(
            self.input_trated.sizePolicy().hasHeightForWidth())
        self.input_trated.setSizePolicy(sizePolicy3)
        self.input_trated.setMinimumSize(QSize(50, 0))
        self.input_trated.setMaximumSize(QSize(100, 16777215))
        self.input_trated.setFont(font)
        self.input_trated.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_trated.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.input_trated, 5, 1, 1, 1)

        self.label_degCW_thetaR = QLabel(self.val_gridframe)
        self.label_degCW_thetaR.setObjectName(u"label_degCW_thetaR")
        self.label_degCW_thetaR.setMinimumSize(QSize(30, 0))
        self.label_degCW_thetaR.setMaximumSize(QSize(50, 16777215))
        self.label_degCW_thetaR.setFont(font)

        self.gridLayout_2.addWidget(self.label_degCW_thetaR, 4, 6, 1, 1)

        self.label_V_vratedmax = QLabel(self.val_gridframe)
        self.label_V_vratedmax.setObjectName(u"label_V_vratedmax")
        self.label_V_vratedmax.setMinimumSize(QSize(30, 0))
        self.label_V_vratedmax.setMaximumSize(QSize(50, 16777215))
        self.label_V_vratedmax.setFont(font)

        self.gridLayout_2.addWidget(self.label_V_vratedmax, 3, 6, 1, 1)

        self.hspacer_row2_middle = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row2_middle, 3, 3, 1, 1)

        self.label_W_powerrating = QLabel(self.val_gridframe)
        self.label_W_powerrating.setObjectName(u"label_W_powerrating")
        self.label_W_powerrating.setMinimumSize(QSize(30, 0))
        self.label_W_powerrating.setMaximumSize(QSize(50, 16777215))
        self.label_W_powerrating.setFont(font)

        self.gridLayout_2.addWidget(self.label_W_powerrating, 2, 6, 1, 1)

        self.label_resistance = QLabel(self.val_gridframe)
        self.label_resistance.setObjectName(u"label_resistance")
        self.label_resistance.setMinimumSize(QSize(80, 0))
        self.label_resistance.setMaximumSize(QSize(100, 16777215))
        self.label_resistance.setFont(font)
        self.label_resistance.setFrameShadow(QFrame.Raised)
        self.label_resistance.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_resistance, 2, 0, 1, 1)

        self.label_T_baseplate = QLabel(self.val_gridframe)
        self.label_T_baseplate.setObjectName(u"label_T_baseplate")
        self.label_T_baseplate.setMinimumSize(QSize(80, 0))
        self.label_T_baseplate.setMaximumSize(QSize(100, 16777215))
        self.label_T_baseplate.setFont(font)
        self.label_T_baseplate.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_T_baseplate, 4, 0, 1, 1)

        self.hspacer_row1_middle = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row1_middle, 2, 3, 1, 1)

        self.hspacer_row1_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row1_right, 2, 7, 1, 1)

        self.hspacer_row2_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row2_right, 3, 7, 1, 1)

        self.hspacer_row3_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row3_right, 4, 7, 1, 1)

        self.hspacer_row4_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.hspacer_row4_right, 5, 7, 1, 1)

        self.verticalLayout.addWidget(self.val_gridframe)

        self.frame_notes = QFrame()
        self.frame_notes.setObjectName(u"frame_notes")
        self.frame_notes.setFrameShape(QFrame.Box)
        self.frame_notes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_notes)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_usernotes = QLabel(self.frame_notes)
        self.label_usernotes.setObjectName(u"label_usernotes")
        self.label_usernotes.setMinimumSize(QSize(100, 100))
        self.label_usernotes.setMaximumSize(QSize(200, 16777215))
        self.label_usernotes.setFont(font)
        self.label_usernotes.setTextFormat(Qt.RichText)

        self.horizontalLayout_3.addWidget(self.label_usernotes)

        self.textedit_usernotes = QPlainTextEdit(self.frame_notes)
        self.textedit_usernotes.setObjectName(u"textedit_usernotes")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.textedit_usernotes.sizePolicy().hasHeightForWidth())
        self.textedit_usernotes.setSizePolicy(sizePolicy4)
        self.textedit_usernotes.setMinimumSize(QSize(100, 100))
        self.textedit_usernotes.setFont(font)

        self.horizontalLayout_3.addWidget(self.textedit_usernotes)

        self.verticalLayout.addWidget(self.frame_notes)

        QWidget.setTabOrder(self.input_powerrating, self.input_vmaxapplied)
        QWidget.setTabOrder(self.input_vmaxapplied, self.input_vratedmax)
        QWidget.setTabOrder(self.input_vratedmax, self.input_tbaseplate)
        QWidget.setTabOrder(self.input_tbaseplate, self.input_thetaR)
        QWidget.setTabOrder(self.input_thetaR, self.input_trated)
        QWidget.setTabOrder(self.input_trated, self.input_tzero)

        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(
            QCoreApplication.translate("ResistorWidget", u"Form", None))
        self.label_refdes.setText(QCoreApplication.translate(
            "ResistorWidget", u"Ref Des:", None))
        self.input_refdes.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor reference designator. Double-click to edit.", None))
        self.input_refdes.setPlaceholderText(
            QCoreApplication.translate("ResistorWidget", u"R??", None))
        self.label_resistor_style.setText(QCoreApplication.translate(
            "ResistorWidget", u"Resistor Style:", None))
        self.btn_info_resistor_style.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor style information", None))
        self.btn_info_resistor_style.setText("")
        self.combo_resistor_style.setItemText(
            0, QCoreApplication.translate("ResistorWidget", u"Item1", None))
        self.combo_resistor_style.setItemText(
            1, QCoreApplication.translate("ResistorWidget", u"Item2", None))

        self.combo_resistor_style.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor style dropdown", None))
        self.btn_defaults.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Apply default values to the fields. See documentation for more information.", None))
        self.btn_defaults.setText("")
        self.label_mpn.setText(QCoreApplication.translate(
            "ResistorWidget", u"MPN:", None))
        self.input_mpn.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Manufacturer part number", None))
        self.label_apn.setText(QCoreApplication.translate(
            "ResistorWidget", u"APN:", None))
        self.input_apn.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Alternate part number", None))
        self.label_degC_trated.setText(
            QCoreApplication.translate("ResistorWidget", u"degC", None))
        self.label_V_Vmaxapplied.setText(
            QCoreApplication.translate("ResistorWidget", u"V", None))
        self.input_tbaseplate.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Baseplate temperature, in degC, with SI prefixes (i.e., 68)", None))
        self.input_tzero.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor's zero-power temperature, in degC, with SI prefixes (i.e., 68)", None))
        self.label_Ohm_resistance.setText(
            QCoreApplication.translate("ResistorWidget", u"Ohm", None))
        self.label_Vmaxapplied.setText(QCoreApplication.translate(
            "ResistorWidget", u"DVmax_Applied", None))
        self.label_powerrating.setText(QCoreApplication.translate(
            "ResistorWidget", u"Power Rating:", None))
        self.input_vratedmax.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor's maximum rated voltage, in volts, with SI prefixes (i.e., 200)", None))
        self.label_trated.setText(QCoreApplication.translate(
            "ResistorWidget", u"T_rated", None))
        self.input_vmaxapplied.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Maximum DV applied to the resistor, in volts, with SI prefixes (i.e., 25m)", None))
        self.label_degC_tbaseplate.setText(
            QCoreApplication.translate("ResistorWidget", u"degC", None))
        self.label_theta_R.setText(QCoreApplication.translate(
            "ResistorWidget", u"Theta_R", None))
        self.input_powerrating.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Power rating, in watts, with SI prefixes (i.e., 63m)", None))
        self.input_thetaR.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor's thermal resistance, in degC/W, with SI prefixes (i.e., 2.3)", None))
        self.label_vratedmax.setText(QCoreApplication.translate(
            "ResistorWidget", u"Vrated_max", None))
        self.label_degC_tzero.setText(
            QCoreApplication.translate("ResistorWidget", u"degC", None))
        self.input_resistance.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistance, in ohms, with SI prefixes (i.e., 10k)", None))
        self.label_tzero.setText(QCoreApplication.translate(
            "ResistorWidget", u"T_zero", None))
        self.input_trated.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"Resistor's rated temperature, in degC, with SI prefixes (i.e., 150)", None))
        self.label_degCW_thetaR.setText(
            QCoreApplication.translate("ResistorWidget", u"degC/W", None))
        self.label_V_vratedmax.setText(
            QCoreApplication.translate("ResistorWidget", u"V", None))
        self.label_W_powerrating.setText(
            QCoreApplication.translate("ResistorWidget", u"W", None))
        self.label_resistance.setText(QCoreApplication.translate(
            "ResistorWidget", u"Resistance:", None))
        self.label_T_baseplate.setText(QCoreApplication.translate(
            "ResistorWidget", u"T_baseplate", None))
        self.label_usernotes.setText(QCoreApplication.translate(
            "ResistorWidget", u"<html><head/><body><p>User Notes</p><p>(One Note Per Line)</p></body></html>", None))
        self.textedit_usernotes.setToolTip(QCoreApplication.translate(
            "ResistorWidget", u"User notes, can be anything. Separate each note by a linebreak.", None))
