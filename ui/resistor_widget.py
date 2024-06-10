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
from ui.infoselection_dialog import InfoSelectionDialog
from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *

from src.components.resistors import (
    resistor_style_dict, EPSA_Resistor
)

class ResistorWidget(QWidget):
    def __init__(self, frame):
        epsa_logger.info("Instantiating ResistorWidget")
        super().__init__()
        self.ui = Ui_ResistorWidget()
        self.ui.setupUi(frame)
        self._relabel()
        self._setup_combo()
        self._set_icons()
        self._setup_slots()
        self._create_resistortype_info()

    def _relabel(self):
        epsa_logger.info("Relabeling ResistorWidget labels")
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

    def _setup_combo(self):
        epsa_logger.info("Adding resistor styles to RedsistorWidget's QComboBox")

        # Get the resistor styles from the dictionary in which we define them
        combo_items = list(resistor_style_dict.keys())
        self.ui.combo_type.clear()
        self.ui.combo_type.addItems(combo_items)

    def _set_icons(self, theme="dark"):
        epsa_logger.info("Adding icons")

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

    def _setup_slots(self):
        epsa_logger.info("Setting up ResistorWidget slots")

        # When any lineedit is done being edited, run the slot_vals_updated function
        for lineedit in [
            self.ui.input_mpn,
            self.ui.input_apn,
            self.ui.input_R,
            self.ui.input_Prated,
            self.ui.input_Vmaxapplied,
            self.ui.input_Vrated,
            self.ui.input_Tbase,
            self.ui.input_ThetaR,
            self.ui.input_Trated,
            self.ui.input_T0
        ]:
            lineedit.editingFinished.connect(self.slot_vals_updated)

        # When Type combobox is changed, run the slot_vals_updated function
        self.ui.combo_type.currentIndexChanged.connect(self.slot_vals_updated)

        # When type button is pressed, launch an InfoSelectionDialog
        self.ui.btn_type.pressed.connect(self.slot_resistor_type_dialog)

    def _create_resistortype_info(self):
        epsa_logger.info("Creating the resistor type info dictionary")
        self.resistor_desc_dict = {}
        for restype, resinfo in resistor_style_dict.items():
            self.resistor_desc_dict[restype] = resinfo.longdesc

    def slot_resistor_type_dialog(self):
        epsa_logger.info("Opening resistor type InfoSelectionDialog")
        # InfoSelectionDialog popup for Resistor Type
        resistor_type_dialog = InfoSelectionDialog(
            "Resistor Style Selection",
            "Resistor Style:",
            "Style Information:",
            self.resistor_desc_dict
        )
        resistor_type_dialog.exec()

        # Result:
        # Can be QDialog.Accepted (user selected resistor type)
        # or QDialog.Rejected (user exited without selecting resistor type)
        result = resistor_type_dialog.result()

    def slot_vals_updated(self):
        epsa_logger.info("ResistorWidget values have been updated. Handling")

    def loadvals(self, refdes: str, defaults: bool=True):
        epsa_logger.info(f"Loading {refdes}'s values into ResistorWidget")
