class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        "Celsius": {"Kelvin": lambda c: c + 273.15, "Fahrenheit": lambda c: (c * 9/5) + 32},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
    }
    
    if fromUnit == toUnit:
        return value  # Identity conversion

    try:
        return round(conversions[fromUnit][toUnit](value), 2)
    except KeyError:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")
