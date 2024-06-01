# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# analysis_resistor: Analyze the resistor CSV file
# ----------------------------------------------------------------
# Created by    : Ryan French
# Created date  : 07/19/2023
# ----------------------------------------------------------------

from utilities import *

# List of all resistors
Rs = []

@dataclass
class Resistor:
    # Input values:
    refdes: str
    rpn: str
    value: UnitQuantity
    P_rating: UnitQuantity
    V_max_applied: UnitQuantity
    T_baseplate: UnitQuantity
    θ_R: UnitQuantity
    V_rated_max: UnitQuantity
    pulse_bool: bool
    V_max_pulse_applied: UnitQuantity
    T_rated: UnitQuantity
    T_zero: UnitQuantity
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

        # Check for 0 Ω
        if self.value == 0.0:
            # Set value to default
            self.value = ureg(f"{R_ZERO_DEFAULT}ohm")
            self.notes = f"{self.notes} ATTN: Resistance = 0 Ω, using {self.value} for calculations."

        # Applied power
        self.P_applied = (self.V_max_applied**2 / self.value).to('W')

        # Temp rise
        self.ΔT = (self.P_applied * self.θ_R)

        # Operating temp
        self.T_operating = self.T_baseplate + self.ΔT

        # Calculate T2 value
        self.T_zero_derated = UnitQuantity((R_P_DERATE * (self.T_zero.magnitude - self.T_rated.magnitude)), ureg.degC)
        self.T_zero_derated = UnitQuantity((self.T_zero_derated.magnitude + self.T_rated.magnitude), ureg.degC)

        self.over_power = False
        self.P_max_slope = 0.0

        if self.T_operating > self.T_zero:
            # Operating over the maximum rated temperature
            self.notes = f"{self.notes} ATTN: Operating temperature greater than zero-point temperature!"

        elif self.T_operating > self.T_rated and self.T_operating < self.T_zero:
            # Between rated and zero-point temperatures. Verify that applied power at operating temp falls below
            # the derated T1-T2 line
            self.P_max_slope = self.derated_power_slope()
            self.over_power = self.P_applied > self.P_max_slope
            self.notes = f"{self.notes} ATTN: Operating temperature greater than T1: used linear derating."
        
        if self.over_power:
            # At the given operating temp, operating at a power that is too high
            self.notes = f"{self.notes} ATTN: Power at operating temp greater than linear derating!"

        # Power derating by multiplicative constant
        self.P_rating_derated = R_P_DERATE * self.P_rating
        if self.P_max_slope > 0.0:
            # Linear derating was done. Use the min between the two calculated P derating values
            self.P_rating_derated = min([self.P_max_slope, self.P_rating_derated])
        elif self.P_max_slope < 0.0:
            # We're calculating negative powers because we're getting power values at too high a temp
            self.notes = f"{self.notes} Calcuated a negative power value from slope derating. Reported derated power value is derated via multiplicative constant."

        # Max voltage rating, calculated from derated power rating
        self.V_max = ((self.P_rating_derated * self.value)**0.5).to('V')

        # Calculate passing values
        self.derating_pass()

    def derated_power_slope(self):
        """Calculate the linear derating if operating temp is above T1

        Parameters
        ----------
        None

        Returns
        ----------
        value : UnitQuantity
            Power value on linear-derated slope at given operating temp
        """

        # Temperatures are weird w/ units - do operatings in chunks
        T2_minus_T1 = UnitQuantity((self.T_zero_derated.magnitude - self.T_rated.magnitude), ureg.degC)
        slope = UnitQuantity(-((self.P_rating.to('W')).magnitude / T2_minus_T1.magnitude), ureg.W/ureg.degC)

        T1_div_T2 = self.T_rated.magnitude/self.T_zero_derated.magnitude
        intercept = UnitQuantity(((self.P_rating.to('W')).magnitude / (1 - T1_div_T2)), ureg.W)

        # y = mx + b
        value = slope.magnitude * self.T_operating.magnitude + intercept.magnitude
        return UnitQuantity(value, ureg.W)

    def derating_pass(self):
        """Decide if the resistor passes derating

        Parameters
        ----------
        None

        Returns
        ----------
        None
        """

        # Choose smallest derated maximum voltage value
        vmax_compare = min([self.V_max, 0.8*self.V_rated_max])
        if vmax_compare == self.V_max:
            self.notes = f"{self.notes} ATTN: Maximum voltage calculated from √P*R"
        else:
            self.notes = f"{self.notes} ATTN: Maximum voltage calculated from {R_V_DERATE}*Vrated_max"

        # Calculate headroom values
        self.V_headroom = vmax_compare - self.V_max_applied
        if self.P_max_slope != 0.0:
            self.P_headroom = self.P_max_slope - self.P_applied
        else:
            self.P_headroom = self.P_rating_derated - self.P_applied
        self.T_headroom = UnitQuantity((self.T_zero_derated.magnitude - self.T_operating.magnitude), ureg.degC)

        # Decide if the resistor passes the deratings
        self.V_pass = self.V_headroom.magnitude > 0.0
        self.P_pass = self.P_headroom.magnitude > 0.0
        self.T_pass = self.T_headroom.magnitude > 0.0 
        # Total pass
        self.R_pass = self.V_pass and self.P_pass and self.T_pass

    def __str__(self):
        # String representation for pretty-printing
        return f"""\
Resistor {self.refdes}:
------------------
RPN: {self.rpn}
Value: {self.value}
Power Rating: {self.P_rating.to_compact():.3f}
Max V Applied: {self.V_max_applied.to_compact():.2f}
Baseplate Temp: {self.T_baseplate.to_compact():.1f}
Thermal Resistivity: {UnitQuantity(self.θ_R.magnitude, ureg.degC/ureg.W):.2f}
Max Rated V: {self.V_rated_max.to_compact():.2f}
Pulsed?: {self.pulse_bool}
Max Pulsed V: {self.V_max_pulse_applied.to_compact():.2f}
Rated Temp: {self.T_rated.to_compact():.1f}
Zero Temp: {self.T_zero.to_compact():.1f}
Notes: {self.notes}

CALCULATED & DERATED VALUES:
------------------
Applied Power: {self.P_applied.to_compact():.3f}
Temp Rise: {UnitQuantity(self.ΔT.magnitude, ureg.degC):.1f}
Operating Temp: {self.T_operating.to_compact():.1f}
Derated Power: {self.P_rating_derated.to_compact():.3f}
Derated Vmax: {self.V_max.to_compact():.2f}
Derated Zero Temp: {self.T_zero_derated.to_compact():.1f}

PASS?
------------------
V pass: {self.V_pass} (Headroom: {self.V_headroom.to_compact():.2f})
P pass: {self.P_pass} (Headroom: {self.P_headroom.to_compact():.3f})
T pass: {self.T_pass} (Headroom: {self.T_headroom.to_compact():.1f})
PASS: {self.R_pass}
"""


