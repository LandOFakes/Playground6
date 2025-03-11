class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        "Celsius": {
            "Kelvin": lambda c: c + 273.15,
            "Fahrenheit": lambda c: (c * 9/5) + 32
        },
        "Fahrenheit": {
            "Celsius": lambda f: (f - 32) * 5/9,
            "Kelvin": lambda f: (f - 32) * 5/9 + 273.15
        },
        "Kelvin": {
            "Celsius": lambda k: k - 273.15,
            "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
        },  # Missing comma was needed here
        "Miles": {
            "Yards": lambda m: m * 1760,
            "Meters": lambda m: m * 1609.34
        },
        "Yards": {
            "Miles": lambda y: y / 1760,
            "Meters": lambda y: y * 0.9144
        },
        "Meters": {
            "Miles": lambda me: me / 1609.34,
            "Yards": lambda me: me / 0.9144
        },
    }
    
    if fromUnit == toUnit:
        return value  # Identity conversion

    try:
        return round(conversions[fromUnit][toUnit](value), 2)
    except KeyError:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")

