import pint

# Unit registry
ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=False)
pint.set_application_registry(ureg)

# Pretty print all units
ureg.default_format = "~P"

# Define quantity
UnitQuantity = pint.Quantity