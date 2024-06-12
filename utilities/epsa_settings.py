from dataclasses import dataclass
import typing
from utilities.epsa_logging import epsa_logger
from PySide6.QtCore import QSettings

# Create settings object. This is global since any call to QSettings w/
# the given strings will always save to the same location
epsa_settings = QSettings("RFrenchEE", "EPSA Wizard")

"""
Constants to use in program
"""
# Version
EPSA_WIZARD_VERSION = "0.0.1a2"

# Global debug flag
EPSA_DEBUG = True

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

@dataclass
class EPSASetting():
    # Registry key name. Must follow camelCase naming conventions!
    registrykey: str
    # Default value. This can be many things, so keep type generic
    default: typing.Any

# Define all settings here
epsa_settingdefs = {
    "version" : EPSASetting("version", EPSA_WIZARD_VERSION),
    "window_height" : EPSASetting("windowHeight", 400),
    "window_width" : EPSASetting("windowWidth", 600),
    "last_file_dir" : EPSASetting("lastFileDir", ""),
    "last_file_name" : EPSASetting("lastFileName", "newfile.epsa"),
    "unit_system" : EPSASetting("unitSystem", 0),
    "unit_length" : EPSASetting("unitLength", 0),
    "unit_temp" : EPSASetting("unitTemp", 0),
    "unit_mass" : EPSASetting("unitMass", 0),
    "debug_flag" : EPSASetting("debug", 0),
    "name" : EPSASetting("userName", "FirstName LastName"),
    "org" : EPSASetting("userOrg", "Great Engineering Company"),
    "title" : EPSASetting("userTitle", "Master Engineer"),
}

def EPSA_check_settings():
    epsa_logger.info("Checking settings and update any missing settings w/ defaults")

    for settingname, setting_obj in epsa_settingdefs.items():
        currentval = epsa_settings.value(setting_obj.registrykey)
        print(f"Setting {settingname} :")
        print(f"Current value: {currentval}")

        if settingname == "version":
            # Check if version registry key matches the hard-coded version here
            if currentval is None or currentval != EPSA_WIZARD_VERSION:
                epsa_settings.setValue(setting_obj.registrykey, EPSA_WIZARD_VERSION)

        else:
            # Otherwise, check for Nones and fill them in
            if currentval is None or currentval == "":
                epsa_settings.setValue(setting_obj.registrykey, setting_obj.default)


def EPSA_save_settings(settingdict) -> None:
    for settingname, settingval in settingdict.items():
        epsa_settings.setValue(epsa_settingdefs[settingname].registrykey, settingval)

def EPSA_get_setting(settingname):
    return epsa_settings.value(epsa_settingdefs[settingname].registrykey)