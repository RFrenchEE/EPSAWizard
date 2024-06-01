# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# utilities: Constants and functions to use in all other modules 
# ----------------------------------------------------------------
# Created by    : Ryan French
# Created date  : 07/19/2023
# ----------------------------------------------------------------

import sys
import os.path
import pint
from configparser import ConfigParser
from dataclasses import dataclass
from typing import List
import csv
import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Color, PatternFill, Alignment, Border, Side
from openpyxl.drawing.image import Image as ExcelImage
from openpyxl_image_loader import SheetImageLoader

# Set up the INI parser
cp = ConfigParser()
cp.read("config.ini")

# Unit registry
ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=False)
pint.set_application_registry(ureg)

# Pretty print all units
ureg.default_format = "~P"

# Define quantity
UnitQuantity = pint.Quantity

# Project information
PROJECT_NAME = cp.get("project_info", "PROJECT_NAME")
BOARD_NAME = cp.get("project_info", "BOARD_NAME")
PCB_RES = cp.get("project_info", "PCB_RES")
PCB_REV = cp.get("project_info", "PCB_REV")
PCA_RES = cp.get("project_info", "PCA_RES")
PCA_REV = cp.get("project_info", "PCA_REV")

# Debug global constant
DEBUG = cp.getboolean("debug", "DEBUG")

# Software version
SCRIPT_VERSION = cp.get("version", "SCRIPT_VERSION")

# Filenames
EXCEL_FILENAME = cp.get("filenames", "EXCEL_FILENAME")
RESISTOR_CSV_FILENAME = cp.get("filenames", "RESISTOR_CSV_FILENAME")
CAPACITOR_CSV_FILENAME = cp.get("filenames", "CAPACITOR_CSV_FILENAME")
INDUCTOR_CSV_FILENAME = cp.get("filenames", "INDUCTOR_CSV_FILENAME")

# Resistor derating values
R_V_DERATE = cp.getfloat("resistors", "R_V_DERATE")
R_P_DERATE = cp.getfloat("resistors", "R_P_DERATE")
R_P_PULSE_DERATE = cp.getfloat("resistors", "R_P_PULSE_DERATE")
R_ZERO_DEFAULT = cp.get("resistors", "R_ZERO_DEFAULT")

# Capacitor values
C_V_DERATE = cp.getfloat("capacitors", "C_V_DERATE")
C_DEFAULT_ESR = cp.getfloat("capacitors", "C_DEFAULT_ESR")
C_DEFAULT_IRIPPLE = cp.getfloat("capacitors", "C_DEFAULT_IRIPPLE")
C_MAX_AMB_TEMP = cp.getfloat("capacitors", "C_MAX_AMB_TEMP")
C_DEFAULT_θ = cp.getfloat("capacitors", "C_DEFAULT_THETA")

# Inductor values
L_T_DERATE = cp.getfloat("inductors", "L_TEMP_DERATE")
L_V_DERATE = cp.getfloat("inductors", "L_V_DERATE")

@dataclass
class PassClass:
    pass_name: str
    pass_num: int

@dataclass
class Passes:
    name: str # Name of the EPSA subject (Resistors, Capacitors, etc.)
    total: int
    pass_list: List[PassClass]



def dprint(s):
    """Debug print

    Parameters
    ----------
    s : string
        (Formatted) string to print if DEBUG is True

    Returns
    ----------
    None
    """
    if DEBUG:
        print(s)

def EPSA_except_hook(type, value, traceback, oldhook=sys.excepthook):
    oldhook(type, value, traceback)
    input("\n\n Press Enter to exit.")