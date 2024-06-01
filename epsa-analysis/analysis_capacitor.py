# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# analysis_capacitor: Analyze the capacitor CSV file
# ----------------------------------------------------------------
# Created by    : Ryan French
# Created date  : 07/19/2023
# ----------------------------------------------------------------

from utilities import *

# List of all capacitors 
Cs = []

@dataclass
class Capacitor:
    # Input values:
    refdes: str
    rpn: str
    value: UnitQuantity
    V_rating: UnitQuantity
    V_max_applied: UnitQuantity
    T_baseplate: UnitQuantity
    θ_C: UnitQuantity
    T_rating_max: UnitQuantity
    V_ripple_bool: bool
    V_ripple_max_applied: UnitQuantity
    I_ripple_bool: bool
    I_ripple_max_applied: UnitQuantity
    I_ripple_rating: UnitQuantity
    esr: UnitQuantity
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
        self.V_rating_derated = C_V_DERATE * self.V_rating

        if self.V_ripple_bool:
            # Add ripple voltage to applied voltage
            self.V_max_applied += self.V_ripple_max_applied 
        
        if self.V_max_applied.magnitude < 10.0:
            # Add note about 100 Vdc rating
            self.notes = f"{self.notes} ATTN: For low-voltage applications, capacitor should be rated at least 100 Vdc (see EEE-INST-002)"

        if self.I_ripple_bool or (self.V_ripple_bool and self.I_ripple_bool):
            # Calculate power from I_ripple
            self.P_dissipated = self.I_ripple_max_applied**2 * self.esr
        elif self.V_ripple_bool and not self.I_ripple_bool:
            # Calculate power from V_ripple
            self.P_dissipated = self.V_ripple_max_applied**2 / self.esr
        else:
            # If neither, just set dissipated power to 0.0 W
            self.P_dissipated = ureg("0.0W")
        self.P_dissipated.ito('W')
        # Calculate temperature increase from dissipated power
        self.ΔT = (self.P_dissipated * self.θ_C)
        self.T_operating = UnitQuantity((self.T_baseplate.magnitude + self.ΔT.magnitude), ureg.degC)

        self.derating_pass()

    def derating_pass(self):
        """Decide if the capacitor passes derating

        Parameters
        ----------
        None

        Returns
        ----------
        None
        """
        self.V_headroom = self.V_rating_derated - self.V_max_applied
        self.T_headroom = UnitQuantity((self.T_rating_max.magnitude - self.T_operating.magnitude), ureg.degC)

        self.V_pass = self.V_headroom.magnitude > 0.0
        self.T_pass = self.T_headroom.magnitude > 0.0
        self.C_pass = self.V_pass and self.T_pass

    def __str__(self):
        # String representation for pretty-printing
        return f"""\
Capacitor {self.refdes}:
---------------
RPN: {self.rpn}
Value: {self.value}
Voltage Rating: {self.V_rating:.2f}
Max V Applied (w/ Ripple): {self.V_max_applied:.2f}
Baseplate Temp: {self.T_baseplate:.1f}
Thermal Resistivity: {UnitQuantity(self.θ_C.magnitude, ureg.degC/ureg.W):.2f}
Max Temp Rating: {self.T_rating_max:.1f}
Vripple?: {self.V_ripple_bool}
Max V Ripple Applied: {self.V_ripple_max_applied:.2f}
Iripple?: {self.I_ripple_bool}
Max I Ripple Applied: {self.I_ripple_max_applied:.2f}
I Ripple Rating: {self.I_ripple_rating:.2f}
ESR: {self.esr}
Notes: {self.notes}

CALCULATED & DERATED VALUES:
------------------
Derated V Rating: {self.V_rating_derated.to_compact():.2f}
Dissipated Power: {self.P_dissipated.to_compact():.2f}
Temp Rise: {UnitQuantity(self.ΔT.magnitude, ureg.degC):.1f}
Operating Temp: {self.T_operating.to_compact():.1f}

PASS?
------------------
V pass: {self.V_pass} (Headroom: {self.V_headroom.to_compact():.2f})
T pass: {self.T_pass} (Headroom: {self.T_headroom.to_compact():.1f})
PASS: {self.C_pass}
"""



