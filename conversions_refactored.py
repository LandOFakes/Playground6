class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        "Celsius": {"Fahrenheit": convertCelsiusToFahrenheit, "Kelvin": convertCelsiusToKelvin},
        "Fahrenheit": {"Celsius": convertFahrenheitToCelsius, "Kelvin": convertFahrenheitToKelvin},
        "Kelvin": {"Celsius": convertKelvinToCelsius, "Fahrenheit": convertKelvinToFahrenheit},
        "Miles": {"Yards": lambda x: x * 1760, "Meters": lambda x: x * 1609.34},
        "Yards": {"Miles": lambda x: x / 1760, "Meters": lambda x: x * 0.9144},
        "Meters": {"Miles": lambda x: x / 1609.34, "Yards": lambda x: x / 0.9144},
    }
