from PySide6.QtCore import QSettings

epsa_settings = QSettings("RyanFrenchEE", "EPSA Wizard")

"""
Constants to use in program
"""
# Version
EPSA_WIZARD_VERSION = "0.0.1a2"

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
Preferences Options
"""
# ComboBox settings are stored according to their index
# Bools are stored as ints
PREFOPTIONS_UNITSYSTEM = ["Metric", "Imperial", "Custom"]
PREFOPTIONS_UNITLENGTH = ["Meter (m, mm, etc.)", "Foot (ft, in, thou, etc.)"]
PREFOPTIONS_UNITTEMP = ["°C", "°F", "K"]
PREFOPTIONS_UNITMASS = ["Kilogram (kg, mg, etc.)", "Pound (lb, oz, etc.)"]

"""
System variable names
"""

# Program (Global) Settings
SETTING_VERSION_NUMBER = "program/versionNumber"
SETTING_LAST_FILE_DIR = "program/lastFileDir"
SETTING_LAST_FILE_NAME = "program/lastFileName"

# Application (Runtime) Settings
SETTING_UNITSYSTEM = "application/unitSystem"
SETTING_UNITLENGTH = "application/unitLength"
SETTING_UNITTEMP = "application/unitTemp"
SETTING_UNITMASS = "application/unitMass"
SETTING_DEBUG = "application/debug"

# User Settings
SETTING_USERNAME = "user/userName"
SETTING_USERORG = "user/userOrg"
SETTING_USERTITLE = "user/userTitle"

# Main Window Settings
SETTING_MAIN_WINDOW_H = "mainwindow/windowHeight"
SETTING_MAIN_WINDOW_W = "mainwindow/windowWidth"