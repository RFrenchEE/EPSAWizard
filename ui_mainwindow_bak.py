"""ui_mainwindow - Main window of EPSA Wizard

Contains the Qt 6 class for the main window of the application. Initial code was generated from Qt Creator,
then modified further by hand.
"""

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QSettings
)

from PySide6.QtGui import (
    QAction, QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence,
    QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform
)

from PySide6.QtWidgets import (
    QAbstractItemView, QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,
    QFileDialog, QMessageBox
)

from utilities._program_consts import *
from utilities._settings_consts import *
from utilities.epsa_logging import epsa_logger

from src.component_defs.resistors import EPSA_Resistor

from resistor_widget import ResistorWidget

# The imports below are necessary to properly import SVGs on Windows 10, 64-bit.
# No idea why. See https://github.com/derrian-distro/LoRA_Easy_Training_Scripts/issues/94
from PySide6 import QtSvg, QtXml

# TODO: Think about where to put the left and right arrows to cycle through items in the parent tree node. And how to link this to left/right keys???

epsa_logger.debug("Imported ui_mainwindow.py")

# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        epsa_logger.debug("Instantiating MainWindow")
        super().__init__()
        # Variable to note if the window is currently being closed.
        # This is neccessary because our _slot_exit()
        self._is_closing = False

        # Is the file saved?
        self._is_saved = False

        # TODO: Set version in settings
        self.setWindowTitle("EPSA Wizard v.???")

        # Set up icons and other constants
        self._setup_constants()

        # Set up the UI
        self._setup_ui()

    def _setup_ui(self):
        epsa_logger.info("Setting up MainWindow UI")
        # Load settings
        self._load_settings()

        # Set window width and height
        window_width = self.settings.value(SETTING_MAIN_WINDOW_W)
        window_height = self.settings.value(SETTING_MAIN_WINDOW_H)
        self.resize(window_width, window_height)

        # Size policy: Expanding X & Y
        sizepolicy_expandxy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizepolicy_expandxy.setHorizontalStretch(0)
        sizepolicy_expandxy.setVerticalStretch(0)
        self.setSizePolicy(sizepolicy_expandxy)

        # Size policy: Preferred X & Y
        sizepolicy_preferredxy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizepolicy_preferredxy.setHorizontalStretch(0)
        sizepolicy_preferredxy.setVerticalStretch(0)

        # Size policy: Preferred X, Fixed Y
        sizepolicy_preferredx_fixedy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizepolicy_preferredx_fixedy.setHorizontalStretch(0)
        sizepolicy_preferredx_fixedy.setVerticalStretch(0)

        # Size policy: Preferred X, Expanding Y
        sizepolicy_preferredx_expandy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizepolicy_preferredx_expandy.setHorizontalStretch(0)
        sizepolicy_preferredx_expandy.setVerticalStretch(0)

        # Set up the font for the main window
        self.font_main = QFont()
        self.font_main.setFamilies([u"Liberation Sans"])
        self.setFont(self.font_main)
        self.setFocusPolicy(Qt.NoFocus)

        # Set up some fonts
        # Liberation Sans, 12pt, Bold
        font_libsans_12_bold = QFont()
        font_libsans_12_bold.setFamilies([u"Liberation Sans"])
        font_libsans_12_bold.setPointSize(12)
        font_libsans_12_bold.setBold(True)

        # Liberation Sans, 10pt
        font_libsans_10 = QFont()
        font_libsans_10.setFamilies([u"Liberation Sans"])
        font_libsans_10.setPointSize(10)

        # Set up main window icon
        icon_wizard = QIcon()
        icon_wizard.addFile(u"./images/epsa_wizard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon_wizard)
        self.setTabShape(QTabWidget.Rounded)


        '''SECTION: FRAMES AND LAYOUT'''
        # Central widget
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.setCentralWidget(self.centralwidget)

        # Main horizontal layout (layout_main_h)
        self.layout_main_h = QHBoxLayout(self.centralwidget)
        self.layout_main_h.setObjectName(u"layout_main_h")
        self.layout_main_h.setContentsMargins(-1, -1, -1, -1) # -1 valued -> (0, 13, 0, 0)

        # Left frame: Component tree widgets (frame_comptree)
        self.frame_comptree = QFrame(self.centralwidget)
        self.frame_comptree.setObjectName(u"frame_comptree")
        self.frame_comptree.setFrameShape(QFrame.Box)
        self.frame_comptree.setFrameShadow(QFrame.Raised)

        # Right frame: Component info widgets (frame_compinfo)
        self.frame_compinfo = QFrame(self.centralwidget)
        self.frame_compinfo.setObjectName(u"frame")
        self.frame_compinfo.setFrameShape(QFrame.Box)
        self.frame_compinfo.setFrameShadow(QFrame.Raised)

        # Component tree vertical layout (layout_comptree_v)
        self.layout_comptree_v = QVBoxLayout(self.frame_comptree)
        self.layout_comptree_v.setObjectName(u"layout_comptree_v")

        # Component info vertical layout (layout_compinfo_v)
        self.layout_compinfo_v = QVBoxLayout(self.frame_compinfo)
        self.layout_compinfo_v.setObjectName(u"layout_compinfo_v")

        '''SECTION: WIDGETS'''
        # Component tree label
        self.label_comptree = QLabel(self.frame_comptree)
        self.label_comptree.setObjectName(u"label_comptree")
        self.label_comptree.setFont(font_libsans_12_bold)
        self.label_comptree.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        # Component tree
        self.component_tree = QTreeWidget(self.frame_comptree)
        self.component_tree.setObjectName(u"component_tree")
        self.component_tree.setSizePolicy(sizepolicy_preferredx_expandy)
        self.component_tree.setMinimumSize(QSize(COMPTREE_MIN_W, COMPTREE_MIN_H))
        self.component_tree.setMaximumSize(QSize(COMPTREE_MAX_W, COMPTREE_MAX_H))
        self.component_tree.setFrameShape(QFrame.StyledPanel)
        self.component_tree.setFrameShadow(QFrame.Sunken)
        self.component_tree.setLineWidth(5)
        self.component_tree.setEditTriggers(
            QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed
        )
        self.component_tree.setTabKeyNavigation(True)
        self.component_tree.setAlternatingRowColors(True)
        self.component_tree.setIconSize(QSize(5, 5))
        self.component_tree.setColumnCount(1)
        self.component_tree.setSortingEnabled(False)
        self.component_tree.itemClicked.connect(self._slot_tree_clicked)
        self.component_tree.itemDoubleClicked.connect(self._slot_tree_doubleclicked)
        self.component_tree.itemSelectionChanged.connect(self._slot_tree_selectionchanged)
        self.component_tree.itemActivated.connect(self._slot_tree_activated)


        # Component info label
        self.label_compinfo = QLabel(self.frame_compinfo)
        self.label_compinfo.setObjectName(u"label")
        sizepolicy_label_compinfo = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizepolicy_label_compinfo.setHorizontalStretch(0)
        sizepolicy_label_compinfo.setVerticalStretch(0)
        self.label_compinfo.setSizePolicy(sizepolicy_label_compinfo)
        self.label_compinfo.setMaximumSize(QSize(16777215, 20))
        self.label_compinfo.setFont(font_libsans_12_bold)
        self.label_compinfo.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        # Component info widget: This is where each type of component will have user input fields
        # These widgets are unique to the component type. These will be defined elsewhere and
        # managed by the user making selections in the component tree
        # i.e., user clicks the "Resistors" dropdown or one of its children,
        # compinfo_widget is changed to the resistor's widget.
        self.compinfo_widget = ResistorWidget(self.frame_compinfo)
        # self.compinfo_widget = QWidget(self.frame_compinfo)
        self.compinfo_widget.setObjectName(u"compinfo_widget")
        self.compinfo_widget.setSizePolicy(sizepolicy_expandxy)

        # Component action frame: This is where buttons are available for the user to
        # do things to the selected component, such as delete or update. There is also
        # a button for creating a new component in the given component class.
        self.frame_compaction = QFrame(self.frame_compinfo)
        self.frame_compaction.setObjectName(u"frame_compaction")
        self.frame_compaction.setSizePolicy(sizepolicy_preferredxy)
        self.frame_compaction.setMinimumSize(QSize(0, 50))
        self.frame_compaction.setMaximumSize(QSize(16777215, 200))
        self.frame_compaction.setFrameShape(QFrame.Box)
        self.frame_compaction.setFrameShadow(QFrame.Sunken)
        self.frame_compaction.setLineWidth(1)

        # Component action horizontal layout
        self.layout_compaction_h = QHBoxLayout(self.frame_compaction)
        self.layout_compaction_h.setObjectName(u"layout_compaction_h")
        self.layout_compaction_h.setContentsMargins(-1, 12, -1, -1) # -1 valued -> (0, 13, 0, 0)

        # Component action label
        self.label_compaction = QLabel(self.frame_compaction)
        self.label_compaction.setObjectName(u"label_compaction")
        self.label_compaction.setSizePolicy(sizepolicy_preferredxy)
        self.label_compaction.setMinimumSize(QSize(LBL_COMPACTION_MIN_W, LBL_COMPACTION_MIN_H))
        self.label_compaction.setMaximumSize(QSize(LBL_COMPACTION_MAX_W, LBL_COMPACTION_MAX_H))
        self.label_compaction.setFont(font_libsans_10)
        self.label_compaction.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Horizontal spacer between component action label and buttons
        self.hspacer_compaction = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # "Delete" button
        self.btn_delete = QPushButton(self.frame_compaction)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setSizePolicy(sizepolicy_preferredx_fixedy)
        self.btn_delete.setMinimumSize(QSize(BTNS_COMPACTION_MIN_W, BTNS_COMPACTION_MIN_H))
        self.btn_delete.setMaximumSize(QSize(BTNS_COMPACTION_MAX_W, BTNS_COMPACTION_MAX_H))
        self.btn_delete.setIcon(self.icon_delete)
        self.btn_delete.clicked.connect(self._slot_delete_component)

        # "New" button
        self.btn_new = QPushButton(self.frame_compaction)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setSizePolicy(sizepolicy_preferredx_fixedy)
        self.btn_new.setMinimumSize(QSize(BTNS_COMPACTION_MIN_W, BTNS_COMPACTION_MIN_H))
        self.btn_new.setMaximumSize(QSize(BTNS_COMPACTION_MAX_W, BTNS_COMPACTION_MAX_H))
        self.btn_new.setIcon(self.icon_new)
        self.btn_new.clicked.connect(self._slot_new_component)

        # "Update" button
        self.btn_update = QPushButton(self.frame_compaction)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setSizePolicy(sizepolicy_preferredx_fixedy)
        self.btn_update.setMinimumSize(QSize(BTNS_COMPACTION_MIN_W, BTNS_COMPACTION_MIN_H))
        self.btn_update.setMaximumSize(QSize(BTNS_COMPACTION_MAX_W, BTNS_COMPACTION_MAX_H))
        self.btn_update.setIcon(self.icon_update)
        self.btn_update.clicked.connect(self._slot_update_component)


        # Set up actions (Top menus)
        self._actions_setup()

        # Set up menubar
        self._menubar_setup()

        # Add widgets to layout
        self._add_widgets_to_layout()

        # Add tooltips, shortcuts, etc.
        self._add_gui_details()

    def _actions_setup(self):
        epsa_logger.info("Setting up actions")
        # File > New
        self.action_new = QAction(self)
        self.action_new.setObjectName(u"action_new")
        self.action_new.setIcon(self.icon_newfile)
        self.action_new.setFont(self.font_main)
        self.action_new.triggered.connect(self._slot_file_new)

        # File > Open
        self.action_open = QAction(self)
        self.action_open.setObjectName(u"action_open")
        self.action_open.setIcon(self.icon_open)
        self.action_open.setFont(self.font_main)
        self.action_open.triggered.connect(self._slot_file_open)

        # File > Save
        self.action_save = QAction(self)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setIcon(self.icon_save)
        self.action_save.setFont(self.font_main)
        self.action_save.triggered.connect(self._slot_file_save)

        # File > Save As...
        self.action_saveas = QAction(self)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_saveas.setIcon(self.icon_saveas)
        self.action_saveas.setFont(self.font_main)
        self.action_saveas.triggered.connect(self._slot_file_saveas)

        # File > Import
        self.action_import = QAction(self)
        self.action_import.setObjectName(u"action_import")
        self.action_import.setIcon(self.icon_import)
        self.action_import.setFont(self.font_main)
        self.action_import.triggered.connect(self._slot_file_import)

        # File > Export > CSV
        self.action_exportcsv = QAction(self)
        self.action_exportcsv.setObjectName(u"action_exportcsv")
        self.action_exportcsv.setIcon(self.icon_exportcsv)
        self.action_exportcsv.setFont(self.font_main)
        self.action_exportcsv.triggered.connect(self._slot_file_exportcsv)

        # File > Export > Text
        self.action_exporttxt = QAction(self)
        self.action_exporttxt.setObjectName(u"action_exporttxt")
        self.action_exporttxt.setIcon(self.icon_exporttxt)
        self.action_exporttxt.setFont(self.font_main)
        self.action_exporttxt.triggered.connect(self._slot_file_exporttxt)

        # File > Preferences
        self.action_preferences = QAction(self)
        self.action_preferences.setObjectName(u"action_preferences")
        self.action_preferences.setIcon(self.icon_preferences)
        self.action_preferences.setFont(self.font_main)
        self.action_preferences.triggered.connect(self._slot_preferences_edit)

        # File > Exit
        self.action_exit = QAction(self)
        self.action_exit.setObjectName(u"action_exit")
        self.action_exit.setIcon(self.icon_exit)
        self.action_exit.setFont(self.font_main)
        self.action_exit.triggered.connect(self._slot_exit)

        # Calculate > Run EPSA Calculation
        self.action_calculate = QAction(self)
        self.action_calculate.setObjectName(u"action_calculate")
        self.action_calculate.setIcon(self.icon_calculate)
        self.action_calculate.setFont(self.font_main)

        # Help > About
        self.action_about = QAction(self)
        self.action_about.setObjectName(u"action_about")
        self.action_about.setIcon(self.icon_about)
        self.action_about.setFont(self.font_main)

        # Help > Documentation
        self.action_documentation = QAction(self)
        self.action_documentation.setObjectName(u"action_documentation")
        self.action_documentation.setIcon(self.icon_documentation)
        self.action_documentation.setFont(self.font_main)

    def _setup_constants(self):
        epsa_logger.info("Setting up constants (icons, etc.)")
        '''ICONS'''
        # New file
        self.icon_newfile = QIcon()
        self.icon_newfile.addFile(u"./images/file_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Open file
        self.icon_open = QIcon()
        self.icon_open.addFile(u"./images/folder_open.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Save file
        self.icon_save = QIcon()
        self.icon_save.addFile(u"./images/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Save file As...
        self.icon_saveas = QIcon()
        self.icon_saveas.addFile(u"./images/file_pen.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Import
        self.icon_import = QIcon()
        self.icon_import.addFile(u"./images/file_import.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Export CSV
        self.icon_exportcsv = QIcon()
        self.icon_exportcsv.addFile(u"./images/file_csv.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Export Text
        self.icon_exporttxt = QIcon()
        self.icon_exporttxt.addFile(u"./images/file_lines.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Exit
        self.icon_exit = QIcon()
        self.icon_exit.addFile(u"./images/x_circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Preferences
        self.icon_preferences = QIcon()
        self.icon_preferences.addFile(u"./images/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Calculate EPSA
        self.icon_calculate = QIcon()
        self.icon_calculate.addFile(u"./images/cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        # About
        self.icon_about = QIcon()
        self.icon_about.addFile(u"./images/info_circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Documentation
        self.icon_documentation = QIcon()
        self.icon_documentation.addFile(u"./images/book.svg", QSize(), QIcon.Normal, QIcon.Off)

        # Delete (Trash Can)
        self.icon_delete = QIcon()
        self.icon_delete.addFile(u"./images/trash_bin.svg", QSize(), QIcon.Normal, QIcon.Off)
        # New (Plus Sign)
        self.icon_new = QIcon()
        self.icon_new.addFile(u"./images/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        # Save (Checkmark)
        self.icon_update = QIcon()
        self.icon_update.addFile(u"./images/check.svg", QSize(), QIcon.Normal, QIcon.Off)

    def _add_widgets_to_layout(self):
        epsa_logger.info("Adding widgets to layout")
        # Add component tree frame, component info frame
        # in left-to-right in main horizontal layout
        self.layout_main_h.addWidget(self.frame_comptree)
        self.layout_main_h.addWidget(self.frame_compinfo)

        # Add label and tree to comptree (left-side) layout
        self.layout_comptree_v.addWidget(self.label_comptree)
        self.layout_comptree_v.addWidget(self.component_tree)

        # Add label, compinfo_widget, and component action
        # stuff to the compinfo (right-side) layout
        self.layout_compinfo_v.addWidget(self.label_compinfo)
        self.layout_compinfo_v.addWidget(self.compinfo_widget)
        self.layout_compinfo_v.addWidget(self.frame_compaction)

        # Add label, hspacer, component action buttons to
        # component action horizontal layout
        self.layout_compaction_h.addWidget(self.label_compaction)
        self.layout_compaction_h.addItem(self.hspacer_compaction)
        self.layout_compaction_h.addWidget(self.btn_delete)
        self.layout_compaction_h.addWidget(self.btn_new)
        self.layout_compaction_h.addWidget(self.btn_update)

    def _menubar_setup(self):
        epsa_logger.info("Setting up menubar")

        # Set up root menu bar
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, WINDOW_INIT_W, MENUBAR_INIT_H))
        self.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        # File menu [1]
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")

        # File > Export As submenu
        self.menu_exportas = QMenu(self.menu_file)
        self.menu_exportas.setObjectName(u"menu_exportas")
        icon_exportas = QIcon()
        icon_exportas.addFile(u"./images/file_export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_exportas.setIcon(icon_exportas)

        # Calculate menu [2]
        self.menu_calculate = QMenu(self.menubar)
        self.menu_calculate.setObjectName(u"menu_calculate")

        # View menu [3]
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")

        # Help menu [4]
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")

        # Add actions to File menu
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

        # Add actions to Export As submenu
        self.menu_exportas.addAction(self.action_exportcsv)
        self.menu_exportas.addAction(self.action_exporttxt)

        # Add actions to Calculate menu
        self.menu_calculate.addAction(self.action_calculate)

        # Add actions to Help menu
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_documentation)

        # Add menus to menubar
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_calculate.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

    def _add_gui_details(self):
        epsa_logger.info("Adding GUI details")
        self.setWindowTitle(QCoreApplication.translate("self", u"EPSA Wizard", None))
        self.action_new.setText(QCoreApplication.translate("self", u"New...", None))
        self.action_new.setToolTip(QCoreApplication.translate("self", u"Create a new EPSA file", None))
        self.action_new.setShortcut(QCoreApplication.translate("self", u"Ctrl+Shift+N", None))
        self.action_open.setText(QCoreApplication.translate("self", u"Open...", None))
        self.action_open.setToolTip(QCoreApplication.translate("self", u"Open an EPSA file", None))
        self.action_open.setShortcut(QCoreApplication.translate("self", u"Ctrl+O", None))
        self.action_save.setText(QCoreApplication.translate("self", u"Save", None))
        self.action_save.setToolTip(QCoreApplication.translate("self", u"Save the current EPSA file", None))
        self.action_save.setShortcut(QCoreApplication.translate("self", u"Ctrl+S", None))
        self.action_saveas.setText(QCoreApplication.translate("self", u"Save As...", None))
        self.action_saveas.setToolTip(QCoreApplication.translate("self", u"Save the current EPSA file as...", None))
        self.action_saveas.setShortcut(QCoreApplication.translate("self", u"Ctrl+Shift+S", None))
        self.action_exit.setText(QCoreApplication.translate("self", u"Exit", None))
        self.action_exit.setShortcut(QCoreApplication.translate("self", u"Ctrl+Q", None))
        self.action_about.setText(QCoreApplication.translate("self", u"About", None))
        self.action_documentation.setText(QCoreApplication.translate("self", u"Documentation", None))
        self.action_documentation.setShortcut(QCoreApplication.translate("self", u"Ctrl+Shift+/", None))
        self.action_import.setText(QCoreApplication.translate("self", u"Import...", None))
        self.action_exportcsv.setText(QCoreApplication.translate("self", u"CSV", None))
        self.action_exporttxt.setText(QCoreApplication.translate("self", u"Text", None))
        self.action_preferences.setText(QCoreApplication.translate("self", u"Preferences", None))
        self.action_calculate.setText(QCoreApplication.translate("self", u"Run EPSA Calculation", None))
        self.action_calculate.setShortcut(QCoreApplication.translate("self", u"Ctrl+R", None))
        self.label_comptree.setText(QCoreApplication.translate("self", u"Component Tree", None))
        self.label_compinfo.setText(QCoreApplication.translate("self", u"Component Information", None))
        self.label_compaction.setText(QCoreApplication.translate("self", u"Component Actions", None))
        self.btn_delete.setToolTip(QCoreApplication.translate("self", u"Delete the current component", None))
        self.btn_delete.setText(QCoreApplication.translate("self", u"Delete", None))
        self.btn_delete.setShortcut(QCoreApplication.translate("self", u"Ctrl+D", None))
        self.btn_new.setToolTip(QCoreApplication.translate("self", u"Create a new component", None))
        self.btn_new.setText(QCoreApplication.translate("self", u"New", None))
        self.btn_new.setShortcut(QCoreApplication.translate("self", u"Ctrl+N", None))
        self.btn_update.setToolTip(QCoreApplication.translate("self", u"Update the current component's information", None))
        self.btn_update.setText(QCoreApplication.translate("self", u"Save", None))
        self.btn_update.setShortcut(QCoreApplication.translate("self", u"Ctrl+S", None))
        self.menu_file.setTitle(QCoreApplication.translate("self", u"File", None))
        self.menu_exportas.setTitle(QCoreApplication.translate("self", u"Export", None))
        self.menu_view.setTitle(QCoreApplication.translate("self", u"View", None))
        self.menu_help.setTitle(QCoreApplication.translate("self", u"Help", None))
        self.menu_calculate.setTitle(QCoreApplication.translate("self", u"Calculate", None))

        # Set up component tree
        self.component_tree.setHeaderLabels(["Ref Des"])
        # TODO: Remove the hard-coded tree entries
        tree_data = {
            "Capacitors" : [
                "C1", "C2", "C3", "C4", "C5", "C12",
            ],
            "Inductors" : [
                "L1", "L2", "L3",
            ],
            "Resistors" : [
                "R1", "R2", "R3", "R4"
            ]
        }

        items = []
        for k, vs in tree_data.items():
            item = QTreeWidgetItem([k])
            for v in vs:
                child = QTreeWidgetItem([v])
                item.addChild(child)
            items.append(item)
        self.component_tree.insertTopLevelItems(0, items)

    def _slot_tree_clicked(self):
        epsa_logger.info("Component Tree clicked")

    def _slot_tree_doubleclicked(self):
        epsa_logger.info("Component Tree double clicked")

    def _slot_tree_selectionchanged(self):
        epsa_logger.info("Component Tree selection changed")

    def _slot_tree_activated(self):
        epsa_logger.info("Component Tree activated")

    def _slot_delete_component(self):
        epsa_logger.info("Delete component button pressed")

    def _slot_new_component(self):
        epsa_logger.info("New component button pressed")

    def _slot_update_component(self):
        epsa_logger.info("Update component button pressed")

    def _slot_file_new(self):
        # TODO: Update this
        epsa_logger.info("New file action triggered")

    def _slot_file_open(self):
        # TODO: Update this
        epsa_logger.info("Open file action triggered")
        fn = QFileDialog.getOpenFileName(self, "Open EPSA File...", "C:\\", "Image Files(*.jpg *.png)")
        print(f"File to open: {fn}")

    def _slot_file_save(self):
        # TODO: Update this
        epsa_logger.info("Save file action triggered")

    def _slot_file_saveas(self):
        # TODO: Update this
        epsa_logger.info("File save as action triggered")

    def _slot_file_import(self):
        # TODO: Update this
        epsa_logger.info("Import file action triggered")
        fn = QFileDialog.getOpenFileName(self, "Import File...", "C:\\", "(*.jpg *.png)")
        print(f"File to import: {fn}")

    def _slot_file_exportcsv(self):
        # TODO: Update this
        epsa_logger.info("Export CSV file action triggered")

    def _slot_file_exporttxt(self):
        # TODO: Update this
        epsa_logger.info("Export text file action triggered")

    def _slot_preferences_edit(self):
        # TODO: Update this
        epsa_logger.info("Edit preferences action triggered")

    def _slot_exit(self):
        # TODO: Update this
        epsa_logger.info("Exit action triggered")

        # Save settings
        self._save_settings()

        if self._is_saved is False:
            # Ask user if they want to save
            exit_save_mbox = QMessageBox()
            exit_save_mbox.setWindowTitle("EPSA Wizard: Unsaved Changes")
            exit_save_mbox.setText(f"Your current session has not been saved!")
            exit_save_mbox.setInformativeText(f"Do you want to save your changes?")
            exit_save_mbox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            exit_save_mbox.setIcon(QMessageBox.Warning)
            exit_save_mbox.setDefaultButton(QMessageBox.Save)

            # Get user input
            exit_save_return = exit_save_mbox.exec()

            if exit_save_return == QMessageBox.Save:
                print(f"Saving before exit")
                self._save_settings()
                self._slot_file_save()
                self._is_closing = True
                self.close()
            elif exit_save_return == QMessageBox.Discard:
                print(f"Discarded changes")
                self._save_settings()
                self._is_closing = True
                self.close()
            elif exit_save_return == QMessageBox.Cancel:
                # Don't exit. Return from this slot.
                print(f"Cancelled the exit")
                self._is_closing = False

    def _save_settings(self):
        # Save all settings. Refer to the list of possible settings in utilities/_settings_consts.py
        epsa_logger.info("Save settings called")

        # Get window geometry
        window_geometry = self.frameGeometry()
        window_width = window_geometry.width()
        window_height = window_geometry.height()
        self.settings.setValue(SETTING_MAIN_WINDOW_H, window_height)
        self.settings.setValue(SETTING_MAIN_WINDOW_W, window_width)

    def _load_settings(self):
        epsa_logger.info("Load settings called")
        self.settings = QSettings("RyanFrenchEE", "EPSA Wizard")

        # Below, define the settings we want to import
        self._window_height_val = self.settings.value(SETTING_MAIN_WINDOW_H)
        self._window_width_val = self.settings.value(SETTING_MAIN_WINDOW_W)
        if self._window_height_val is None or self._window_width_val is None:
            self.settings.setValue(SETTING_MAIN_WINDOW_H, WINDOW_INIT_H)
            self.settings.setValue(SETTING_MAIN_WINDOW_W, WINDOW_INIT_W)

    def closeEvent(self, event):
        epsa_logger.info("closeEvent event called")

        # If closeEvent is called twice, skip it
        if self._is_closing is True:
            event.accept()
            return

        # TODO: Here, we need to define any actions to take when exiting
        self._save_settings()

        if self._is_saved is False:
            self._slot_exit()
            if self._is_closing is False:
                event.ignore()
                return

        event.accept()