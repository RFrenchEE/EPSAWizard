from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QTreeWidgetItem, QFileDialog
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

import re

from utilities.epsa_logging import epsa_logger
from utilities.epsa_settings import *
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_resistorwidget import Ui_ResistorWidget
from ui.resistor_widget import ResistorWidget
from ui.preferences_window import PreferencesWindow

epsa_logger.debug("Imported main_window.py")

class MainWindow(QMainWindow):
    def __init__(self):
        epsa_logger.info("Instantiating MainUI")

        super().__init__()

        # Current file path + name
        self.current_filepath = r""
        self.current_filename = r"newfile.epsa"

        # Variable to note if the window is currently being closed.
        # This is neccessary because our _slot_exit()
        self._is_closing = False

        # Is the file saved?
        self._is_saved = True

        # Preferences Window?
        self.pref_window = None
        self.pref_window_is_open = False

        # Import UI info from PySide6-uic output
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Current component being edited.
        # TODO: May have to change when we boot on a non-alpha new session
        self._current_component = self.ui.comptree.topLevelItem(0).child(0)
        self.ui.comptree.setCurrentItem(
            self._current_component,
            0
        )
        self._update_compinfo_label()

        # TODO: Change this to dynamic maybe? Can't be static
        self.main_widget = ResistorWidget(self.ui.main_frame)

        # Load settings
        self._load_settings()

       # Set window title 
        self.base_title = f"EPSA Wizard v{epsa_settings.value(SETTING_VERSION_NUMBER)}"
        self.window_title = f"{self.base_title} - {self.current_filename}"
        self.setWindowTitle(self.window_title)

        # Set icons
        # TODO: Add dark/light theming integration
        self._set_icons()

        # Set up window title and size
        self._setup_window()

        # Set up slots
        self._setup_slots()

    def _setup_window(self):
        epsa_logger.info("Setting up window...")
        # Set window width and height
        window_width = epsa_settings.value(SETTING_MAIN_WINDOW_W)
        window_height = epsa_settings.value(SETTING_MAIN_WINDOW_H)
        self.resize(window_width, window_height)

        # Set up main window icon
        icon_wizard = QIcon()
        icon_wizard.addFile(u"./images/epsa_wizard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon_wizard)
        # self.setTabShape(QTabWidget.Rounded)

    def _setup_slots(self):
        epsa_logger.info("Setting up slots...")
        # Actions
        # File Menu
        self.ui.action_new.triggered.connect(self.slot_newfile)
        self.ui.action_open.triggered.connect(self.slot_openfile)
        self.ui.action_save.triggered.connect(self.slot_savefile)
        self.ui.action_saveas.triggered.connect(self.slot_savefileas)
        self.ui.action_import.triggered.connect(self.slot_import)
        self.ui.action_exporttxt.triggered.connect(self.slot_exporttxt)
        self.ui.action_exportcsv.triggered.connect(self.slot_exportcsv)
        self.ui.action_preferences.triggered.connect(self.slot_preferences)
        self.ui.action_exit.triggered.connect(self.slot_exit)

        # Calculate Menu
        self.ui.action_run_epsa_calc.triggered.connect(self.slot_run_epsa_calc)

        # Help Menu
        self.ui.action_about.triggered.connect(self.slot_about_epsa_wizard)
        self.ui.action_documentation.triggered.connect(self.slot_documentation)

        # Buttons
        self.ui.btn_prevcomp.clicked.connect(self.slot_prevcomp)
        self.ui.btn_nextcomp.clicked.connect(self.slot_nextcomp)
        self.ui.btn_delcomp.clicked.connect(self.slot_delcomp)
        self.ui.btn_newcomp.clicked.connect(self.slot_newcomp)
        self.ui.btn_savecomp.clicked.connect(self.slot_savecomp)
        self.ui.btn_compdefault.clicked.connect(self.slot_compdefault)

        # Component Tree
        self.ui.comptree.itemDoubleClicked.connect(self.slot_treeitem_chosen)

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

        # New file
        icon_newfile = QIcon()
        icon_newfile.addFile(svg_icon("file_new"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_new.setIcon(icon_newfile)

        # Open file
        icon_open = QIcon()
        icon_open.addFile(svg_icon("folder_open"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_open.setIcon(icon_open)

        # Save file
        icon_save = QIcon()
        icon_save.addFile(svg_icon("file"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_save.setIcon(icon_save)

        # Save file As...
        icon_saveas = QIcon()
        icon_saveas.addFile(svg_icon("file_pen"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_saveas.setIcon(icon_saveas)

        # Import
        icon_import = QIcon()
        icon_import.addFile(svg_icon("file_import"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_import.setIcon(icon_import)

        # Export CSV
        icon_exportcsv = QIcon()
        icon_exportcsv.addFile(svg_icon("file_csv"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_exportcsv.setIcon(icon_exportcsv)

        # Export Text
        icon_exporttxt = QIcon()
        icon_exporttxt.addFile(svg_icon("file_lines"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_exporttxt.setIcon(icon_exporttxt)

        # Exit
        icon_exit = QIcon()
        icon_exit.addFile(svg_icon("x_circ"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_exit.setIcon(icon_exit)

        # Preferences
        icon_preferences = QIcon()
        icon_preferences.addFile(svg_icon("hsliders"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_preferences.setIcon(icon_preferences)

        # Calculate EPSA
        icon_calculate = QIcon()
        icon_calculate.addFile(svg_icon("cog"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_run_epsa_calc.setIcon(icon_calculate)

        # About
        icon_about = QIcon()
        icon_about.addFile(svg_icon("info_circ"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_about.setIcon(icon_about)

        # Documentation
        icon_documentation = QIcon()
        icon_documentation.addFile(svg_icon("book"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.action_documentation.setIcon(icon_documentation)

        # Previous Component Button (Caret Left)
        icon_previous = QIcon()
        icon_previous.addFile(svg_icon("caret_left"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_prevcomp.setIcon(icon_previous)

        # Next Component Button (Caret Right)
        icon_next = QIcon()
        icon_next.addFile(svg_icon("caret_right"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_nextcomp.setIcon(icon_next)

        # Component Defaults Button (Rotate)
        icon_compdefault = QIcon()
        icon_compdefault.addFile(svg_icon("rotate"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_compdefault.setIcon(icon_compdefault)

        # Delete Component Button (Trash Can)
        icon_delete = QIcon()
        icon_delete.addFile(svg_icon("trash"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_delcomp.setIcon(icon_delete)

        # New Component Button (Plus Sign)
        icon_new = QIcon()
        icon_new.addFile(svg_icon("plus"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_newcomp.setIcon(icon_new)

        # Save Components Button (Check Mark)
        icon_save = QIcon()
        icon_save.addFile(svg_icon("check"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_savecomp.setIcon(icon_save)

    def icon_qss(self, theme="dark"):
        epsa_logger.info("Generating Qt StyleSheet icon QSS...")

        def svg_icon(name: str) -> str:
            # Returns path to icon with given name
            # Takes into account the type of theme
            if theme == "dark":
                postfix = "light"
            else:
                postfix = "dark"
            return f"./images/{name}-{postfix}.svg"

        icon_chevdown = svg_icon("chevron_down")
        icon_chevup = svg_icon("chevron_up")
        icon_check = svg_icon("check")


        qss = f"""
            QTreeWidget QHeaderView::down-arrow {{
	            image: url({icon_chevdown})
            }}
            QTreeWidget QHeaderView::up-arrow {{
	            image: url({icon_chevup})
            }}
            QComboBox::down-arrow {{
                right: 4px;
                image: url({icon_chevdown});
            }}
            QCheckBox::indicator:checked {{
                image: url({icon_check})
            }}
            """

        return qss

    def _save_settings(self):
        # Save all settings. Refer to the list of possible settings in utilities/_settings_consts.py
        epsa_logger.info("Saving settings...")

        # Get window geometry
        window_geometry = self.frameGeometry()
        window_width = window_geometry.width()
        window_height = window_geometry.height()
        epsa_settings.setValue(SETTING_MAIN_WINDOW_H, window_height)
        epsa_settings.setValue(SETTING_MAIN_WINDOW_W, window_width)

    def _load_settings(self):
        epsa_logger.info("Loading settings...")

        # Below, define the settings we want to import
        self._window_height_val = epsa_settings.value(SETTING_MAIN_WINDOW_H)
        self._window_width_val = epsa_settings.value(SETTING_MAIN_WINDOW_W)
        if self._window_height_val is None or self._window_width_val is None:
            epsa_settings.setValue(SETTING_MAIN_WINDOW_H, WINDOW_INIT_H)
            epsa_settings.setValue(SETTING_MAIN_WINDOW_W, WINDOW_INIT_W)

    def slot_newfile(self):
        check_passed = self._check_saved()
        if not check_passed:
            return
        self.window_title = f"{self.base_title} - newfile.epsa"
        self.setWindowTitle(self.window_title)

        # Check default directory to open
        defaultdir = epsa_settings.value(SETTING_LAST_FILE_DIR)
        if defaultdir is None:
            defaultdir = ""

        epsa_logger.info("Created newfile.epsa")
        self.current_filepath = defaultdir
        self.current_filename = "newfile.epsa"

    def slot_openfile(self):
        # Check default directory to open
        defaultdir = epsa_settings.value(SETTING_LAST_FILE_DIR)
        if defaultdir is None:
            defaultdir = ""

        filename = QFileDialog.getOpenFileName(self, "Open EPSA File...", defaultdir, "EPSA File (*.epsa)")

        fn_str = filename[0]
        res = re.search(
            r"[\D\d]+/",
            fn_str
        )
        self.current_filepath = res.group()[:-1]

        res = re.search(
            r"\w+\.epsa",
            fn_str
        )
        self.current_filename = res.group()


        if fn_str == "":
            epsa_logger.info(f"File open canceled")

        else:
            epsa_logger.info(f"Opening file {fn_str}")
            # Save opening directory
            res = re.search(
                r"[\D\d]+/",
                fn_str
            )
            fn_dir = res.group()[:-1]
            epsa_settings.setValue(SETTING_LAST_FILE_DIR, fn_dir)

    def slot_savefile(self):
        epsa_logger.info("Save File action called...")

        was_saved = False
        current_filepathname = f"{self.current_filepath}/{self.current_filename}"
        if current_filepathname[1:] == self.current_filename:
            # No directory specified yet
            was_saved = self.slot_savefileas()

        if was_saved:
            with open(current_filepathname, 'w') as f:
                f.write("Hello World!")
            self._is_saved = True

        # Remove star from window title to indicate file is saved 
        self.window_title = f"{self.base_title} - {self.current_filename}"
        self.setWindowTitle(self.window_title)

    def slot_savefileas(self):
        # Check default directory to open
        defaultdir = epsa_settings.value(SETTING_LAST_FILE_DIR)
        if defaultdir is None:
            defaultdir = ""

        current_filepathname = f"{self.current_filepath}/{self.current_filename}"

        if current_filepathname == "":
            fp = f"{defaultdir}/newfile.epsa"
        else:
            fp = current_filepathname

        filename = QFileDialog.getSaveFileName(self, "Save EPSA File As...", fp, "EPSA File (*.epsa)")

        fn_str = filename[0]

        if fn_str != "":
            res = re.search(
                r"[\D\d]+/",
                fn_str
            )
            self.current_filepath = res.group()[:-1]

            res = re.search(
                r"\w+\.epsa",
                fn_str
            )
            self.current_filename = res.group()


            if fn_str == "":
                epsa_logger.info(f"File Save As canceled")
                return False
            else:
                self.slot_savefile()
                epsa_logger.info(f"Saved file {fn_str}")
                # Save opening directory
                res = re.search(
                    r"[\D\d]+/",
                    fn_str
                )
                fn_dir = res.group()[:-1]
                epsa_settings.setValue(SETTING_LAST_FILE_DIR, fn_dir)
                return True

        return False

    def slot_import(self):
        epsa_logger.info("Import action called...")

    def slot_exporttxt(self):
        epsa_logger.info("Export Text File action called...")

    def slot_exportcsv(self):
        epsa_logger.info("Export CSV File action called...")

    def slot_preferences(self):
        # Launch the PreferencesWindow
        # UI defined in ui/preferences_window.ui
        epsa_logger.info("Opening preferences window")
        self.pref_window = PreferencesWindow()
        self.pref_window.show()

    def slot_run_epsa_calc(self):
        epsa_logger.info("Running EPSA Calculation...")

    def slot_about_epsa_wizard(self):
        epsa_logger.info("About EPSA Wizard action called...")

    def slot_documentation(self):
        epsa_logger.info("Documentation action called...")

    def slot_prevcomp(self):
        epsa_logger.info("Previous Component Button clicked...")

        # Get current item and index
        current_comp = self.ui.comptree.currentItem()

        # Get total number of components in given type
        total_items = current_comp.parent().childCount()

        # Use index model to get component's row
        item_index = self.ui.comptree.indexFromItem(current_comp)
        current_row = item_index.row()

        if current_row == 0:
            # We're at the beginning, loop to the end
            new_row = total_items - 1
        else:
            new_row = current_row - 1

        # Select new component
        self.ui.comptree.setCurrentItem(current_comp.parent().child(new_row))

        # Update component info label 
        self._update_compinfo_label()

    def slot_nextcomp(self):
        epsa_logger.info("Next Component Button clicked...")

        # Get current item and index
        current_comp = self.ui.comptree.currentItem()

        # Get total number of components in given type
        total_items = current_comp.parent().childCount()

        # Use index model to get component's row
        item_index = self.ui.comptree.indexFromItem(current_comp)
        current_row = item_index.row()

        if current_row == total_items - 1:
            # We're at the end, loop to the beginning
            new_row = 0
        else:
            new_row = current_row + 1

        # Select new component
        self.ui.comptree.setCurrentItem(current_comp.parent().child(new_row))

        # Update component info label 
        self._update_compinfo_label()

    def slot_delcomp(self):
        epsa_logger.info("Delete Component Button clicked...")

    def slot_newcomp(self):
        epsa_logger.info("New Component Button clicked...")

    def slot_savecomp(self):
        epsa_logger.info("Save Components Button clicked...")

        # Add star to window title to indicate unsaved changes
        self.window_title = f"{self.base_title} - {self.current_filename}*"
        self.setWindowTitle(self.window_title)

        # TODO: Run checks on data to see if it has actually changed
        self._is_saved = False

    def slot_compdefault(self):
        epsa_logger.info("Setting default component values...")

    def slot_treeitem_chosen(self, item, col):
        epsa_logger.info(f"Component Tree double clicked --- Ref Des {item.text(0)}, Second Column {item.text(1)}")
        self._update_compinfo_label()

    def _update_compinfo_label(self):
        epsa_logger.info(f"Updating Component Info label...")
        item = self.ui.comptree.currentItem()
        if item is None:
            return
        refdes = item.text(0)
        self.ui.lbl_compinfo.setText(f"Component {refdes}")

    def slot_exit(self):
        # TODO: Update this
        epsa_logger.info("Exit slot called...")

        # Save settings
        self._save_settings()

        check_passed = self._check_saved()
        if check_passed:
            self.close()

    def _check_saved(self):
        if self._is_saved is False:
            # Ask user if they want to save
            exit_save_mbox = QMessageBox()
            exit_save_mbox.setWindowTitle("EPSA Wizard: Unsaved Changes")
            exit_save_mbox.setText(f"Your current session has not been saved!")
            exit_save_mbox.setInformativeText(f"Do you want to save your changes?")
            exit_save_mbox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            exit_save_mbox.setIcon(QMessageBox.Warning)
            exit_save_mbox.setDefaultButton(QMessageBox.Save)
            box_font = QFont()
            box_font.setFamilies([u"Liberation Sans"])
            exit_save_mbox.setFont(box_font)

            # Get user input
            exit_save_return = exit_save_mbox.exec()

            if exit_save_return == QMessageBox.Save:
                epsa_logger.info(f"Saving from QMessageBox")
                self._save_settings()
                self.slot_savefile()
                self._is_closing = True
                return True
            elif exit_save_return == QMessageBox.Discard:
                epsa_logger.info(f"Discarding changes from QMessageBox")
                self._save_settings()
                self._is_closing = True
                return True
            elif exit_save_return == QMessageBox.Cancel:
                # Don't exit. Return from this slot.
                epsa_logger.info(f"Cancelled from QMessageBox")
                self._is_closing = False
                return False

        return True

    def closeEvent(self, event):
        epsa_logger.info("Request to close...")

        # If closeEvent is called twice, skip it
        if self._is_closing is True:
            event.accept()
            return

        # TODO: Here, we need to define any actions to take when exiting
        if self._is_saved is False:
            self.slot_exit()
            if self._is_closing is False:
                event.ignore()
                return

        event.accept()