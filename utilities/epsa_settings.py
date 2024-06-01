from PySide6.QtCore import QSettings

epsa_settings = QSettings("RyanFrenchEE", "EPSA Wizard")

"""
Constants to use in program
"""
# Version
EPSA_WIZARD_VERSION = "0.0.1alpha"

# Global debug flag
EPSA_DEBUG = True

# USER INTERFACE CONSTANTS
WINDOW_INIT_W = 600
WINDOW_INIT_H = 350
MENUBAR_INIT_H = 20
COMPTREE_MIN_W = 150
COMPTREE_MAX_W = 250
COMPTREE_MIN_H = 300
COMPTREE_MAX_H = 16777215
LBL_COMPACTION_MIN_W = 125
LBL_COMPACTION_MAX_W = 200
LBL_COMPACTION_MIN_H = 25
LBL_COMPACTION_MAX_H = 50
BTNS_COMPACTION_MIN_W = 60
BTNS_COMPACTION_MAX_W = 150
BTNS_COMPACTION_MIN_H = 25
BTNS_COMPACTION_MAX_H = 50


"""
System variable names
"""

# Program Settings
SETTING_VERSION_NUMBER = "program/versionNumber"

# Main Window Settings
SETTING_MAIN_WINDOW_H = "mainwindow/windowHeight"
SETTING_MAIN_WINDOW_W = "mainwindow/windowWidth"