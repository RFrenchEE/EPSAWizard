# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# analysis_inductor: Analyze the inductor CSV file 
# ----------------------------------------------------------------
# Created by    : Ryan French
# Created date  : 07/19/2023
# ----------------------------------------------------------------

from utilities import *

# List of all inductors 
Ls = []

@dataclass
class Inductor:
    # Input values:
    refdes: str
    rpn: str
    value: UnitQuantity
    V_incircuit_max: UnitQuantity
    V_dielectric_max: UnitQuantity
    T_operating_max: UnitQuantity
    T_operating_derated_bool: bool
    T_incircuit_max: UnitQuantity
    notes: str

    def calc_and_derate(self):
        """Calculate all derived quantities and do the derating

        Parameters
        ----------
        None

        Returns
        ----------
        None
        """
        self.V_operating_derated = L_V_DERATE * self.V_dielectric_max

        mil_temp_ratings = [85, 105, 125, 130, 150]
        
        if self.T_operating_derated_bool:
            self.T_operating_derated = self.T_operating_max
        else:
            if (self.T_operating_max.magnitude < 85.0 or self.T_operating_max.magnitude > 150.0):
                self.notes = f"{self.notes} ATTN: Operating temperature outside of normal range."
                # Temp rating not a Mil temperature, derate by factor of 0.75
                self.notes=f"{self.notes} ATTN: Operating temperature not a standard Mil temperature. Derating by factor of 0.75."
                self.T_operating_derated = UnitQuantity((0.75 * self.T_operating_max.magnitude), ureg.degC)
            else:
                if int(self.T_operating_max.magnitude) in mil_temp_ratings:
                    # Subtract derate factor
                    self.T_operating_derated = UnitQuantity((self.T_operating_max.magnitude - L_T_DERATE), ureg.degC)
                else:
                    # Temp rating not a Mil temperature, derate by factor of 0.75
                    self.notes=f"{self.notes} ATTN: Operating temperature not a standard Mil temperature. Derating by factor of 0.75."
                    self.T_operating_derated = UnitQuantity((0.75 * self.T_operating_max.magnitude), ureg.degC)
                    

        self.derating_pass()

    def derating_pass(self):
        """Decide if the inductor passes derating

        Parameters
        ----------
        None

        Returns
        ----------
        None
        """
        self.V_headroom = self.V_operating_derated - self.V_incircuit_max
        self.T_headroom = UnitQuantity((self.T_operating_derated.magnitude - self.T_incircuit_max.magnitude), ureg.degC)

        self.V_pass = self.V_headroom.magnitude > 0.0
        self.T_pass = self.T_headroom.magnitude > 0.0
        self.L_pass = self.V_pass and self.T_pass

    def __str__(self):
        # String representation for pretty-printing
        return f"""\
Inductor {self.refdes}:
---------------
RPN: {self.rpn}
Value: {self.value}
In-Circuit Vmax: {self.V_incircuit_max:.2f}
Dielectric Withstanding Voltage: {self.V_dielectric_max:.2f}
Max Operating Temp: {UnitQuantity(self.T_operating_max.magnitude, ureg.degC):.1f}
Max Operating Temp Already Derated?: {self.T_operating_derated_bool}
Max In-Circuit Temp: {UnitQuantity(self.T_incircuit_max.magnitude, ureg.degC):.1f}
Notes: {self.notes}

CALCULATED & DERATED VALUES:
------------------
Derated V Rating: {self.V_operating_derated.to_compact():.2f}
Derated Operating Temp: {self.T_operating_derated.to_compact():.1f}

PASS?
------------------
V pass: {self.V_pass} (Headroom: {self.V_headroom.to_compact():.2f})
T pass: {self.T_pass} (Headroom: {self.T_headroom.to_compact():.1f})
PASS: {self.L_pass}
"""


