"""resistors.py

Code to define the EPSA_Resistor class, which stores
all information about a resistor, as well as performs
the EPSA resistor calculations
"""

# Nonlocal imports
from dataclasses import dataclass
from enum import Enum
from typing import List

# Local imports
from utilities.pprinter import pprint_function_called, pprint_method_called
from utilities.epsa_units import UnitQuantity
from utilities._component_errors import ComponentNote
from utilities.epsa_logging import epsa_logger

epsa_logger.debug("Imported resistors.py")

@dataclass
class ResistorStyle:
    name: str # Name of resistor style from table 4 [string]
    description: str # Description of resistor style [string]
    derating_factor_power: float # Power derating factor [float]
    derating_factor_voltage: float # Voltage derating factor [float]
    derating_temp_T1: float # Derating temperature T1 [float, °C]
    derating_temp_T2: float # Derating temperature T2 [float, °C]
    zero_power_temp_T3: float # Zero power temperature T3 [float, °C]

# Dictionary of resistor styles, as listed in Table 4
resistor_style_dict = {
    "G311P672" : ResistorStyle(
        name="G311P672",
        description="Fixed, High Voltage",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=94.0,
        zero_power_temp_T3=110.0
    ),
    "G311P683" : ResistorStyle(
        name="G311P683",
        description="Fixed, Precision, High Voltage",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=185.0,
        zero_power_temp_T3=225.0
    ),
    "G311P742" : ResistorStyle(
        name="G311P742",
        description="Fixed, Low TC, Precision",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=155.0,
        zero_power_temp_T3=175.0
    ),
    "RBR, 1%" : ResistorStyle(
        name="RBR, 1%",
        description="Fixed, Wirewound (Accurate), ER, 1%",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=137.0,
        zero_power_temp_T3=145.0
    ),
    "RBR, 0.5%" : ResistorStyle(
        name="RBR, 0.5%",
        description="Fixed, Wirewound (Accurate), ER, 0.5%",
        derating_factor_power=0.35,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=132.0,
        zero_power_temp_T3=145.0
    ),
    "RBR, 0.1%" : ResistorStyle(
        name="RBR, 0.1%",
        description="Fixed, Wirewound (Accurate), ER, 0.1%",
        derating_factor_power=0.25,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=130.0,
        zero_power_temp_T3=145.0
    ),
    "RWR" : ResistorStyle(
        name="RWR",
        description="Fixed, Wirewound (Power Type), ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=25.0,
        derating_temp_T2=160.0,
        zero_power_temp_T3=250.0
    ),
    "RCR" : ResistorStyle(
        name="RCR",
        description="Fixed, Composition (Insulated), ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=0.0, # NOTE: This must be calculated, per Note 3
        zero_power_temp_T3=0.0 # NOTE: This must be calculated, per Note 3
    ),
    "RER" : ResistorStyle(
        name="RER",
        description="Fixed, Wirewound (Power Type), Chassi Mounted, ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=25.0,
        derating_temp_T2=160.0,
        zero_power_temp_T3=250.0
    ),
    "RTR" : ResistorStyle(
        name="RTR",
        description="Variable, Wirewound (Lead Screw Acutated), ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=25.0,
        derating_temp_T2=160.0,
        zero_power_temp_T3=250.0
    ),
    "RLR, 100ppm" : ResistorStyle(
        name="RLR, 100ppm",
        description="Fixed, Film (Insulated), ER, 100ppm",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=118.0,
        zero_power_temp_T3=150.0
    ),
    "RLR, 350ppm" : ResistorStyle(
        name="RLR, 350ppm",
        description="Fixed, Film (Insulated), ER, 350ppm",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=103.0,
        zero_power_temp_T3=125.0
    ),
    "RNX" : ResistorStyle(
        name="RNX",
        description="Fixed, Film, ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=125.0,
        derating_temp_T2=155.0,
        zero_power_temp_T3=175.0
    ),
    "RM" : ResistorStyle(
        name="RM",
        description="Fixed, Film, Chip, ER",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=118.0,
        zero_power_temp_T3=150.0
    ),
    "RZ" : ResistorStyle(
        name="RZ",
        description="Fixed, Film, Networks",
        derating_factor_power=0.6,
        derating_factor_voltage=0.8,
        derating_temp_T1=70.0,
        derating_temp_T2=103.0,
        zero_power_temp_T3=125.0
    ),
    "Others" : ResistorStyle(
        name="Others",
        description="Various",
        derating_factor_power=0.5,
        derating_factor_voltage=0.8,
        derating_temp_T1=0.0, # NOTE: This must be calculated, per Note 4
        derating_temp_T2=0.0, # NOTE: This must be calculated, per Note 4
        zero_power_temp_T3=0.0 # NOTE: This must be calculated, per Note 4
    ),
}


@dataclass
class EPSA_Resistor:
    refdes: str # Reference designator [string]. Ex: "R42"
    mpn: str # Manufacturer part number [string]. Ex: "RC0402JR-0710KL"

    # Alternate part number. Useful if a company has a local inventory system. [string].
    # Can also be used for a backup MPN.  Ex: "COMPANY-1003377A"
    apn: str 
    value: UnitQuantity # Resistance [UnitQuantity(Ω)]
    power_rating: UnitQuantity # Power rating of resistor [UnitQuantity(W)]
    ΔVmax_applied: UnitQuantity # Maximum voltage applied across resistor [UnitQuantity(V)]
    T_baseplate: UnitQuantity # Baseplate temperature (usually PCB temperature) [UnitQuantity(°C)]
    θ_R: UnitQuantity # Thermal resistance of resistor [UnitQuantity(°C/W)]
    Vrated_max: UnitQuantity # Resistor's maximum rated ΔV [UnitQuantity(V)]
    T_rated: UnitQuantity # Resistor's maximum rated temperature [UnitQuantity(°C)]
    T_zero: UnitQuantity # Resistor's zero-power temperature [UnitQuantity(°C)]
    user_notes: List[str] # User notes about this part. Can have multiple. [list(str)]

    # Notes generated from the program during calculation. [list(ComponentNote)]
    # Can be just information, like the method of calculation used, or can be
    calc_notes: List[ComponentNote]
    style: ResistorStyle # Resistor style