from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QTreeWidgetItem
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

from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *
from ui.ui_preferenceswindow import Ui_MainWindow as Ui_PreferencesWindow

epsa_logger.debug("Imported preferences_window.py")

class PreferencesWindow(QMainWindow):
    def __init__(self):
        epsa_logger.info("Instantiating PreferencesWindow")
        super().__init__()

        self.ui = Ui_PreferencesWindow()
        self.ui.setupUi(self)