def analyze_inductors(L_csv_file=INDUCTOR_CSV_FILENAME):
    """Analyze all resistors in the resistors CSV file

    Parameters
    ----------
    R_csv_file : str [default="resistors.csv"]
        Filename of the resistors CSV file. Must contain the file extension.

    Returns
    ----------
    None
    """
    print(f"Analyzing {L_csv_file}...")
    # Check if the CSV file exists
    if not os.path.isfile(f"./{L_csv_file}"):
        raise Exception(f"Error: No inductors CSV file named {L_csv_file}! Exiting.")

    with open(L_csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # Skip header
        for idx, row in enumerate(reader):
            # Read in values from CSV
            refdes = row[0]
            rpn = row[1]
            if row[2].endswith("H"):
                value = ureg(f"{row[2]}")
            else:
                value = ureg(f"{row[2]}H")
            V_incircuit_max = ureg(f"{row[3]}V")
            V_dielectric_max = ureg(f"{row[4]}V")
            T_operating_max = UnitQuantity(float(row[5]), ureg.degC)

            T_operating_derated_bool = row[6]
            if T_operating_derated_bool in ["true", "yes"]:
                T_operating_derated_bool = True
            else:
                T_operating_derated_bool = False

            T_incircuit_max = UnitQuantity(float(row[7]), ureg.degC)
            notes = row[8]

            L = Inductor(
                refdes=refdes,
                rpn=rpn,
                value=value,
                V_incircuit_max=V_incircuit_max,
                V_dielectric_max=V_dielectric_max,
                T_operating_max=T_operating_max,
                T_operating_derated_bool=T_operating_derated_bool,
                T_incircuit_max=T_incircuit_max,
                notes=notes
            )
            L.calc_and_derate()
            Ls.append(L)

def write_inductors_to_excel(filename=EXCEL_FILENAME):
    """Write all the EPSA results to the Inductors sheet

    Parameters
    ----------
    filename : str [default: "epsa-results.xlsx"]
        Filename to write the results to. Must contain the file extension.

    Returns
    ----------
    None
    """
    print(f"Writing Inductor EPSA results to {filename}...")
    # Header text for the sheet
    headers = [
        "Ref Des",
        "RES",
        "Value",
        "Max In-Circuit V",
        "Dielectric Withstanding V",
        "Max Operating Temp",
        "Operating Temp Already Derated?",
        "Max In-Circuit Temp",
        "Derated Vmax",
        "Derated Operating Temp",
        "V Pass",
        "V Headroom",
        "T Pass",
        "T Headroom",
        "Overall Pass",
        "Notes"
    ]

    wb = load_workbook(filename)

    # Check if the Inductors sheet exists. If not, create it
    if "Inductors" not in wb.get_sheet_names():
        wb.create_sheet("Inductors")

    # Change to Inductors sheet and add headers 
    ws = wb["Inductors"]
    ws.append(headers)

    for inductor in Ls:
        # Write all values
        vals = [
            f"{inductor.refdes}",
            f"{inductor.rpn}",
            f"{inductor.value.to_compact():~P.2f}",
            f"{inductor.V_incircuit_max.to_compact():~P.2f}",
            f"{inductor.V_dielectric_max.to_compact():~P.2f}",
            f"{UnitQuantity(inductor.T_operating_max.magnitude, ureg.degC):~P.1f}",
            f"{inductor.T_operating_derated_bool}",
            f"{UnitQuantity(inductor.T_incircuit_max.magnitude, ureg.degC):~P.1f}",
            f"{inductor.V_operating_derated.to_compact():~P.2f}",
            f"{UnitQuantity(inductor.T_operating_derated.magnitude, ureg.degC):~P.1f}",
            f"{inductor.V_pass}",
            f"{inductor.V_headroom.to_compact():~P.2f}",
            f"{inductor.T_pass}",
            f"{UnitQuantity(inductor.T_headroom.magnitude, ureg.degC):~P.1f}",
            f"{inductor.L_pass}",
            f"{inductor.notes}"
        ]
        ws.append(vals)

    # Center all text vertically and horizontally
    for row in range(1, ws.max_row+1):
        for col in range(1, ws.max_column+1):
            cell = ws.cell(row, col)
            cell.alignment = Alignment(horizontal="center", vertical="center")
    
    if DEBUG:
        wb.save(f"{filename[:-5]}_inductors.xlsx")
        wb.close()
    else:
        wb.save(filename)
        wb.close()

def get_L_passes():
    """Get all the passing values for the inductors 

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """
    l_v_pass_list = PassClass("V Passes", 0)
    l_t_pass_list = PassClass("T Passes", 0)
    l_pass_list = PassClass("Overall Passes", 0)
    for L in Ls:
        if L.V_pass:
            l_v_pass_list.pass_num += 1
        if L.T_pass:
            l_t_pass_list.pass_num += 1
        if L.L_pass:
            l_pass_list.pass_num += 1

    l_passes = Passes("Inductors", len(Ls),
    [
        l_pass_list,
        l_v_pass_list,
        l_t_pass_list
    ])
    return l_passes
