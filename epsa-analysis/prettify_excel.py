# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# prettify_excel: Modify the EPSA Excel file  
# ----------------------------------------------------------------
# Created by    : Ryan French
# Created date  : 07/19/2023
# ----------------------------------------------------------------

from utilities import *

def style_overview_sheet(worksheet):
    """Style the Overview sheet 

    Parameters
    ----------
    worksheet : Excel Worksheet object

    Returns
    ----------
    None
    """
    ws = worksheet

    # Set column widths and row heights
    ws.column_dimensions['A'].width = 8.5
    ws.column_dimensions['B'].width = 19.6
    ws.column_dimensions['C'].width = 20.7
    ws.column_dimensions['D'].width = 12.4
    ws.column_dimensions['E'].width = 8.4
    ws.column_dimensions['F'].width = 8.5
    ws.row_dimensions[1].height = 72
    ws.row_dimensions[2].height = 43
    ws.row_dimensions[7].height = 10

    for x in range(3, 7):
        ws.row_dimensions[x].height = 16
    for x in range(8, 201):
        ws.row_dimensions[x].height = 16

    # Do cell merging
    ws.merge_cells("B2:E2")
    ws.merge_cells("C3:E3")
    ws.merge_cells("C4:E4")
    ws.merge_cells("C5:E5")
    ws.merge_cells("C6:E6")
    ws.merge_cells("B8:E8")

    # Resistor merging
    ws.merge_cells("B10:B13")
    ws.merge_cells("C10:C13")
    # Capacitor merging
    ws.merge_cells("B14:B16")
    ws.merge_cells("C14:C16")
    # Inductor merging
    ws.merge_cells("B17:B19")
    ws.merge_cells("C17:C19")

    # Add text
    ws["B2"] = "Electronic Part Stress Analysis Results"
    ws["B2"].font = Font(size=20, bold=True)
    ws["B2"].alignment = Alignment(horizontal="center", vertical="center") 

    ws["B3"] = "Project Name"
    ws["B3"].font = Font(size=14, bold=True)
    ws["B3"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["C3"] = PROJECT_NAME
    ws["C3"].font = Font(size=14)
    ws["C3"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["B4"] = "Board"
    ws["B4"].font = Font(size=14, bold=True)
    ws["B4"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["C4"] = BOARD_NAME
    ws["C4"].font = Font(size=14)
    ws["C4"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["B5"] = "PCB"
    ws["B5"].font = Font(size=14, bold=True)
    ws["B5"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["C5"] = f"{PCB_RES} Rev. {PCB_REV}"
    ws["C5"].font = Font(size=14)
    ws["C5"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["B6"] = "PCA"
    ws["B6"].font = Font(size=14, bold=True)
    ws["B6"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["C6"] = f"{PCA_RES} Rev. {PCA_REV}"
    ws["C6"].font = Font(size=14)
    ws["C6"].alignment = Alignment(horizontal="left", vertical="center") 

    ws["B8"] = "EPSA Pass Overview"
    ws["B8"].font = Font(size=12, bold=True)
    ws["B8"].alignment = Alignment(horizontal="center", vertical="center") 
    ws["B8"].fill = PatternFill(start_color="2F75B5", end_color="2F75B5", fill_type="solid")

    ws["B9"] = "Component Type"
    ws["B9"].font = Font(size=12, bold=True)
    ws["B9"].alignment = Alignment(horizontal="center", vertical="center") 
    ws["B9"].fill = PatternFill(start_color="9BC2E6", end_color="9BC2E6", fill_type="solid")

    ws["C9"] = "Number Analyzed"
    ws["C9"].font = Font(size=12, bold=True)
    ws["C9"].alignment = Alignment(horizontal="center", vertical="center") 
    ws["C9"].fill = PatternFill(start_color="9BC2E6", end_color="9BC2E6", fill_type="solid")

    ws["D9"] = "Pass Type"
    ws["D9"].font = Font(size=12, bold=True)
    ws["D9"].alignment = Alignment(horizontal="center", vertical="center") 
    ws["D9"].fill = PatternFill(start_color="9BC2E6", end_color="9BC2E6", fill_type="solid")

    ws["E9"] = "Passes"
    ws["E9"].font = Font(size=12, bold=True)
    ws["E9"].alignment = Alignment(horizontal="center", vertical="center") 
    ws["E9"].fill = PatternFill(start_color="9BC2E6", end_color="9BC2E6", fill_type="solid")

    # Add Redwire image
    img_loader = SheetImageLoader(ws)
    # Check if image exists. If not, add it
    if not img_loader.image_in("B1"):
        rw_img = ExcelImage("redwire-logo.png")
        rw_img.anchor = "B1"
        ws.add_image(rw_img)

    # Add borders
    thin = Side(border_style="medium")
    thick = Side(border_style="thick")
    # Project info borders
    ws["B3"].border = Border(top=thick, left=thick, right=thick)
    ws["C3"].border = Border(top=thick)
    ws["D3"].border = Border(top=thick)
    ws["E3"].border = Border(top=thick, right=thick)
    ws["B4"].border = Border(left=thick, right=thick)
    ws["E4"].border = Border(right=thick)
    ws["B5"].border = Border(left=thick, right=thick)
    ws["E5"].border = Border(right=thick)
    ws["B6"].border = Border(bottom=thick, left=thick, right=thick)
    ws["C6"].border = Border(bottom=thick)
    ws["D6"].border = Border(bottom=thick)
    ws["E6"].border = Border(bottom=thick, right=thick)
    # Overview borders
    ws["B8"].border = Border(top=thick, bottom=thin, left=thick)
    ws["C8"].border = Border(top=thick, bottom=thin)
    ws["D8"].border = Border(top=thick, bottom=thin)
    ws["E8"].border = Border(top=thick, bottom=thin, right=thick)
    ws["B9"].border = Border(bottom=thin, left=thin, right=thin)
    ws["C9"].border = Border(bottom=thin, left=thin, right=thin)
    ws["D9"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E9"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B10"].border = Border(left=thick, right=thin)
    ws["C10"].border = Border(left=thin, right=thin)
    ws["D10"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E10"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B11"].border = Border(left=thick, right=thin)
    ws["C11"].border = Border(left=thin, right=thin)
    ws["D11"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E11"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B12"].border = Border(left=thick, right=thin)
    ws["C12"].border = Border(left=thin, right=thin)
    ws["D12"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E12"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B13"].border = Border(bottom=thick, left=thick, right=thin)
    ws["C13"].border = Border(bottom=thick, left=thin, right=thin)
    ws["D13"].border = Border(bottom=thick, left=thin, right=thin)
    ws["E13"].border = Border(bottom=thick, left=thin, right=thick)
    ws["B14"].border = Border(left=thick, right=thin)
    ws["C14"].border = Border(left=thin, right=thin)
    ws["D14"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E14"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B15"].border = Border(left=thick, right=thin)
    ws["C15"].border = Border(left=thin, right=thin)
    ws["D15"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E15"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B16"].border = Border(bottom=thick, left=thick, right=thin)
    ws["C16"].border = Border(bottom=thick, left=thin, right=thin)
    ws["D16"].border = Border(bottom=thick, left=thin, right=thin)
    ws["E16"].border = Border(bottom=thick, left=thin, right=thick)
    ws["B17"].border = Border(left=thick, right=thin)
    ws["C17"].border = Border(left=thin, right=thin)
    ws["D17"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E17"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B18"].border = Border(left=thick, right=thin)
    ws["C18"].border = Border(left=thin, right=thin)
    ws["D18"].border = Border(bottom=thin, left=thin, right=thin)
    ws["E18"].border = Border(bottom=thin, left=thin, right=thick)
    ws["B19"].border = Border(bottom=thick, left=thick, right=thin)
    ws["C19"].border = Border(bottom=thick, left=thin, right=thin)
    ws["D19"].border = Border(bottom=thick, left=thin, right=thin)
    ws["E19"].border = Border(bottom=thick, left=thin, right=thick)


def style_epsa_sheets(filename=EXCEL_FILENAME):
    """Style the EPSA sheets (everything except the Overview sheet) 

    Parameters
    ----------
    filename : string
        Filename of the Excel workbook. Must contain the .xlsx extension.

    Returns
    ----------
    None
    """

    dprint("Style EPSA sheets...")
    wb = load_workbook(filename)
    sheets_to_style = wb.get_sheet_names()

    # Get rid of Overview sheet
    sheets_to_style.remove("Overview")

    for sheet in sheets_to_style:
        ws = wb[sheet]
        bold_font = Font(bold=True)
        for rows in ws.iter_rows(min_row=1, max_row=1, min_col=1):
            for cell in rows:
                # Bold the header row
                cell.font = bold_font

    wb.save(filename)
    wb.close()


def auto_column_width(filename=EXCEL_FILENAME):
    """Auto-scale the column widths of the EPSA sheets

    Parameters
    ----------
    filename : string
        Filename of the Excel workbook. Must contain the .xlsx extension.

    Returns
    ----------
    None
    """

    dprint("Automatic column widths...")
    wb = load_workbook(filename)

    for sheet in wb.get_sheet_names():
        ws = wb[sheet]
        for column in ws.columns:
            max_len = 0
            col_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_len:
                        max_len = len(cell.value)
                except:
                    pass
            
            # Set column width to maximum string length + scaling factor
            adj_width = (max_len + 5)
            ws.column_dimensions[col_letter].width = adj_width

    sheets_to_style = wb.get_sheet_names()

    # Get rid of the Overview sheet
    sheets_to_style.remove("Overview")

    # Need smaller scaling for notes columns because of the long strings
    for sheet in sheets_to_style:
        ws = wb[sheet]
        for column in ws.columns:
            if column[0].value.lower() == "notes":
                # Set width to 30
                col_letter = column[0].column_letter
                ws.column_dimensions[col_letter].width = 30
            else:
                # Note a notes column
                continue
            
            # Left-align all cells and wrap text
            for cell in column:
                try:
                    if cell.value.lower() == "notes":
                        pass
                    else:
                        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                except AttributeError:
                    pass
    
    wb.save(filename)
    wb.close()

def highlight_passes(filename=EXCEL_FILENAME):
    """Highlight the Pass/Fail columns of the EPSA sheets.

    Parameters
    ----------
    filename : string
        Filename of the Excel workbook. Must contain the .xlsx extension.

    Returns
    ----------
    None
    """

    dprint("Highlighting passing criteria...")
    wb = load_workbook(filename)

    sheets_to_style = wb.get_sheet_names()

    # Get rid of the Overview sheet
    sheets_to_style.remove("Overview")

    red_fill = PatternFill(start_color="ff0000", end_color="ff0000", fill_type="solid")
    green_fill = PatternFill(start_color="00ff00", end_color="00ff00", fill_type="solid")

    for sheet in sheets_to_style:
        ws = wb[sheet]
        for column in ws.columns:
            # Look for the word "Pass" in the column headers
            if "Pass" in column[0].value:
                for cell in column:
                    if cell.value == "True":
                        cell.fill = green_fill
                    elif cell.value == "False":
                        cell.fill = red_fill
    
    wb.save(filename)
    wb.close()