def analyze_resistors(R_csv_file=RESISTOR_CSV_FILENAME):
    """Analyze all resistors in the resistors CSV file

    Parameters
    ----------
    R_csv_file : str [default="resistors.csv"]
        Filename of the resistors CSV file. Must contain the file extension.

    Returns
    ----------
    Rs : list(Resistor Objects)
        List of all resistor objects
    """
    # Check if the CSV file exists
    print(f"Analyzing {R_csv_file}...")
    if not os.path.isfile(f"./{R_csv_file}"):
        raise Exception(f"Error: No resistors CSV file named {R_csv_file}! Exiting.")

    with open(R_csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # Skip header
        for idx, row in enumerate(reader):
            # Read in values from CSV
            refdes = row[0]
            rpn = row[1]
            value = ureg(f"{row[2]}Ω")
            P_rating = ureg(f"{row[3]}W")
            V_max_applied = ureg(f"{row[4]}V")
            T_baseplate = UnitQuantity(float(row[5]), ureg.degC)
            θ_R = UnitQuantity(float(row[6]), ureg.delta_degC/ureg.W)
            V_rated_max = ureg(f"{row[7]}V")
            pulse_bool = row[8]
            V_max_pulse_applied = ''

            # Check if pulsed is true
            if pulse_bool.lower() in ["true", "yes"]:
                pulse_bool = True
                V_max_pulse_applied = ureg(f"{row[9]}V")
            else:
                pulse_bool = False
                V_max_pulse_applied = ureg("0V")
            T_rated = UnitQuantity(float(row[10]), ureg.degC)
            T_zero = UnitQuantity(float(row[11]), ureg.degC)
            notes = row[12]
            
            # Add values to dataclass
            R = Resistor(
                refdes=refdes,
                rpn=rpn,
                value=value,
                P_rating=P_rating,
                V_max_applied=V_max_applied,
                T_baseplate=T_baseplate,
                θ_R=θ_R,
                V_rated_max=V_rated_max,
                pulse_bool=pulse_bool,
                V_max_pulse_applied=V_max_pulse_applied,
                T_rated=T_rated,
                T_zero=T_zero,
                notes=notes
            )
            R.calc_and_derate()
            # dprint(R)
            Rs.append(R)
    return Rs

def write_resistors_to_excel(filename=EXCEL_FILENAME):
    """Write all the EPSA results to the Resistors sheet

    Parameters
    ----------
    filename : str [default: "epsa-results.xlsx"]
        Filename to write the results to. Must contain the file extension.

    Returns
    ----------
    None
    """
    print(f"Writing Resistor EPSA results to {filename}...")
    # Header text for the sheet
    headers = [
        "Ref Des",
        "RES",
        "Value",
        "Power Rating",
        "Max V Applied",
        "Baseplate Temperature",
        "Thermal Resistivity",
        "Max Rated V",
        "Pulsed?",
        "Max Pulsed V",
        "Rated Temp (T1)",
        "Zero-Point Temp (T3)",
        "Applied Power",
        "Temp Rise",
        "Operating Temp",
        "Derated Power",
        "Derated Max V",
        "Derated Zero-Point Temp (T2)",
        "Voltage Pass",
        "Voltage Headroom",
        "Power Pass",
        "Power Headroom",
        "Temp Pass",
        "Temp Headroom",
        "Overall Pass",
        "Notes"
    ]

    wb = load_workbook(filename)

    # Check if the Resistors sheet exists. If not, create it
    if "Resistors" not in wb.get_sheet_names():
        wb.create_sheet("Resistors")

    # Change to Resistors sheet and add headers 
    ws = wb["Resistors"]
    ws.append(headers)

    for resistor in Rs:
        # Write all values
        # If resistor value was 0 Ω, change it back
        if resistor.value == ureg(f"{R_ZERO_DEFAULT}ohm"):
            resistor.value = ureg("0ohm")
        vals = [
            f"{resistor.refdes}",
            f"{resistor.rpn}",
            f"{resistor.value.to_compact():~P.1f}",
            f"{resistor.P_rating.to_compact():~P.1f}",
            f"{resistor.V_max_applied.to_compact():~P.2f}",
            f"{resistor.T_baseplate.to_compact():~P.1f}",
            f"{UnitQuantity(resistor.θ_R.magnitude, ureg.degC/ureg.W):~P.1f}",
            f"{resistor.V_rated_max.to_compact():~P.2f}",
            f"{resistor.pulse_bool}",
            f"{resistor.V_max_pulse_applied.to_compact():~P.2f}",
            f"{resistor.T_rated.to_compact():~P.1f}",
            f"{resistor.T_zero.to_compact():~P.1f}",
            f"{resistor.P_applied.to_compact():~P.2f}",
            f"{UnitQuantity(resistor.ΔT.magnitude, ureg.degC):~P.1f}",
            f"{resistor.T_operating.to_compact():~P.1f}",
            f"{resistor.P_rating_derated.to_compact():~P.2f}",
            f"{resistor.V_max.to_compact():~P.2f}",
            f"{resistor.T_zero_derated.to_compact():~P.1f}",
            f"{resistor.V_pass}",
            f"{resistor.V_headroom.to_compact():~P.2f}",
            f"{resistor.P_pass}",
            f"{resistor.P_headroom.to_compact():~P.2f}",
            f"{resistor.T_pass}",
            f"{resistor.T_headroom.to_compact():~P.2f}",
            f"{resistor.R_pass}",
            f"{resistor.notes}"
        ]
        ws.append(vals)

    # Center all text vertically and horizontally
    for row in range(1, ws.max_row+1):
        for col in range(1, ws.max_column+1):
            cell = ws.cell(row, col)
            cell.alignment = Alignment(horizontal="center", vertical="center")

    if DEBUG:
        wb.save(f"{filename[:-5]}_resistors.xlsx")
        wb.close()
    else:
        wb.save(filename)
        wb.close()


def get_R_passes():
    """Get all the passing values for the resistors

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """
    r_v_pass_list = PassClass("V Passes", 0)
    r_p_pass_list = PassClass("P Passes", 0)
    r_t_pass_list = PassClass("T Passes", 0)
    r_pass_list = PassClass("Overall Passes", 0)
    for R in Rs:
        if R.V_pass:
            r_v_pass_list.pass_num += 1
        if R.P_pass:
            r_p_pass_list.pass_num += 1
        if R.T_pass:
            r_t_pass_list.pass_num += 1
        if R.R_pass:
            r_pass_list.pass_num += 1

    r_passes = Passes("Resistors", len(Rs),
    [
        r_pass_list,
        r_v_pass_list,
        r_p_pass_list,
        r_t_pass_list
    ])
    dprint(r_passes)
    return r_passes

        

