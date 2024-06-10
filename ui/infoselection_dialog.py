from textwrap import dedent
from PySide6.QtWidgets import (
    QDialog
)

from PySide6.QtGui import (
    QIcon
)

from PySide6.QtCore import (
    QSize
)

# The imports below are necessary to properly import SVGs on Windows 10, 64-bit.
# No idea why. See https://github.com/derrian-distro/LoRA_Easy_Training_Scripts/issues/94
from PySide6 import QtSvg, QtXml

from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *
from ui.qss_translate import load_epsa_qss
from ui.ui_infoselectiondialog import Ui_InfoSelectionDialog

epsa_logger.debug("Imported infoselection_dialog.py")

class InfoSelectionDialog(QDialog):
    def __init__(self,
        title="EPSA Info Selection Dialog",
        listlabel="Items:",
        desclabel="Description Area:",
        item_desc_dict={}
    ):
        epsa_logger.info("Instantiating InfoSelectionDialog")
        # Create local variables for window title, labels, and item/description dictionary
        self.windowtitle = title
        self.listlabel = listlabel
        self.desclabel = desclabel
        self.item_desc_dict = item_desc_dict

        super().__init__()

        self.ui = Ui_InfoSelectionDialog()
        self.ui.setupUi(self)

        self._relabel()
        self._set_icons()
        self._additem_desc()
        self._setup_slots()


    def _relabel(self):
        epsa_logger.info("Relabeling InfoSelectionDialog")
        self.setWindowTitle(self.windowtitle)
        self.ui.lbl_list.setText(self.listlabel)
        self.ui.lbl_desc.setText(self.desclabel)

    def _additem_desc(self):
        epsa_logger.info(f"Adding items to {self.windowtitle} dialog window")
        self.ui.listwidget_infoselection.clear()
        self.ui.listwidget_infoselection.addItems(list(self.item_desc_dict.keys()))

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

        # Main Window Icon
        icon_info = QIcon()
        icon_info.addFile(svg_icon("info_circ"), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon_info)

        # Apply Icon
        icon_apply = QIcon()
        icon_apply.addFile(svg_icon("check"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_apply.setIcon(icon_apply)

        # Cancel Icon
        icon_cancel = QIcon()
        icon_cancel.addFile(svg_icon("x"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_cancel.setIcon(icon_cancel)

    def _setup_slots(self):
        epsa_logger.info("Setting up InfoSelectionDialog slots")

        self.ui.listwidget_infoselection.currentTextChanged.connect(self.slot_update_desc)

    def slot_update_desc(self, rowtext):
        epsa_logger.info("Changing description in InfoSelectionDialog")

        # Use rowtext to access the description dictionary then display it
        self.ui.textbrowser_desc.setHtml(self.item_desc_dict[rowtext])