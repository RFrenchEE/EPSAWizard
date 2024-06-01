"""qss_translate.py

A processor for epsa_wizard.qss to apply variable definitions found
in this file. 
"""

import re

# DEFINE UI SCHEMES
# Use dashes only
_dark_uischeme = {
    # COLORS
    "color-white": "#ffffff",
    "color-black": "#000000",
    "color-dark" : "#242226",
    "color-dark-lightened" : "#a2a0a5",
    "color-primary": "#6002ee",
    "color-primary-highlight": "#9965f4",
    "color-primary-lowlight": "#3d00e0",

    "color-secondary": "#90ee02",
    "color-secondary-highlight": "#c6f68d",
    "color-secondary-lowlight": "#61d800",

    # WIDTHS
    "width-border-button": "1px",
    "width-border-button-pressed": "2px",
    "width-border-textedit": "1px",
    "width-border-groupbox": "1px",
    "width-border-combobox": "1px",

    # RADII
    "radius-button": "4px",
    "radius-groupbox": "4px",
    "radius-textedit": "4px",
    "radius-combobox": "4px",

    # PADDING
    "padding-button": "1px",
    "padding-groupbox": "8px",

    # MARGINS
    "margin-top-groupbox": "6px"
}


# TODO: Write documentation
def load_epsa_qss():
    # Sort the variable dictionary by key length (longest first), just in case subscripting would otherwise cause errors
    # For example, if we had two variables
    # color-primary and color-primary-bright,
    # the former may get replaced first, leaving the second broken in the resulting qss
    sorted_keys = sorted(_dark_uischeme.keys(), key=len, reverse=True)
    _qss_var_dict_local = dict(zip(sorted_keys, [_dark_uischeme[key] for key in sorted_keys]))

    # Load the qss_comp file, which has variables defined with
    # prepended ampersands. Example: @color-dark
    with open("./ui/epsa_wizard.qss_comp", 'r') as f:
        _style = f.read()

    # Substitute all variables
    # Example: @color-dark -> #1e1d23 (or whatever is defined above)
    for attr, val in _qss_var_dict_local.items():
        _style = re.sub(
            f"@{attr}",
            f"{val}",
            _style
        )
    
    # Write qss to qss file for easier viewing in some editors
    with open("./ui/epsa_wizard.qss", 'w') as f:
        f.write(_style)

    return _style