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

        self._check_if_saved = True

        # Call local setup, where the basic stuff created in
        # Qt Designer/Creator UI is overwritten
        self._setup_ui()

        # self._save_defaults()

        self._load_prefs_into_window()

        self._setup_slots()

    def _setup_ui(self):
        epsa_logger.info("Setting up preferences window UI...")

        # Units ComboBoxes
        self.ui.combo_unitsystem.clear()
        self.ui.combo_unitsystem.addItems(PREFOPTIONS_UNITSYSTEM)

        self.ui.combo_lengthtype.clear()
        self.ui.combo_lengthtype.addItems(PREFOPTIONS_UNITLENGTH)

        self.ui.combo_masstype.clear()
        self.ui.combo_masstype.addItems(PREFOPTIONS_UNITMASS)

        self.ui.combo_temptype.clear()
        self.ui.combo_temptype.addItems(PREFOPTIONS_UNITTEMP)

    def _save_defaults(self):
        # Needed to reset registry keys in case they get borked up
        epsa_logger.info("Saving default preferences...")

        # Application
        epsa_settings.setValue(SETTING_UNITSYSTEM, 0)
        epsa_settings.setValue(SETTING_UNITLENGTH, 0)
        epsa_settings.setValue(SETTING_UNITTEMP, 0)
        epsa_settings.setValue(SETTING_UNITMASS, 0)
        epsa_settings.setValue(SETTING_DEBUG, 0)

        # User
        epsa_settings.setValue(SETTING_USERNAME, "FirstName LastName")
        epsa_settings.setValue(SETTING_USERORG, "Your Company/Org Here")
        epsa_settings.setValue(SETTING_USERTITLE, "Your Title Here")

    def _load_prefs_into_window(self):
        epsa_logger.info("Loading preferences into window...")

        # Application
        self.ui.combo_unitsystem.setCurrentIndex(epsa_settings.value(SETTING_UNITSYSTEM))
        self.ui.combo_lengthtype.setCurrentIndex(epsa_settings.value(SETTING_UNITLENGTH))
        self.ui.combo_masstype.setCurrentIndex(epsa_settings.value(SETTING_UNITMASS))
        self.ui.combo_temptype.setCurrentIndex(epsa_settings.value(SETTING_UNITTEMP))
        self.ui.checkbox_debug.setChecked(bool(epsa_settings.value(SETTING_DEBUG)))

        # User
        self.ui.input_username.setText(epsa_settings.value(SETTING_USERNAME))
        self.ui.input_userorg.setText(epsa_settings.value(SETTING_USERORG))
        self.ui.input_usertitle.setText(epsa_settings.value(SETTING_USERTITLE))

    def _setup_slots(self):
        epsa_logger.info("Setting up slots...")

        # Main button clicks
        self.ui.btn_apply.clicked.connect(self.slot_apply)
        self.ui.btn_cancel.clicked.connect(self.slot_cancel)
        self.ui.btn_ok.clicked.connect(self.slot_ok)

    def slot_apply(self):
        epsa_logger.info("Applying preferences...")

        # Application
        epsa_settings.setValue(SETTING_UNITSYSTEM, int(str(self.ui.combo_unitsystem.currentIndex())))
        epsa_settings.setValue(SETTING_UNITLENGTH, int(str(self.ui.combo_lengthtype.currentIndex())))
        epsa_settings.setValue(SETTING_UNITTEMP, int(str(self.ui.combo_temptype.currentIndex())))
        epsa_settings.setValue(SETTING_UNITMASS, int(str(self.ui.combo_masstype.currentIndex())))
        epsa_settings.setValue(SETTING_DEBUG, int(self.ui.checkbox_debug.isChecked()))

        # User
        epsa_settings.setValue(SETTING_USERNAME, self.ui.input_username.text())
        epsa_settings.setValue(SETTING_USERORG, self.ui.input_userorg.text())
        epsa_settings.setValue(SETTING_USERTITLE, self.ui.input_usertitle.text())

    def slot_cancel(self):
        epsa_logger.info("Canceling preferences...")
        self._check_if_saved = False
        self.close()

    def slot_ok(self):
        epsa_logger.info("OKing preferences...")
        self.slot_apply()

        # "Quick" exit (no saved check)
        self._check_if_saved = False
        self.close()

    def _check_saved(self):
        epsa_logger.info("Checking that preferences are saved...")

        # Get all current values
        # Application
        unitsystem_idx = int(str(self.ui.combo_unitsystem.currentIndex()))
        lengthtype_idx = int(str(self.ui.combo_lengthtype.currentIndex()))
        temptype_idx = int(str(self.ui.combo_temptype.currentIndex()))
        masstype_idx = int(str(self.ui.combo_masstype.currentIndex()))
        debug_checked = int(self.ui.checkbox_debug.isChecked())

        # User
        username = self.ui.input_username.text()
        userorg = self.ui.input_userorg.text()
        usertitle = self.ui.input_usertitle.text()

        # Compare to stored values
        saved_list = [
            unitsystem_idx == epsa_settings.value(SETTING_UNITSYSTEM),
            lengthtype_idx == epsa_settings.value(SETTING_UNITLENGTH),
            temptype_idx == epsa_settings.value(SETTING_UNITTEMP),
            masstype_idx == epsa_settings.value(SETTING_UNITMASS),
            debug_checked == epsa_settings.value(SETTING_DEBUG),
            username == epsa_settings.value(SETTING_USERNAME),
            userorg == epsa_settings.value(SETTING_USERORG),
            usertitle == epsa_settings.value(SETTING_USERTITLE),
        ]

        if False in saved_list:
            return False
        else:
            return True

    def _ask_saved(self):
        epsa_logger.info("Checking that preferences are saved...")
        exit_save_mbox = QMessageBox()
        exit_save_mbox.setWindowTitle("EPSA Wizard: Preferences Unsaved")
        exit_save_mbox.setText(f"Your preferences haven't been saved!")
        exit_save_mbox.setInformativeText(f"Do you want to save your current preferences?")
        exit_save_mbox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        exit_save_mbox.setIcon(QMessageBox.Warning)
        exit_save_mbox.setDefaultButton(QMessageBox.Save)
        box_font = QFont()
        box_font.setFamilies([u"Liberation Sans"])
        exit_save_mbox.setFont(box_font)

        # Get user input
        exit_save_return = exit_save_mbox.exec()

        if exit_save_return == QMessageBox.Save:
            self.slot_apply()
            self.close()
            return True
        elif exit_save_return == QMessageBox.Discard:
            self.close()
            return True
        elif exit_save_return == QMessageBox.Cancel:
            self._check_if_saved = True
            return False

    def closeEvent(self, event):
        epsa_logger.info("Closing preferences...")
        self._exit_window(event)

    def _exit_window(self, event=None):
        epsa_logger.info("Exiting window...")

        is_saved = self._check_saved()

        if is_saved:
            self.close()
        else:
            if self._check_if_saved:
                close_window = self._ask_saved()
                if event is not None:
                    if not close_window:
                        event.ignore()
                    else:
                        event.accept()
            else:
                event.accept()
