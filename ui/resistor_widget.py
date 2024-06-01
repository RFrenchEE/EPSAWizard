from PySide6.QtWidgets import (
    QWidget
)
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

    def _relabel(self):
        epsa_logger.info("Relabeling ResistorWidget labels...")
        self.ui.unitlbl_R.setText("Ω")
        self.ui.unitlbl_T0.setText("°C")
        self.ui.unitlbl_Tbase.setText("°C")
        self.ui.unitlbl_ThetaR.setText("°C/W")
        self.ui.unitlbl_Trated.setText("°C")

        # Update labels that require unicode/HTML
        self.ui.lbl_Vmaxapplied.setText("Max ΔV Applied:")
        self.ui.lbl_ThetaR.setText("θ<sub>R</sub>:")