from PySide6.QtWidgets import (
    QWidget
)
from PySide6.QtGui import (
    QIcon, QFont
)
from PySide6.QtCore import (
    QSize, QSettings
)

# The imports below are necessary to properly import SVGs on Windows 10, 64-bit.
# No idea why. See https://github.com/derrian-distro/LoRA_Easy_Training_Scripts/issues/94
from PySide6 import QtSvg, QtXml

from ui.ui_resistorwidget import Ui_ResistorWidget
from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *

class ResistorWidget(QWidget):
    def __init__(self, frame):
        epsa_logger.info("Instantiating ResistorWidget...")
        super().__init__()
        self.ui = Ui_ResistorWidget()
        self.ui.setupUi(frame)
        self._relabel()
        self._set_icons()

    def _relabel(self):
        epsa_logger.info("Relabeling ResistorWidget labels...")
        self.ui.unitlbl_R.setText("Ω")
        self.ui.unitlbl_T0.setText("°C")
        self.ui.unitlbl_Tbase.setText("°C")
        self.ui.unitlbl_ThetaR.setText("°C/W")
        self.ui.unitlbl_Trated.setText("°C")

        # Update labels that require unicode/HTML
        self.ui.lbl_Vmaxapplied.setText("ΔV<sub>max</sub>: ")
        self.ui.lbl_Vrated.setText("V<sub>rated</sub>: ")
        self.ui.lbl_Prated.setText("P<sub>rated</sub>: ")
        self.ui.lbl_T0.setText("T<sub>0</sub>: ")
        self.ui.lbl_Tbase.setText("T<sub>base</sub>: ")
        self.ui.lbl_Trated.setText("T<sub>rated</sub>: ")
        self.ui.lbl_ThetaR.setText("θ<sub>R</sub>: ")
    
    def _set_icons(self, theme="dark"):
        epsa_logger.info("Adding icons...")

        def svg_icon(name: str) -> str:
            # Returns path to icon with given name
            # Takes into account the type of theme
            if theme == "dark":
                postfix = "light"
            else:
                postfix = "dark"
            return f"./images/{name}-{postfix}.svg"

        # Resistor Type Question
        icon_info = QIcon()
        icon_info.addFile(svg_icon("info_circ"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_type.setIcon(icon_info)