def analyze_capacitors(C_csv_file=CAPACITOR_CSV_FILENAME):
    """Analyze all capacitors in the capacitors CSV file

    Parameters
    ----------
    C_csv_file : str [default="capacitors.csv"]
        Filename of the capacitors CSV file. Must contain the file extension.

    Returns
    ----------
    None
    """
    print(f"Analyzing {C_csv_file}...")
    # Check if the CSV file exists
    if not os.path.isfile(f"./{C_csv_file}"):
        raise Exception(f"Error: No capacitors CSV file named {C_csv_file}! Exiting.")

    with open(C_csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # Skip header
        for idx, row in enumerate(reader):
            # Read in values from CSV
            refdes = row[0]
            rpn = row[1]
            if row[2].endswith("F"):
                value = ureg(f"{row[2]}")
            else:
                value = ureg(f"{row[2]}F")
            V_rating = ureg(f"{row[3]}V")
            V_max_applied = ureg(f"{row[4]}V")
            T_baseplate = UnitQuantity(float(row[5]), ureg.degC)

            if row[6].lower() in ['', "default"]:
                θ_C = UnitQuantity(C_DEFAULT_θ, ureg.delta_degC/ureg.W)
            else:
                θ_C = UnitQuantity(float(row[6]), ureg.delta_degC/ureg.W)

            T_rating_max = UnitQuantity(float(row[7]), ureg.degC)
            V_ripple_bool = row[8]

            if V_ripple_bool.lower() in ["true", "yes"]:
                V_ripple_bool = True
                V_ripple_max_applied = ureg(f"{row[9]}V") 
            else:
                V_ripple_bool = False
                V_ripple_max_applied = ureg("0.0V")

            I_ripple_bool = row[10]

            if I_ripple_bool.lower() in ["true", "yes"]:
                I_ripple_bool = True
                I_ripple_max_applied = ureg(f"{row[11]}A")
            else:
                I_ripple_bool = False
                I_ripple_max_applied = ureg("0.0A") 

            if row[12].lower() in ['', "default"]:
                I_ripple_rating = UnitQuantity(C_DEFAULT_IRIPPLE, ureg.amp)
            else:
                I_ripple_rating = ureg(f"{row[12]}A")

            if row[13].lower() in ['', "default"]:
                esr = UnitQuantity(C_DEFAULT_ESR, ureg.ohm)
            else:
                esr = ureg(f"{row[13]}ohm")

            notes = row[14]

            # Add values to dataclass
            C = Capacitor(
                refdes=refdes,
                rpn=rpn,
                value=value,
                V_rating=V_rating,
                V_max_applied=V_max_applied,
                T_baseplate=T_baseplate,
                θ_C=θ_C,
                T_rating_max=T_rating_max,
                V_ripple_bool=V_ripple_bool,
                V_ripple_max_applied=V_ripple_max_applied,
                I_ripple_bool=I_ripple_bool,
                I_ripple_max_applied=I_ripple_max_applied,
                I_ripple_rating=I_ripple_rating,
                esr=esr,
                notes=notes
            )
            C.calc_and_derate()
            # dprint(C)
            Cs.append(C)

def write_capacitors_to_excel(filename=EXCEL_FILENAME):
    """Write all the EPSA results to the Capacitors sheet

    Parameters
    ----------
    filename : str [default: "epsa-results.xlsx"]
        Filename to write the results to. Must contain the file extension.

    Returns
    ----------
    None
    """
    print(f"Writing Capacitor EPSA results to {filename}...")
    # Header text for the sheet
    headers = [
        "Ref Des",
        "RES",
        "Value",
        "Voltage Rating",
        "Vripple?",
        "Max Vripple Applied",
        "Max V Applied (w/ Ripple)",
        "Iripple?",
        "Max Iripple Applied",
        "Iripple Rating",
        "Baseplate Temp",
        "Thermal Resistivity",
        "Max Temp Rating",
        "ESR",
        "Derated V Rating",
        "Dissipated Power",
        "Temp Rise",
        "Operating Temp",
        "V Pass",
        "V Headroom",
        "T Pass",
        "T Headroom",
        "Overall Pass",
        "Notes"
    ]

    wb = load_workbook(filename)

    # Check if the Capacitors sheet exists. If not, create it
    if "Capacitors" not in wb.get_sheet_names():
        wb.create_sheet("Capacitors")

    # Change to Capacitors sheet and add headers 
    ws = wb["Capacitors"]
    ws.append(headers)

    for capacitor in Cs:
        # Write all values
        vals = [
            f"{capacitor.refdes}",
            f"{capacitor.rpn}",
            f"{capacitor.value.to_compact():~P.2f}",
            f"{capacitor.V_rating.to_compact():~P.2f}",
            f"{capacitor.V_ripple_bool}",
            f"{capacitor.V_ripple_max_applied.to_compact():~P.2f}",
            f"{capacitor.V_max_applied.to_compact():~P.2f}",
            f"{capacitor.I_ripple_bool}",
            f"{capacitor.I_ripple_max_applied.to_compact():~P.2f}",
            f"{capacitor.I_ripple_rating.to_compact():~P.2f}",
            f"{UnitQuantity(capacitor.T_baseplate.magnitude, ureg.degC):~P.1f}",
            f"{UnitQuantity(capacitor.θ_C.magnitude, ureg.degC/ureg.W):~P.1f}",
            f"{UnitQuantity(capacitor.T_rating_max.magnitude, ureg.degC):~P.1f}",
            f"{capacitor.esr:~P.2f}",
            f"{capacitor.V_rating_derated.to_compact():~P.2f}",
            f"{capacitor.P_dissipated.to_compact():~P.2f}",
            f"{UnitQuantity(capacitor.ΔT.magnitude, ureg.degC):~P.1f}",
            f"{UnitQuantity(capacitor.T_operating.magnitude, ureg.degC):~P.1f}",
            f"{capacitor.V_pass}",
            f"{capacitor.V_headroom.to_compact():~P.2f}",
            f"{capacitor.T_pass}",
            f"{UnitQuantity(capacitor.T_headroom.magnitude, ureg.degC):~P.1f}",
            f"{capacitor.C_pass}",
            f"{capacitor.notes}"
        ]
        ws.append(vals)

    # Center all text vertically and horizontally
    for row in range(1, ws.max_row+1):
        for col in range(1, ws.max_column+1):
            cell = ws.cell(row, col)
            cell.alignment = Alignment(horizontal="center", vertical="center")

    if DEBUG:
        wb.save(f"{filename[:-5]}_capacitors.xlsx")
        wb.close()
    else:
        wb.save(filename)
        wb.close()

def get_C_passes():
    """Get all the passing values for the capacitors 

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """
    c_v_pass_list = PassClass("V Passes", 0)
    c_t_pass_list = PassClass("T Passes", 0)
    c_pass_list = PassClass("Overall Passes", 0)
    for C in Cs:
        if C.V_pass:
            c_v_pass_list.pass_num += 1
        if C.T_pass:
            c_t_pass_list.pass_num += 1
        if C.C_pass:
            c_pass_list.pass_num += 1

    c_passes = Passes("Capacitors", len(Cs),
    [
        c_pass_list,
        c_v_pass_list,
        c_t_pass_list
    ])
    dprint(c_passes)
    return c_passes
