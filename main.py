import sys
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.qss_translate import load_epsa_qss

from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *

if __name__ == "__main__":
    # Set version number
    epsa_settings.setValue(SETTING_VERSION_NUMBER, EPSA_WIZARD_VERSION)

    epsa_wizard_style = load_epsa_qss()
    app = QApplication(sys.argv)
    window = MainWindow()
    icon_qss = window.icon_qss()

    # Set application StyleSheet by adding the qss file and icon_qss strings
    app.setStyleSheet(epsa_wizard_style + '\n' + icon_qss)

    window.show()

    sys.exit(app.exec())
